liste = list(range(1,101))

new_list = []
for i in liste:
    
    if i % 3 == 0 and i % 5 == 0:
        new_list.append('FizzBuzz')
    elif i % 5 == 0:
        new_list.append('Buzz')
    elif i % 3 == 0:
        new_list.append('Fizz')
    else:
        new_list.append(i)

print(new_list)
