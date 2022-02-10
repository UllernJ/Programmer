import random
import pyperclip

def __main__():  
    passwordLength = input("Insert the length you want your password: ")
    passwordLength = int(passwordLength) 

    passwordList = '1234567890+!"#¤%&/()=?`qwertyuiopasdfghjkl<>zxcvbnm,.-_:;*^~QWERTYUIOPASDFGHJKLZXCVBNM'
    arr = list(passwordList)

    i = 0
    generatedPassword = ""

    while(i < passwordLength):
        i += 1
        generatedPassword += random.choice(arr)
        

    print("\nYour password:", generatedPassword, "\nPassword has been copied to your clipboard.")
    pyperclip.copy(generatedPassword)

if __name__ == '__main__':
    __main__()

    