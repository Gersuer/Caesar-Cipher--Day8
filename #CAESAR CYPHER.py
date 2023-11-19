#CAESAR CYPHER
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x',
  'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x',
  'y', 'z'
]
index = []

def encrypt(message, shift):    
  caesar_message = ''
  for letter in message:
   position = alphabet.index(letter)
   new_position = position + shift
   new_letter = alphabet[new_position]
   caesar_message +=new_letter
  print(f'A mensagem a ser decifrada será: {caesar_message}')

def decode(message,shift):
  decipher_message = ''
  for letter in message:
    positon = alphabet.index(letter)
    new_position = positon - shift
    new_letter = alphabet[new_position]
    decipher_message += new_letter
  print(f"A tradução da sua mensagem é: {decipher_message}")  

while True:
  direction = input("What you want to do? Encode or Decode:\n").lower()
  message = input("What is your message?\n").lower()
  shift = int(input("Type the shift number: "))

  if direction != 'encode' and direction != 'decode' or shift == '' or message == '':
    print('Type encode or decode and type how many shifts and your message')
  if direction == 'encode':
    encrypt(message, shift)
  if direction == 'decode':
    decode(message, shift)    
  while True:
    get_out = input('Do you want to exit? Y/N:\n').lower()
    if get_out != 'y' and get_out != 'n':
      print("Type Y or N")
    if get_out == 'y' or 'n':
      break
  if get_out == 'y':
    print("Thank you for used our app")
    break

  
#Doing the same thing with one function

def casear_cipher(message, shift, direction):
  if direction == 'decode':
      shift *= -1
  initial_message = ''
  for letter in message:
    position = alphabet.index(letter)
    new_position = position + shift
    new_letter = alphabet[new_position]
    initial_message += new_letter
  print(f"The {direction} is {initial_message}")

while True:
  direction = input("What you want to do? Encode or Decode:\n").lower()
  message = input("What is your message?\n").lower()
  shift = int(input("Type the shift number: "))
  if direction == '' or (direction != 'decode' and direction != 'encode') or shift == '':
    print("Type if you want to decode or endode your message, your message and how many shifts you want.")
  else:
    casear_cipher(message, shift, direction)
  while True:
    go_out = input("Do you want to exit? Y/N \n").lower()
    if go_out != 'y' and go_out!='n':
      print("Please respond the answer with Y or N")
    if go_out == 'y' or go_out == 'n':
      break
  if go_out == 'y':
    print("Thanks for used our app.")
    break 