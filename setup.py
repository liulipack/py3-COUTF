#!user/bin/python
# 加载库
import random

# 输入参数
length = input('填充长度 :: ')
length = int(length)
frequency = input('创建文件 :: ')
frequency = int(frequency)
file_path = input('文件保存路径 :: ')
file_path = int(file_path)

# 定义随机填充内容函数
def fill():
    chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&')
    fill = ''
    for num in range(length):
        fill += random.choice(chars)
    return fill

# 创建文件
for num in range(frequency):
    num_Result = str(num)
    frequency_fix = eval(str(frequency)+'-1')
    frequency_Result = str(frequency_fix)
    file_name = file_path+'fill-'+num_Result+'.txt'
    fill_Result = str.encode(fill())
    f = open(file_name,'wb')
    f.write(fill_Result)
    f.close()
    print('进度 :: '+num_Result+'/'+frequency_Result)
