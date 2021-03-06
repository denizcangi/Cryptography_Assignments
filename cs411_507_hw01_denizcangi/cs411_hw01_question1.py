# -*- coding: utf-8 -*-
"""cs411_hw01_question1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ugYojFdPZHQ__6w5b3G8gqmn4KCAJHp1
"""

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}

inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
          8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
          16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
          24:'Y', 25:'Z'}

def letterToNumber(text): #encode the letters

  listOfNum= []
  for char in text:
    listOfNum.append(uppercase[char])

  print("Encoding of the letters in ciphertext is:", listOfNum)
  return listOfNum

def NumberToLetter(listOfNum):

  text=''
  print()
  print("Possible keys and the decyrpted texts with these keys: ")

  for key in range(26): #try all the numbers in the alphabet as key and find the text
    for num in listOfNum:
      textAndKey = (num+key)%26
      text+=inv_uppercase[textAndKey]

    if key==9 or key== 16: 
      print('')
      print(key, text)
    
    text=''


text= "NYVVC"
num = letterToNumber(text)
NumberToLetter(num)
print()
print("Keys that give meaningful plaintexts are 9 and 16, 9 gives plaintext WHEEL and 16 gives plaintext DOLLS.")