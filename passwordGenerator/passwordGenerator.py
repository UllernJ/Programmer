import random
import pyperclip
import requests

def __main__():  
    passwordLength = input("Insert the length you want your password: ")
    passwordLength = int(passwordLength) 
    arr = list('1234567890+!"#¤%&/()=?`qwertyuiopasdfghjkl<>zxcvbnm,.-_:;*^~QWERTYUIOPASDFGHJKLZXCVBNM')

    i = 0
    generatedPassword = ""

    while(i < passwordLength):
        i += 1
        generatedPassword += random.choice(arr)

    print("\nYour password:", generatedPassword, "\nPassword has been copied to your clipboard.")
    pyperclip.copy(generatedPassword)

def wordGenerator():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()
    numberWords = int(input("Type in number of words you want in your password: "))
    password = ""
    i = 0
    nothing = ""
    symbols = list("1234567890<>zxcvbnm,.-_:;*^~+!#¤%&/()=?`")
    while(i < numberWords):
        i += 1
        choice = [nothing, random.choice(symbols)]
        sentence = ""
        sentence = str(random.choice(words), 'utf-8')
        password += ''.join(random.choice((str.upper, str.lower))(chr) for chr in sentence)
        password += ''.join(random.choice(choice))
    print(password, "\nYour password has been copied to clipboard")
    pyperclip.copy(password)





if __name__ == '__main__':
    userInput = input("Choose between two modes: \nThis mode will randomize all random characters. [Type 1]\nThis Mode will make more easier password (Still secure), with random words combined with numbers and symbols. [Type 2]\nType 1 or 2: ")
    userInput = int(userInput)
    if userInput == 1:
        __main__()

    elif userInput == 2:
        wordGenerator()

    else:
        print("Error, please type in either 1 or 2.")
    

    