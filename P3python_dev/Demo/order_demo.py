#手动在控制台输入五个数字
nums=input('请输入任意五个数字：')
print(type(nums))
num=nums.split(' ')
print(type(num))
num.sort()
print(num)
num_list=num.sort(reverse=True)
print('%s'%num_list)


