import random
import string

def generate_password(min_len, numbers = True, special_chars = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters

    if numbers:
        chars += digits
    if special_chars:
        chars += special
    
    pwd = ""
    meets_criteria = False
    has_nums = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(chars)

        pwd += new_char

        if new_char in digits:
            has_nums = True
        elif new_char in special:
            has_special = True
        

        meets_criteria = True
        if numbers:
            meets_criteria = has_nums
        if special_chars:
            meets_criteria = meets_criteria and has_special
        
    return pwd

min_length = int(input("Enter minimum length of the password: "))
has_nums = input("Do you want to include numbers? (y/n)").lower() == "y"
has_special = input("Do you want to include special characters? (y/n)").lower() == "y"

print(generate_password(min_length, has_nums, has_special))