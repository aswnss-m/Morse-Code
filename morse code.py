"""
This program is a morse code generator
Morse Code : is an encrypted code language that is used by military personals to exchange messages over radio
, but this is no longer used by them i think
A":"._          1":".____
B":"_...        2":"..___
C":"_._.        3":"...__
D":"_..         4":"...._
E":".           5":".....
F":".._.        6":"_....
G":"__.         7":"__...
H":"....        8":"___..
I":"..          9":"____.
J":".___        0":"_____
K":"_._
L":"._..
M":"__
N":"_.
O":"___
P":".__.
Q":"__._
R":"._.
S":"...
T":"_
U":".._
V":"..._
W":".__
X":"_.._
Y":"_.__
Z":"__ ..
"""
#givem below is the key mapping used in the morse code do not tamper with it
morse_code = {"A":"._","B":"_...","C":"_._.","D":"_..","E": ".","F":".._.","G":"__.","H":"....","I":"..","J":".___","K":"_._","L":"._..","M":"__","N":"_.","O":"___","P":".__.","Q":"__._","R":"._.","S":"...","T":"_","U":".._","V":"..._","W":".__","X":"_.._","Y":"_.__","Z":"__ .."}
#Given below the is number mapping used in morse code
morse_code_num = {'1':".____",'2':"..___",'3':"...__",'4':"...._",'5':".....",'6':"_....",'7':"__...",'8':"___..",'9':"____.",'0':"_____"}

import time
import os #this import is to copy the final output into the clipboard so that we can send to someone
message = "" #this variable is used to store the output data
run = 'y'

while run == 'y':
    print("What do you want to do ?")
    print("1.Translate to Morse Code ")
    print("2.Decode morse code")
    option = input("Enter your option (1 or 2) : ")
    try :
        #down below is the code for creating morse code from string
        if option == '1' :
            string  = input("Enter the message : ")
            for text in string.upper():  #Here the string is capitalized to suite the words in the above morse code dictionary : L40 - L65
                if text == " ":
                    message = message + "  "
                else:
                    if text.isnumeric(): #To differenciate the numbers from the charactor , i divided this encrytion between charactors and numbers to make the workload less (this way its more faster)
                        for y in morse_code_num:
                            if text == y:
                                message = message + morse_code_num[y] + " "
                    else :
                        for x in morse_code:
                            if text == x:
                                message = message + morse_code[x] + " "
            print("Morse Code : ",message)
            print("\n\nThe Morse code have been copied to the clipboard !!")
            os.system('echo' + message + '| clip') #this code is to copy the output message to the clipboard , an extra feature


        #given below is the code for decoding morse code into message (string)
        #this part was tricky because we need to differenciate each words and each letters of the words
        #So i went with " " single space seperation for each letters and "  " double space seperation for each words
        elif option == '2':
            print ("Use \" \" (single space)to seperate each letter and \"  \" (double space)  to seperate words ") #prompt the user about the spacing they have to follow
            string  = input("Enter the morse code : ")
            words = string.split("  ")
            for word in words :
                letters = word.split(" ")
                for letter in letters:
                    for code in morse_code :
                        if letter == morse_code[code]:
                            message = message + code
                    for code in morse_code_num:
                        if letter == morse_code_num[code]:
                            message = message + code
                message = message + " "
            print("Decoded message : ",message)
            print("\n\nThe message have been copied to the clipboard !!")
            os.system('echo' + message + '| clip')
            time.sleep('10')

        run = input("\n\nDo you want to go again ?\nThis will overwrite the previous message in your clipboard ! (y/n) : ")


    except ValueError:
        time.sleep(1)
        print("You have entered wrong input")
        try :
            run = input("Do you want to go again (y / n) : ")
        except ValueError:
            print("Wrong input sorry , program crashed")
            run = 'n'


print("\n\n\nYou have exited from the program\n\n")
