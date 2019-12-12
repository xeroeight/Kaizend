# Exercise 3
def func(var = 'hello'):
    return var
temp = ''
for i in range(3):
    temp += func()
print(temp)
