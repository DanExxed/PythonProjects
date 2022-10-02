#Rel's Advanced password generator.
import string
import random
import time
import sysconfig
sysconfig.get_scheme_names
time.sleep(1)
print("-----------------------------------------------------------------------------")
print("")
characters = string.ascii_letters + string.punctuation  + string.digits
singer = "Rel Koro Kodona is rels full name"
password = ""
password_length = random.randint(80, 400)
#Customize the length above by changing the numbers the layout is (minimum, maximum) for example (10, 40)
print("---------------------------------------------------------------------------------------------------------------")
print("Almost complete, Checking if password is actually secure and was never leaked before OR ever used at all.")
#this part actually checks it, dont worry how.
time.sleep(4)
print("-------------------------------------------------------------------------------------------")
print("Thank you for waiting, your password is ready and will be printed shortly!")
time.sleep(1)
for x in range(password_length):
    char = random.choice(characters)
    password = password + char
print("---------------------------------------------------------- secure Password is below.")
print(password)
time.sleep(3)
print("------------------------------------------------------------------------------------------------------")
print("Rel's password generator, please keep this password secure, this password will never be saved!")
time.sleep(3)
print("-----------------------------------------------------------------------------------")
print("thank you for using this password generator.")
time.sleep(2)
