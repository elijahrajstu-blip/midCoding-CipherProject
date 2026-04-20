choice = input("encode or decode?")
if choice == "encode":
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""

    for char in message:
        if char.isalpha():
            start = ord(char)
            new_char = chr(start + shift)
            encoded += new_char
        else:
            encoded += char

    print("Encoded message:", encoded)
else:
    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))
    encoded = ""

    for char in message:
        if char.isalpha():
            start = ord(char)            
            shiftValue = start - shift
            new_char = chr(shiftValue)
            encoded += new_char
        else:
        
            encoded += char

    print("Decoded message:", encoded)