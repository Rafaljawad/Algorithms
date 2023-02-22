#W=hello, v=[‘a’,’e’,’i’,’o’,’u’] write a python program to get the output [‘e’,’o’] using list comprehension


v = ['a', 'e', 'i', 'o', 'u']
w = "hello"
res = [w[index] for index in range(len(w)) if w[index] in v]
print(res)

#or
w='hello'
v=['a','e','i','o','u']

output=[char for char in w if char in v]
print(output)