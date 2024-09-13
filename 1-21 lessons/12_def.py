def test_func(a):
    print("Hwllo world", a, sep=" ")

test_func("Andrey")

def sum(a,b):
    return a + b

c = sum(11,4)
print(c)

# ---------------------------------------------------------------------------

nums =  [7,4,5,0,2,32,2]

def minim(nums):
    min = nums[0]
    for i in nums:
        if min > i:
            min = i
    return min
minimal = minim([7,4,5,1,2,32,2])
print(minimal)

# ---------------------------------------------------------------------------

a = lambda x,y: x*y
print(a(5,2))



