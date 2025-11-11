is_fast = True
if is_fast:
    car = 'Ferrari'
else:
    car = 'Tico'
print(car)
###### Тернарный оператор
print('Ferrari2' if is_fast else 'tico2')
####
a,b,c = 4,5,1 #множественное присвоение  
print(a if a>b and a>c else b if b>c else c )
# 
data = []
for i in range(100):
    if i % 2 == 0:
        data.append(i)
print(data)
#######Генератор списков
data2 = [i for i in range(100) if i %2==0]
print(data2)
