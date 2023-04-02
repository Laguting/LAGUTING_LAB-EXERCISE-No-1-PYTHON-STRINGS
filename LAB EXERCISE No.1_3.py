# Maricon Jane G. Laguting
# BSCpE 1-4

# Intro
import pyfiglet
in_tro = pyfiglet.figlet_format("THE VIGENERE CIPHER".center(70," "), font = "digital")
print("\33[1m_" * 100)
print("\n", in_tro)
print("\33[1m_" * 100)

welcome = pyfiglet.figlet_format("Hi!", font = "doh")
print("\n", welcome)
print("\33[1m_" * 62)

# Start the program
start = input("\33[1m\33[33mDo you want to start the program?\U0001F481 \n Enter Y if 'Yes' and N if 'No': \33[0m")
if start == "Y":
    print("\n\033[96m\33[4mThe Program is Starting...\033[0m")
elif start == "N":
    quit
else:
    quit
def countdown(n):
    if(n==0):
        print ("\33[45m\033[3mThank you for your patience\033[0m" + "\33[45m\033[3m!\033[0m")
    else: 
        print(n)
        countdown(n-1)
countdown(5)

# Get the users message and key
instruction = ("\33[102mEnter the Message and Key you have in mind below\U0001F53D \033[0m")
print("\33[1m-+" * 62)
print(instruction)
message_input = input("\n\33[104mMessage\U0001F4AC: \33[0m")
message_input = message_input.upper()
key_input = input("\n\33[105mKey\U0001F511: \33[0m")
key_input = key_input.upper()

# Check the equivalent numbers of the letters inputted (Message & Key)
message_input = [ord(char) - 65 for char in message_input if char.isalpha()]
key_input = [ord(char) - 65 for char in key_input]

# Add the equivalent numbers of the letters inputted (Message & Key)
ciphered_txt = []
for i, val in enumerate(message_input):
    key_val = key_input[i % len(key_input)]
    ciphered_val = (val + key_val) % 26
    ciphered_txt.append(ciphered_val)

# Get the equivalent letters of the sum extracted from the Message & Key
ciphered_txt = ''.join([chr(val + 65) for val in ciphered_txt])

# Print the Ciphertext
print("\33[1m-+" * 62)
print("\n\n\33[43m\33[41mThe result is: \33[0m", ciphered_txt)

# Outro
ou_tro = pyfiglet.figlet_format("Thank you for availing our service!", font = "bubble")
print(ou_tro)
closing = "\n\033[96m\33[4mClosing...\033[0m\n\n"
print(closing)