# my_nums = list(x * x for x in [1, 2 ,3])
# print(my_nums)


nums = [1,2,3,4,5,6]
my_nums = [n for n in nums if n%2 == 0]
print(my_nums)


my_list = filter(lambda n: n % 2 ==0 , nums)
print(list(my_list))