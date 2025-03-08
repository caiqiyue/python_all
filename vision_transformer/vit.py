import torch
from torch import nn

from einops import rearrange, repeat
from einops.layers.torch import Rearrange

# helpers

def pair(t):
    return t if isinstance(t, tuple) else (t, t)

# classes

class PreNorm(nn.Module):
    def __init__(self, dim, fn):
        super().__init__()
        self.norm = nn.LayerNorm(dim)#层归一化
        self.fn = fn#多头注意力
    def forward(self, x, **kwargs):
        return self.fn(self.norm(x), **kwargs)

class FeedForward(nn.Module):
    def __init__(self, dim, hidden_dim, dropout = 0.):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, hidden_dim),#1024 --> 2048
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, dim),#2048 --> 1024
            nn.Dropout(dropout)
        )
    def forward(self, x):
        return self.net(x)

class Attention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, dropout = 0.):
        super().__init__()
        inner_dim = dim_head *  heads#分头
        project_out = not (heads == 1 and dim_head == dim)

        self.heads = heads
        self.scale = dim_head ** -0.5

        self.attend = nn.Softmax(dim = -1)
        self.dropout = nn.Dropout(dropout)

        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)

        self.to_out = nn.Sequential(
            nn.Linear(inner_dim, dim),
            nn.Dropout(dropout)
        ) if project_out else nn.Identity()

    def forward(self, x):
        qkv = self.to_qkv(x).chunk(3, dim = -1)#q:1,65,128  k 和 v都是同样大小 128是因为 2个头 ，每个头 64
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = self.heads), qkv)#q:1,2,65,64
        #2个头，每个头 65个图片信息，每个图片信息用 64query 表示  k和 v同理
        dots = torch.matmul(q, k.transpose(-1, -2)) * self.scale#1,2,65,65 计算注意力得分

        attn = self.attend(dots)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)#和 value 相乘 1,2,65,64
        out = rearrange(out, 'b h n d -> b n (h d)')#合并头 1,65,128
        return self.to_out(out)

class Transformer(nn.Module):
    def __init__(self, dim, depth, heads, dim_head, mlp_dim, dropout = 0.):
        super().__init__()
        self.layers = nn.ModuleList([])
        for _ in range(depth):#多少个transformer的encoder块叠加
            self.layers.append(nn.ModuleList([
                PreNorm(dim, Attention(dim, heads = heads, dim_head = dim_head, dropout = dropout)),
                PreNorm(dim, FeedForward(dim, mlp_dim, dropout = dropout))
            ]))
    def forward(self, x):#1,65,1024
        for attn, ff in self.layers:
            x = attn(x) + x#1,65,1024  残差连接 norm + attention
            x = ff(x) + x# 1,65,1024  残差连接  norm + mlp
        return x

class ViT(nn.Module):
    def __init__(self, *, image_size, patch_size, num_classes, dim, depth, heads, mlp_dim, pool = 'cls', channels = 3, dim_head = 64, dropout = 0., emb_dropout = 0.):
        super().__init__()
        image_height, image_width = pair(image_size)#图片大小 256，256
        patch_height, patch_width = pair(patch_size)#图片块大小 32，32

        assert image_height % patch_height == 0 and image_width % patch_width == 0, 'Image dimensions must be divisible by the patch size.'

        num_patches = (image_height // patch_height) * (image_width // patch_width)#64，图片可以切分成多少个图片块
        patch_dim = channels * patch_height * patch_width#一个图片块 flatten之后，像素是多大
        assert pool in {'cls', 'mean'}, 'pool type must be either cls (cls token) or mean (mean pooling)'

        self.to_patch_embedding = nn.Sequential(
            Rearrange('b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1 = patch_height, p2 = patch_width),
            nn.Linear(patch_dim, dim),#将一个图片块的所有像素  线性映射到 1024
        )

        self.pos_embedding = nn.Parameter(torch.randn(1, num_patches + 1, dim))#位置编码
        self.cls_token = nn.Parameter(torch.randn(1, 1, dim))#在64个图片块信息前面加一个 cls信息
        self.dropout = nn.Dropout(emb_dropout)

        self.transformer = Transformer(dim, depth, heads, dim_head, mlp_dim, dropout)

        self.pool = pool
        self.to_latent = nn.Identity()#对数据不作任何修改，就是一个占位符，供以后修改模型结构

        self.mlp_head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_classes)#做预测
        )

    def forward(self, img):
        x = self.to_patch_embedding(img)#img:1,3,256,256  x:1,64,1024
        b, n, _ = x.shape#bach_size patches_num,dimesntion

        cls_tokens = repeat(self.cls_token, '1 n d -> b n d', b = b)#self.cls_token:1,1,1024
        x = torch.cat((cls_tokens, x), dim=1)#1,65,1024 64个图片patches和一个cls信息
        x += self.pos_embedding[:, :(n + 1)]#pos_embedding 1,65,1024
        x = self.dropout(x)#1,65,1024

        x = self.transformer(x)#1,65,1024

        x = x.mean(dim = 1) if self.pool == 'mean' else x[:, 0]#1,1024  要么就是 1，65，1024取平均，要么就是取第一个cls信息

        x = self.to_latent(x)#1,1024
        return self.mlp_head(x)#norm + mlp


if __name__ == '__main__':
    

    vision_transformer = ViT(
        image_size=256,patch_size=32,
        num_classes=4,dim=1024,
        depth=2,heads=2,mlp_dim=2048
        )
    # .cuda()
    x = torch.zeros(1,3, 256, 256)
    # x = torch.zeros(1,3, 224, 224).cuda()
    out = vision_transformer(x)#1,4 一张图片的四个分类概率
    print(out.shape)