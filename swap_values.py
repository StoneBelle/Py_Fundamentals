# GOAL: Swap the values of var a & b wo a temp var

a = 5
b = 6


# a becomes 11
a = a + b

# b becomes 5
b = a - b

# a becomes 6
a = a - b


# Easier way
# a, b = b, a


cookie1= "oreo"
cookie2 ="choco-chip"


cookie1, cookie2 = cookie2, cookie1
print(f"cookie1: {cookie1}")
print(f"cookie2: {cookie2}")


nums = list("56")

print(type(nums))

x = 0 
for num in nums:
    print(type(num))
    x += int(num) 

print(x)

