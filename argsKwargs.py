# *args - arguments
def sum2(*args):
    total =0
    for i in args:
        total+=i
    print(f"Сумма: {total}")
sum2(5,6,5,6,78)
#####
a = [1,2,3,4]
b = [*a,5,6,7,8,9] 
print(b)
#####
def printPoint(student, *args):
    print(f"{student}")
    for i in args:
        print("Балл: ", i)
    
printPoint('Bayel', 40,50)


# **kwargs - keyword arguments - dict {}
def show(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

show(name='Gena', age=45, city='Bishkek', gender='Male')
####
def pets(owner, **kwargs):
    print(f"Владелец: {owner}")
    for k,v in kwargs.items():
        print(k,v)

pets('Davlet', dog='Bobik', cat="Lol", eats=['fish', 'meat'])


import re #регулярные выражения
my_str = 'wegf6grgr56egfreg576'
nums = re.findall('[0-9]+', my_str)
numbers = []
for i in nums:
    numbers.append(int(i))
print(numbers)
#########
nums = [] # внутри должны лезжать только числа
tem = ''
for i in my_str:
    if i.isdigit():
        tem += i
    elif tem:
        nums.append(int(tem))
        tem = ''
if tem:
    nums.append(int(tem))        
print(nums)