# #列表常用的操作方法
# stu=['张三','李四','王二','麻子','a','aa','a']
# print('stu=%s'%stu)
# # L.append(var) #追加元素
# stu.append('田七')
# print(stu)
# # L.insert(index,var) #在指定位置插入元素
# stu.insert(6,'和九')
# print(stu)
# # L.pop(var) #返回最后一个元素，并从 list 中删除之
# a=stu.pop(0)
# print(a)
# # L.remove(var) #删除第一次出现的该元素
# stu.remove('李四')
# print(stu)
# # L.count(var) #该元素在列表中出现的个数
# b=stu.count('a')
# print(b)
# # L.index(var) #该元素的位置,无则抛异常a
# print('麻子的下标：',stu.index('麻子'))
#
# # L.extend(list) #追加 list，即合并 list 到 L 上
# score=[90,87,90,98,78,87]
# stu.extend(score)
# print(stu)
# # L.sort() #排序
# score=[100,338,-9,0,2376,872,6,2387,99]
# score.sort(reverse=True)
# print(score)
# # L.reverse() #反转
# score.reverse()
# print(score)
# print(score[0:3])

#list复制
score=[90,87,90,98,78,87]
score2=score[:]
print(score)
print(score2)

score3=score
print(score3)

score3[2]=123
print(score)

print(id(score))
print(id(score2))
print(id(score3))
#
# score=[100,200,300] #值传递
# score2=score[:]
# print(score)
# print(score2)
# #地址传递
# score3=score
# print(score3)
# #假设我们改变 score3 的值，score 的值会不变不？
# score3[2]=123
# print(score)
# print(id(score))
# print(id(score2))
# print(id(score3))