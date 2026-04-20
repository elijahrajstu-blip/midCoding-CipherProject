message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))
encoded = ""

for char in message:
    if char.isalpha():
       
        start = ord('A') if char.isupper() else ord('a')
        
        shiftValue = start - shift
        new_char = chr(shiftValue)
        encoded += new_char
    else:
       
        encoded += char

print("Encoded message:", encoded)