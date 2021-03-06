# -*- coding: utf-8 -*-
"""cs411_hw01_question5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N9xWTLm8wR0mVdG9gwEJbphpY5y0gVeT
"""

!apt-get install libenchant1c2a
!pip install --user pyenchant

import enchant #to decide if the decyrpted messages are in English or not
import math
import random
import fractions

d = enchant.Dict("en_US") #create English dictionary

alphabet = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 
            'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 
            'Z':25, ' ':26, '.':27, ',': 28, '!': 29, '?':30}

inv_alphabet = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z', 26:' ', 27:'.', 28:',', 29:'!', 30:'?'}

def phi(n):
    amount = 0
    possibleAlpha= [] #find the possible alpha values in the phi funvtion
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
          possibleAlpha.append(k)
          amount += 1
    return possibleAlpha

# The extended Euclidean algorithm (EEA)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Modular inverse algorithm that uses EEA
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def encode(triagram): #encode the triagram as stated in question 4

  encodedNum= alphabet[triagram[0]] * (31**2) + alphabet[triagram[1]] * 31 + alphabet[triagram[2]]

  return encodedNum

def findAlphaBetaPairs(plain, cipher): #for each alpha it finds the corresponding beta pair with known plaintext and its corresponding ciphertext

  possibleAlpha= phi(31**3)
  plainEncode = encode(plain)
  cipherEncode= encode(cipher)
  possibleBeta = []

  for alpha in possibleAlpha:
    beta = (cipherEncode - alpha * plainEncode)%(31**3)
    possibleBeta.append(beta)
  
  alpha_beta_tuple = list(zip(possibleAlpha,possibleBeta))
  return alpha_beta_tuple

ciphertext = "IDSEOYLTVVDO?PSAUEKZO?LQIILQMP?LQNP!YSFNGSDBJZRZYTZTPS?EVYF,?LQ ,SAXSWTFXFD" 

plain_lastthree= ".XX" 
cipher_lastthree= "XFD"
alpha_beta_pairs= findAlphaBetaPairs(plain_lastthree, cipher_lastthree)

def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    i=0
    while i<=plen-2:
        l1= ptext[i]
        l2= ptext[i+1]
        l3= ptext[i+2]
        toencode = l1+l2+l3 #triagram
        encoded = encode(toencode) #encode the ciphertext triagrams 

        poz = (key.gamma*encoded+key.theta)%(31**3) 

        poz_1 = poz%31 #find the last letter's encoding in alphabet
        poz_2 = ((poz-poz_1) % (31**2))//31 #find the second letter's encoding in alphabet
        poz_3 = ((poz-poz_1-poz_2)%(31**3))//(31**2) #find the first letter's encoding in the alphabet

        ctext += inv_alphabet[poz_3] 
        ctext += inv_alphabet[poz_2] 
        ctext += inv_alphabet[poz_1] #create the ciphertext
        i=i+3
    return ctext


# key object for Affine cipher
# (alpha, beta) is the encryption key
# (gamma, theta) is the decryption key
class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0


for pairs in range(len(alpha_beta_pairs)): #for each alpha beta pair we find a new decyrpted text using the keys
  key.alpha = alpha_beta_pairs[pairs][0]
  key.beta = alpha_beta_pairs[pairs][1]
  key.gamma = modinv(key.alpha, (31**3)) # you can compute decryption key from encryption key
  key.theta = (31**3) - (key.gamma * key.beta) % (31**3) #since it's mod 31**3 I've changed these parts

  dtext = Affine_Dec(ciphertext, key)
  
  #after decyrpting the ciphertext I put all the words in a list so that we can check if each word is English or not

  split_sentence_tolist = []
  new_word= ""
  new_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for char in dtext:
    if char in new_alphabet:
      new_word+=char
    else:
      split_sentence_tolist.append(new_word)
      new_word=""
  split_sentence_tolist.append(new_word)

  flag = True

  for word in split_sentence_tolist: #for each word in decrypted message
    if len(word)>0:
      if d.check(word) == False: #if any word is not English then check function will give False and we will stop checking them
        flag=False
        break

  if flag== True: #if all the words in the decyrpted message is English then this would be our plaintext

    print("Keys used for encryption is alpha =", key.alpha, "and beta =", key.beta)
    print("Keys used for decryption is gamma =", key.gamma, "and theta =", key.theta)
    print("plaintext: ", dtext)