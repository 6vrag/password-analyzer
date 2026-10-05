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

score = 0

if length >= 8:
    score += 1

if has_uppercase: 
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

print("Score: ", score)

if score == 5:
     print("Strength: Strong")

elif score >= 3:
    print("Strength: Medium")
else:
    print("Strength: Weak")

if length < 8 or not has_uppercase or not has_lowercase or not has_number or not has_symbol: 
    print("\nSuggestion: ")

    if length < 8: 
        print("- Use at least 8 Characters!")

    if not has_uppercase: 
     print("- Use Uppercase!")

    if not has_lowercase:
     print("- Use Lowercase!")

    if not has_number: 
        print("- Use Numbers!")

    if not has_symbol: 
        print("- Use Unique Symbols!")
