#操作字符串
# String='I Love yangtingting'
# print(String[0:11])
# print(String[-1:]+'   jjj')
# print(String*7)

# str='Hello World!'
# print(str) # 输出完整字符串
# print(str[0]) # 输出字符串中的第一个字符
# print(str[2:5] ) # 输出字符串中第三个至第五个之间的字符串
# print(str[2:] ) # 输出从第三个字符开始的字符串
# print(str * 2 ) # 输出字符串两次
# print(str + "TEST") # 输出连接的字符串
# name='yang ting ting'
# print(name[3:8])
# print(name[8:])
# name2=name[:]
# print(name2)
# a1='liu'
# a2='guagn'
# print(a1+a2)
# print((a1+a2) *2)



#3.字符串常用操作
str='i Love china!'
# capitalize():将字符串第一个字符大写
print(str.capitalize())
# lower()：将整个字符串都小写
print(str.lower())
# upper()：将整个字符串都大写
print(str.upper())
# replace(old,[,new][,count]):将字符串中的 old 子串替换为 new，替换 count 次，默认全部替换
print(str.replace('i','I'))
# split(sep)：将字符串用给定的标准分割，并且以列表形式返回分割后的元素
strs=str.split('i')
print(strs)
print(type(strs))
fils='Demo_String_01.py'
fil=fils.split('.')
print(fil)
print(fil[1])



