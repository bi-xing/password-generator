import string
import secrets

#planned features:
# add the option to save the password to a text file
# provide the option to encode the password in base64, hex, binary, XOR, etc, when it is saved to the text file
# add the option to generate multiple passwords at once and save all of them in a shared text file

def passlength():
    while True:
        try:
            passwordchars=int(input("Length of Password: "))
            if passwordchars<4:
                print("Length must be at least 4 characters.  (•̀⤙•́ )")
                continue
            else:
                return passwordchars
        except ValueError:
            print("Error, please enter a number!")
        
def password_generator(length):
    passwordarr=[
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    while len(passwordarr)<length:
        passwordarr.append(secrets.choice(string.ascii_letters+string.digits+string.punctuation))
    secrets.SystemRandom().shuffle(passwordarr)
    return ''.join(passwordarr)

def redo_instance(currentpass):
    asciiart=r"""
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡛⣿⣿⣿⣯⢻
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⢟⣻⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣧
        ⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣆⠻⡫⣢⠿⣿⣿⣿⣿⣿⣿⣿⣷⣜⢻⣿
        ⣿⣿⡏⣿⣿⣨⣝⠿⣿⣿⣿⣿⣿⢕⠸⣛⣩⣥⣄⣩⢝⣛⡿⠿⣿⣿⣆⢝
        ⣿⣿⢡⣸⣿⣏⣿⣿⣶⣯⣙⠫⢺⣿⣷⡈⣿⣿⣿⣿⡿⠿⢿⣟⣒⣋⣙⠊
        ⣿⡏⡿⣛⣍⢿⣮⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⢱⣾⣿⣿⣿⣝⡮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣋⣻⣿⣿⣿⣿
        ⢿⢸⣿⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⡕⣡⣴⣶⣿⣿⣿⡟⣿⣿⣿
        ⣦⡸⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿
        ⢛⠷⡹⣿⠋⣉⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣷⢹⣿⣿
        ⣷⡝⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⣠⣤⣤⣦⣽⣿⣿⣿⡿⠋⠘⣿⣿
        ⣿⣿⡹⣿⡼⣿⣿⣿⣿⣿⣿⣿⣧⡰⣿⣿⣿⣿⣿⣹⡿⠟⠉⡀⠄⠄⢿⣿
        ⣿⣿⣿⣽⣿⣼⣛⠿⠿⣿⣿⣿⣿⣿⣯⣿⠿⢟⣻⡽⢚⣤⡞⠄⠄⠄⢸⣿    """
    print(asciiart)
    print("\nThanks for using this instance of the generator!\n")
    print(f"Your generated password was: {currentpass}\n")
    print("Would you like to generate another password? (y/n)\n")
    while True:
        redo=input("Input: ").lower()
        if redo=="y":
            function()
            break
        elif redo=="n":
            print(r"""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠒⠢⢄⡀⠀⠀⢠⡏⠉⠉⠉⠑⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠙⢦⠀⡇⡇⠀⠀⠀⠀⠀⠀⠈⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠉⠉⠙⠒⢤⡀⠀⣼⠀⠀⢀⣶⣤⠀⠀⠀⢣⡇⡇⠀⠀⢴⣶⣦⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢀⣠⠤⢄⠀⠀⢰⡇⠀⠀⣠⣀⠀⠀⠈⢦⡿⡀⠀⠈⡟⣟⡇⠀⠀⢸⡇⡆⠀⠀⡼⢻⣠⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⢀⠖⠉⠀⠀⠀⣱⡀⡞⡇⠀⠀⣿⣿⢣⠀⠀⠈⣧⣣⠀⠀⠉⠋⠀⠀⠀⣸⡇⠇⠀⠀⠈⠉⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣠⠏⠀⠀⣴⢴⣿⣿⠗⢷⡹⡀⠀⠘⠾⠾⠀⠀⠀⣿⣿⣧⡀⠀⠀⠀⢀⣴⠇⣇⣆⣀⢀⣀⣀⣀⣀⣤⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⣿⠀⠀⢸⢻⡞⠋⠀⠀⠀⢿⣷⣄⠀⠀⠀⠀⠀⣠⡇⠙⢿⣽⣷⣶⣶⣿⠋⢰⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⡿⡄⠀⠈⢻⣝⣶⣶⠀⠀⠀⣿⣿⣱⣶⣶⣶⣾⡟⠀⠀⠀⢈⡉⠉⢩⡖⠒⠈⠉⡏⡴⡏⠉⠉⠉⠉⠉⠉⠉⠉⡇⠀⠀⢀⣴⠒⠢⠤⣀
                ⢣⣸⣆⡀⠀⠈⠉⠁⠀⠀⣠⣷⠈⠙⠛⠛⠛⠉⢀⣴⡊⠉⠁⠈⢢⣿⠀⠀⠀⢸⠡⠀⠁⠀⠀⠀⣠⣀⣀⣀⣀⡇⠀⢰⢁⡇⠀⠀⠀⢠
                ⠀⠻⣿⣟⢦⣤⡤⣤⣴⣾⡿⢃⡠⠔⠒⠉⠛⠢⣾⢿⣿⣦⡀⠀⠀⠉⠀⠀⢀⡇⢸⠀⠀⠀⠀⠀⠿⠿⠿⣿⡟⠀⢀⠇⢸⠀⠀⠀⠀⠘
                ⠀⠀⠈⠙⠛⠿⠿⠿⠛⠋⢰⡋⠀⠀⢠⣤⡄⠀⠈⡆⠙⢿⣿⣦⣀⠀⠀⠀⣜⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⡸⠀⠇⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢣⠀⠀⠈⠛⠁⠀⢴⠥⡀⠀⠙⢿⡿⡆⠀⠀⢸⠀⢸⢰⠀⠀⠀⢀⣿⣶⣶⡾⠀⢀⠇⣸⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⢇⠀⠀⠀⢀⡀⠀⠀⠈⢢⠀⠀⢃⢱⠀⠀⠀⡇⢸⢸⠀⠀⠀⠈⠉⠉⠉⢱⠀⠼⣾⣿⣿⣷⣦⠴⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠘⡄⠀⠀⢹⣿⡇⠀⠀⠈⡆⠀⢸⠈⡇⢀⣀⣵⢨⣸⣦⣤⣤⣄⣀⣀⣀⡞⠀⣠⡞⠉⠈⠉⢣⡀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠘⡄⠀⠀⠉⠀⠀⣠⣾⠁⠀⠀⣧⣿⣿⡿⠃⠸⠿⣿⣿⣿⣿⣿⣿⠟⠁⣼⣾⠀⠀⠀⠀⢠⠇⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠹⣀⣀⣤⣶⣿⡿⠃⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⢻⣿⣷⣦⣤⣤⠎⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣤⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀""")
            print("\n")
            exit()

def function():
    length=passlength()
    password=password_generator(length)
    print(f"Password: {password}\n")
    redo_instance(password)

def main():
    print("🔑 ▼ PASSWORD GENERATOR PROGRAM ▼ 🔑\n")
    print("-"*50)
    print("\nHey user! Welcome to the password generator ♥\n")
    print("This program will scramble letters, numbers, and other characters to create a password.\n")
    function()
main()