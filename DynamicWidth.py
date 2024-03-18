m = int(input())
n = int(input())
result = '{:b}'.format(m)
result = result.zfill(n)
# zfill函数 如果字符串长度不够就填充剩余度的0
print(result)
