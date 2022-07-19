import collections
#from gameparser import *


chemicals = { 
    "1" : "Sulfuric acid", 
    "2": "Calcium fluoride", 
    "3" : "Iron", 
    "4": "Sodium "}

intro = {"story" : """Oh, shoot! You are in Bill Gate's Kitchen.
There are some chemicals in the kitchen!!! 
You suddenly remember what Bob—your A-level chemistry teacher—told you about HYDROFLUORIC ACID.
It is a colourless acid and can be deadly to humans, 
which can be useful later on."""}

possible_answer = { "1+2" : "hydrofluoric acid", "2+1" : "hydrofluoric acid",
"1+3" : "iron sulphate—Oops!Try again.", "3+1" : "iron sulphate—Oops!Try again.",
"3+2" : "unknown chemical—Oops!Try again.", "2+3" : "unknown chemical—Oops!Try again.", 
"2+4" : "calcium fluoride—Oops!Try again.","4+2" : "calcium fluoride—Oops!Try again.",
"4+1" : "sodium sulfate—Oops!Try again.","1+4" : "sodium sulfate—Oops!Try again.", 
"3+4" : "unknown chemical—Oops!Try again.", "4+3" : "unknown chemical—Oops!Try again."}

answer = { "1+2" : "hydrofluoric acid","2+1" : "hydrofluoric acid" }


def print_intro(intro): #print the intro
    print(intro["story"])


def print_chemicals(chemicals): #funtion to print the chemicals option
    chemicals_order = collections.OrderedDict(chemicals) #put the chemicals in order
    print("Use these chemicals to make hydrofluoric acid!!!")
    
    for element in chemicals_order:
        print(element, ":", chemicals[element])



def mix_chemicals(possible_answer, user_input): # mix the chemicals and give out the result
    for key in possible_answer:
        if user_input == key:
            result = possible_answer[key]
            print("You have created", result)

    
    if result == "hydrofluoric acid":
         print("Well done!!")
         return
       
       
       

        

def valid_answer(possible_answer, user_input): #check whether the user input is valid
    if user_input in possible_answer:
        return mix_chemicals(possible_answer,user_input)
    else:
        print("Invalid input.")


def menu2(possible_answer):
    #read player's input
    user_input = input ("> ")

    #normalised user input????

    #check whether the input is valid
    valid_answer(possible_answer, user_input)


    return valid_answer




def main():
    print_intro(intro)
    print_chemicals(chemicals)

    while True:
        menu2(possible_answer)
        

        
if __name__ == "__main__":
    main()
   




# make the function to normalise the input
# define winning -- sort of there
