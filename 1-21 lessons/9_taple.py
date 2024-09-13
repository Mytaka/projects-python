date = (3,4,5,1,6,"Text", 3.2, True) # - картеж
# data[0] = 5 - NO
print(date[2])
print(date[::])
print(date.count(6))
print(len(date))

date = (5,) # - картеж
date = 5,   # - картеж
date = 5,1,2,5,"Text" # - картеж

for i in date:
    print(i)

nums = [5,1,2,3,4]
text = "Hello world"
new_date = tuple(nums) # переделывание в картеж
T = tuple(text)        # переделывание в картеж
print(T, new_date)


