#格式化输出
# 练习 1
num=110
# %d,%i 带符号的十进制数
print('%d'%num)
print('%i'%num)
# %o 不带符号的八进制
print('%o'%num)
# %u 不带符号的十进制
print('%u'%num)
# %x 不带符号的十六进制(小写)
print('%x'%num)
# %X 不带符号的十六进制(大写)
print('%X'%num)
# %e 科学计数法表示浮点数(小写)
print('%e'%num)
# %E 科学计数法表示浮点数(大写)
print('%E'%num)
# %f,%F 十进制浮点数
print('%f'%num,' %F'%num)
# %s 输出字符串
print('%s'%num)
num=12.345
print('%f'%num)
print('%F'%num)
city='上海'
print('我现在居住的城市是%s'%city)



#练习2，精度
num=123
print('%d'%num)
print('%5d'%num)
print('%05d'%num)

score=123.456
print('%f'%score)
print('%5.2f'%score)
print('%7.2f'%score)
print('%07.2f'%score)




















