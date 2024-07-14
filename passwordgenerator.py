import random
import string
def generationofpassword(length,):
    characters = string.ascii_lowercase
    characters = characters + string.ascii_uppercase
    characters = characters + string.digits  
    characters = characters + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    password = generationofpassword(length)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()