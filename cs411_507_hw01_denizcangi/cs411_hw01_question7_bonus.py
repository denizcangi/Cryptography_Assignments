# -*- coding: utf-8 -*-
"""cs411_hw01_question7_BONUS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uoTfJMJtsU6zgkbOUL48G8EQab8VcMG_
"""

lowercase = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
         'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
         'r':17, 's':18,  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
         'z':25}

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}

inv_lowercase = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
         25:'z'}

inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z'}

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
         'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
         'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

english_frequences = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
					  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
					  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
					  0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

ordered_frequentLetters= ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L", "C", "U", "M", "W", "F", "G", "Y", "P", "B", "V", "K", "J", "X", "Z", "Q"]

def stringToList(text): #turn a string into list of chars

  listofText=[]

  for char in text:
    char=char.upper()
    if char in uppercase:

      listofText.append(char)
  
  return listofText

def shiftTheCiphertext(textList): #for shifting the ciphertext 1 by 1, tried at most 15 shifts
  maxCoincidence = 0
  PossibleKeyLength = 0

  for i in range(1, 15):
    numofCoincidence = 0
    for j in range(len(textList)-i):
      if textList[i+j] == textList[j]:
        numofCoincidence += 1
    
    if numofCoincidence > maxCoincidence:
      PossibleKeyLength = i
      maxCoincidence = numofCoincidence

  print("Possible key length is:", PossibleKeyLength, "and number of coincidence is", maxCoincidence)
  return PossibleKeyLength #possible key length is 7 with 38 coincidences

def applyFreqAnalysis(subCiphertext): #for 7 times I've calculated the frequency analysis and find the best suiting keys 

  for j in range(7):
    key = (uppercase[subCiphertext[0][0]]-uppercase[ordered_frequentLetters[j]])%26

    new_list=[]
    for i in range(len(subCiphertext)):
      new_num = (uppercase[subCiphertext[i][0]] - key)%26
      new_list.append(inv_uppercase[new_num])
    
    print(j, "th possible encryption list is", new_list)
    print("Key is", key)


def findMostRepeatedLetters(listOfLetters): #to find the most repeated letters in the subciphertext

  newletter_count = dict(letter_count)

  for i in listOfLetters:
    newletter_count[i] += 1
  
  sort_letters = sorted(newletter_count.items(), key=lambda x: x[1], reverse=True)
  
  print(sort_letters)
  applyFreqAnalysis(sort_letters)

def findTheKey(textList, keyLength): #it first creates the subciphertexts and then call the most repeated letters
  subciphertext= []
  for k in range(keyLength):
    newList = []
    newList.append(textList[k])
    subciphertext.append(newList)

  for j in range(keyLength, len(textList)):
    subciphertext[j%keyLength].append(textList[j])
  i=1
  for sub in subciphertext:
    print(" ")
    print(i, "th subciphertext")
    i=i+1
    print(sub)
    findMostRepeatedLetters(sub)

def decrypt(ciphertext, keyWord): #I've found the key by my own observation among the possible keys, 
#then tried if the key gives a meaningful decrypted message with the decrypt function

  keyNumber= [uppercase[i] for i in keyWord]

  plaintext = ""

  keyindex=0

  for i in range(len(ciphertext)):

    if ciphertext[i] in uppercase:
    
      findthenum= (uppercase[ciphertext[i]] - keyNumber[keyindex % len(key)]) % 26

      plaintextletter = inv_uppercase[findthenum]
      plaintext += plaintextletter
      keyindex+=1
    elif ciphertext[i] in lowercase:
      findthenum= (lowercase[ciphertext[i]] - keyNumber[keyindex % len(key)]) % 26

      plaintextletter = inv_lowercase[findthenum]
      plaintext += plaintextletter
      keyindex+=1

    else: 
      plaintext += ciphertext[i]

  print()
  print()

  print("Plaintext that is decrypted with key", keyWord, "is:")
  print()
  print(plaintext)

ciphertext = "Fwg atax: P’tx oh li hvabawl jwgvmjs, nw fw tfiapqz lziym, rqgv uuwfpxj wpbk jxlnlz fptf noqe wgw. Qoifmowl P bdg mg xv qe ntlyk ba bnjh vcf ekghn izl fq blidb eayz jgzbwx sqwm lgglbtqgy xlip. Pho fvvs ktf C smf ur ecul ywndxlz uv mzcz xxivw? Qomdmowl P bgzg, oblzqdxj C swas, B kyl btm udujs dcbfm vn yg eazl, pqzx, oblzq Q’ow mwmzb lg ghvk gxslz, emamwx apqu, wwmazagxv nomy bhlustk. Ghm qvv’f nbfx h vqe vgoubdg, pgh’a nuvw shvbtmk kbvzq. Baam jqfg pafs ixetqm wcdanw svc. Kwn’df dixs mzy ziym llllmfa, zjid wxl bf nom eifw hlqspuglowall, loyv sztq cu btmlw mhuq phmmla. Kwn’df htiirk yul gx bf noqe kbls. Kwz’b agjl naz mzcuoe mekydpqzx: lblzq’a gg moqb nhj svc, fpxjy’z va zhsx. Uwi basn fwg’dx ouzbql rgoy tunx zyym, uv mzcz ayied wvzzmk, qib’dq lxknywkmw an ldqzroblzq qg lbl eazev."
listOfLetters= stringToList(ciphertext)
PossibleKeyLength = shiftTheCiphertext(listOfLetters)
findTheKey(listOfLetters, PossibleKeyLength)
key= 'HIMITSU'
decrypt(ciphertext, key)