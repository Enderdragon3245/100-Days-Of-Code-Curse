#Functions 
import math

def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice today?")

greet()

#Functions that allows for input

def greet_with_name(name):
    print(f"How wo doin {name}?")

greet_with_name("gustavo")

def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}")

greet_with("Gustavo", "Russas") #Position Argument = Default
greet_with(name="Gustavo", location="Russas") #Keyword Arguments

#Challenge 1 Calculating the area of ​​a wall


def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  
  print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Challenge 2 - Its a Prime Number?

def prime_checker(number):
  in_prime = True
  for i in range(2, number):
    if number % i == 0:
      in_prime = False


  if in_prime == True:
    print("It's a prime number.")
  if in_prime == False:
    print("It's not a prime number.")

#Challenge Caeser Cipher ------------------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_test, shift_amount):
        cipher_text = ""
        for letter in plain_test:
            
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        
        print(f"the encoded text is {cipher_text}")

    encrypt(plain_test=text, shift_amount=shift)

elif direction == "decode":
    decode_text = input("Type your encode message:\n".lower())
    shift = int(input("Type the shift number:\n"))

    def decrypt(decoded_test, shift_amount):
        cipher_text = ""

        for letter in decoded_test:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        
        print(f"the decody text is {cipher_text}")

    decrypt(decoded_test=decode_text, shift_amount=shift)

else:
    print("Type one of two conditions")