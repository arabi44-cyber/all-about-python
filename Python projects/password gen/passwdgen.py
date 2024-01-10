import numbers
import string
import random
# length of password
length = int(input("Enetr the password length: "))
if (length < 8 or length > 16) :
    print("password must be in lenghth between 8-16 character !!")

else:
    print('''Choose character set for password form these :
        1  Digitis
        2. Letters
        3. Special characters
        2. Exit ''')
    characterList=""
    #Getting character set for password

    while(True):
        choice = int(input(" Pick a number "))
        if(choice == 1):

            #Adding letters to possible characters
            characterList += string.digits
        elif(choice == 2):

            #Adding Digits to possible
            characterList += string.ascii_letters
        elif(choice == 3):

            #Adding special character to possible characters
            characterList += string.punctuation
        elif(choice == 4):
            break
        else:
            print("Please pick a valid option!")

    passwd = [""]
    for i in range(length):
        #Picking random character form our character list
        randomchar = random.choice(characterList)
        
        #appending a random chararacter to passwd
        passwd.append(randomchar)
    #Priting password as a string
    print("the random password is "+"".join(passwd))
  
#complete 