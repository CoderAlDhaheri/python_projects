import random, string
password_length = int(input("how long do you want the password: "))

password_character = string.digits + string.ascii_letters +string.punctuation

password = []
for x in range(password_length):
    password.append(random.choice(password_character))
print(''.join(password))

print("""                           
        --------------------------------------------------------""")
answer = input("""
                    keep playing!!
                  hit enter to replay
                 or tipe exit to exit :
""")


while answer == "":
    password_length = int(input("how long do you want the password: "))

    password_character = string.digits + string.ascii_letters +string.punctuation

    password = []
    for x in range(password_length):
        password.append(random.choice(password_character))
    print(''.join(password))
    print("""                           
        --------------------------------------------------------""")
    answer = input("""
                    keep playing!!
                  hit enter to replay
                 or tipe exit to exit :
""")