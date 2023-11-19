empty_dict = {}

user_input = None
while True:
    
    user_input = input("User input: ")
    if user_input != 'revert':
        liste = user_input.split(';')
        empty_dict[liste[0]] = liste[1]
        print(empty_dict)
    elif user_input == 'revert':
        reverse_dict = {}
        for key, value in empty_dict.items():
            reverse_dict[value] = key

        print(empty_dict)
        print(reverse_dict)
        