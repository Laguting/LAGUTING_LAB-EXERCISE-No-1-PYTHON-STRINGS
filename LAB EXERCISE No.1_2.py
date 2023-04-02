# Laguting, Maricon Jane G. 
# BSCpE 1-4

# Intro (Orange) an import pyfiglet module
import pyfiglet
in_tro = pyfiglet.figlet_format("Welcome!", font = "digital")
print("=" * 17)
print(in_tro.upper())
print("=" * 17)

# Accept an input from the user
user_input = input("\033[46m\033[27mHi, User! please enter any encrypted code you have in mind:\033[0m ")
print("=" * 17)

# Processing countdown
processing = "\033[33m\033[1mPlease wait, we're currently processing the encrypted code you entered.\033[0m"
print(processing)
print("=" * 17)

def countdown(n):
    if(n==0):
        print ("\33[45m\033[3mThank you for your patience\033[0m" + "\33[45m\033[3m!\033[0m")
    else: 
        print(n)
        countdown(n-1)
countdown(5)
print("." * 20)

# a, e, i, o, u assigned to *, &, #, +, ! respectively
t = ("*", "&", "#", "+", "!")
decrypted_input = ""

#Checking
# If *, change to "a"
for u in range (len(user_input)):
    if user_input[u] == t[0]:
        decrypted_input += "a"

# If &, change to "e"
    elif user_input[u] == t[1]:
        decrypted_input += "e"

# If #, change to "i"
    elif user_input[u] == t[2]:
        decrypted_input += "i"

# If +, change to "o"
    elif user_input[u] == t[3]:
        decrypted_input += "o"

# If !, change to "u"
    elif user_input[u] == t[4]:
        decrypted_input += "u"
    else:
        decrypted_input += user_input[u]

# Print the decrypted input of the user
print("\033[43m\033[1mThe encrypted code you entered a while a go is: \033[0m", decrypted_input)

# Outro
ou_tro = "\033[107mThank you for availing our services !\033[0m"
print("=" * 17)
print(ou_tro)
print("=" * 17)

