# -*- coding: iso-8859-15 -*-
import random;

print("Dette er Ullern's passord generator. \nDet er viktig å ha et sikkert og langt passord. Dette er på grunn av muligheten til å knekke passord basert på lengde, jo lengere passordet er, desto flere forskjellige kombinasjoner er mulig.",
"\n\nHvorfor bruke min generator istede for å lage et eget passord?", 
"\n- Passord generatoren vil bruke helt tilfeldige tall, symboler og bokstaver. Dette vil eliminere den personifiserte passord typen som også 'svekker' passord. ",
"\n\nEkstra tips: ",
"\n- Dette vil ikke være et uhackbar passord, muligheten er alltid der. Men om det skjer er det mest sansynnelig at ditt passord er på aveie.",
"\n- Vær kritisk med å bruke samme passord på flere sider, spør deg selv hvor mange ganger har du brukt samme passord, på forskjellige sider?",
"\n- En fin side for å få oversikt av databrudd du kan være rammet av: https://haveibeenpwned.com/ ",
"\n- Hvor bør jeg lagre passord? Passord bør etter MIN mening lagres fysisk og ikke på PCen noe sted for optimal sikkerhet."

)
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
        

    print(generertPassord)

if __name__ == '__main__':
    __main__()

    