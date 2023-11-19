punishment_text = "I will not teach others to fly"

def bart_cheat_code(numb_of_repetition, punishment_text):
    
    string = print(f"{punishment_text}\n"*numb_of_repetition)
    return string

svar =  bart_cheat_code(3, 'Hei på deg')

print(svar)