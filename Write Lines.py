
#Import random module.
import random
#import string module.
import string

#the variable "alphabet" will store all the ASCII alphabet in lowercase.
alphabet = string.ascii_lowercase
#change string data type into a list. The variable "alphabet_list" will be listed.
alphabet_list = list(alphabet)
#the variable "typos" will store a set without any item. A set because if there are same character will be not counted.
typos = set()
#the variable "character_index" will store a set without any item. A set because if there are same character will be not counted.
character_index = set()
#the variable "sentence_index" will store a set without any item. A set because if there are same character will be not counted.
sentence_index = set()
#the variable "sentence_list" will store a list withou any item.
sentence_list = []

#those lines of code will indetify the 10 typos.
#while loop, the length of the variable "typos" is less than 10
while len(typos) < 10:
    #the variable "character" will be assigned a random item in the list "alphabet_list". used to choose the wrong characters.
    character = random.choice(alphabet_list)
    #the set "typos" will be added the variable "character" as a new item.
    typos.add(character)
#the variable "typos" will be changed into list from set.
typos = list(typos)

#those lines of code will indetify \xthe typos index in the sentence.
#while loop, the length of the variable "character_index" is less than 10.
while len(character_index) < 10:
    #the variable "number" will be assigned a random integer from 0 to 34. used to find wrong index of the varible "sentence".
    number = random.randint(0, 34)
    #the variable "character_index" will be added the variable "number" as a new item.
    character_index.add(number)
#change the set into list, the variable "character_index" will be listed.
character_index = list(character_index)

#those lines of code will indetify which sentence the typos are.
#while loop, while the length of the variable "sentence_index" is less than 10.
while len(sentence_index) < 10:
    #the variable "number" will be assigned a random integer from 0 to 34. used to find wrong index of the varible "sentence".
    number = random.randint(0, 100)
    #the variable "sentence_index" will be added the variable "number" as a new item.
    sentence_index.add(number)
#change the set into list, the variable "sentence_index" will be listed.
sentence_index = list(sentence_index)

#thhose line of code will transform the sentence into a list and put them into the parent list "sentence_list".
#for loop, for x in range of 100.
for x in range(100):
    #the variable "sentence" will store a string data type.
    sentence = "i will not forget to do my homework"
    #the parent list "sentence_list" will be appended a new list of variable "sentence".
    sentence_list.append(list(sentence))

#those line of code willtransform the typos in the sentences
#for loop, for x in range of 0 to 10.
for x in range(0, 10):
    #the variable "sentence_list[sentence_index[x]][character_index[x]]" will be changed into the variable "typos".
    sentence_list[sentence_index[x]][character_index[x]]= typos[x]

#those line will reproducethe sentence into string data type and print them.
#for loop, for x in range of 100.
for x in range(100):
    #the variable "sentence_list[x]" will be joined together to form a list. Convertion from list to string.
    sentence_list[x]=''.join(sentence_list[x])
    #print() function, print the variable "sentence_list".
    print(sentence_list[x])




                 
    
    
