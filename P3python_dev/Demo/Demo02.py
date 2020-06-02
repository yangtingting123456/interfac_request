#python 基础
#1.查了python两个变量的地址
a=10
b=20
print(id(a))
print(id(b))
#2.两个数值进行交换
tmp=a
a=b
b=tmp
print(a)
print(b)
print(id(a))
print(id(b))
