password = input("Enter your password: ")


length = len(password)
print("Length:", length)



has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False

for character in password: 
    if character.isupper():
        has_uppercase = True
    
    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_number = True

    if not character.isalnum():
        has_symbol = True
        
        
        
print("Has uppercase:", "YES!" if has_uppercase else "NO!")
print("Has lowercases: ", "YES!" if has_lowercase else "NO!")
print("Has number: ", "YES!" if has_number else "NO!")
print("Contains Symbol: ", "YES!" if has_symbol else "NO!")



if length >= 8 and has_uppercase and has_lowercase and has_number and has_symbol:
     print("Strength: Strong")

elif length >= 6 and has_uppercase and has_lowercase and has_number:
    print("Strength: Medium")
else:
    print("Strength: Weak")