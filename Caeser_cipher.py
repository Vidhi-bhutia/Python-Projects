alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  cipher_text=[]
  for i in text:
    if i == ' ':
      cipher_text += ' '
    else:
      current_index = alphabet.index(i)
      new_index = current_index + shift
      if new_index > 26:
        new_index-=25
        cipher_text += alphabet[new_index - 1]
      else:
        cipher_text += alphabet[new_index]
  print(''.join(cipher_text))

def decode(text, shift):
  decoded_test = []
  for i in text:
    if i == ' ':
      decoded_test += ' '
    else:
      current_index = alphabet.index(i)
      new_index = current_index - shift
      if new_index < 0:
        new_index+=25
        decoded_test += alphabet[new_index + 1]
      else:
        decoded_test += alphabet[new_index]
    
  print(''.join(decoded_test))

condition = True
while condition:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
  if direction.lower() == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
    
  elif direction.lower() == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decode(text, shift)
    
  else:
    print("Please enter a valid choice")
    quit()

  again = input("Do you want to run this again: 'yes' or 'no' ?").lower()
  if again == "yes":
    condition = True
  elif again == "no":
    condition == False
    break
  else:
    print("Invalid choice")
    condition == False
    break
      

# # Different approach    
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:

#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")


# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")
    


