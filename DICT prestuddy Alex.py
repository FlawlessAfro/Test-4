info= {}
 
while True:
 
    user_input = input("INPUT: (end or print)").lower().strip()
    user_info = user_input.split()
 
    if len(user_info)==2:
        key, value =user_info
        if key in info:
            info[key].append(value)
        else:
            info[key] = [value]
    elif len(user_info) ==1:
        if(user_info[0]) == "print":
            print(info)
        elif(user_info[0] == "end"):
            print(info)
            break
        else:
            print("Invalid input")
    else:
        print("Invalid input")