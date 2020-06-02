#1.python中标识符命令规则
#1.只能以数字，字母，_组成
#2.不能以数字开头
#3.不能用关键字
#4.标识符区分大小写



#2.python中数据类型，数字(number),列表（List），字符串（String），元组（tuple），字典（Dictionary），集合（set）
# 数字类型
# 1、整型
score=98
print('分数:%s'%score)
# 2、浮点型
money=1000.56
print('工资:',money)
# 3、bool 型
a=1==0
print(a)
if a:
    print('正确')
else:
    print('错误')
# 4、复数
c=100+20j
print(c)

#3.type()函数的用法，返回当前数值的类型
print(type(100+20j))
print(type(1))