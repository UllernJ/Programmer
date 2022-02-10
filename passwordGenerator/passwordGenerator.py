# -*- coding: utf-8 -*-
import random
import pyperclip

def __main__():  
    passordLengde = input("Hvor langt vil du at passorde skal være?: ")
    passordLengde = int(passordLengde) 

    passordListe = '1234567890+!"#¤%&/()=?`qwertyuiopasdfghjkl<>zxcvbnm,.-_:;*^~QWERTYUIOPASDFGHJKLZXCVBNM'
    arr = list(passordListe)

    i = 0
    generertPassord = ""

    while(i < passordLengde):
        i += 1
        generertPassord += random.choice(arr)
        

    print("\nHer er ditt passord:", generertPassord, "\nPassord er kopiert.")
    pyperclip.copy(generertPassord)

if __name__ == '__main__':
    __main__()

    