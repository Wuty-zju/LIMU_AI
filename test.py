# 测试cuda版本和cudnn版本
import torch
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())

# 测试环境版本
