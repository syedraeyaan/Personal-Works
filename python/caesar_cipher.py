import string

letters = list(string.ascii_lowercase)

work = input("Type encode to encrypt the message / decode to decrypt the message: ").lower()

if work == "encode":

    def caesar_cipher_encrypt(original_text:str , offset:int): # Defines the parameters
        
        caesar_text = "" # Empty String to store the new alphabet
        
        for i in original_text:
            
            letter_index = letters.index(i)
            caesar_index = letter_index + offset
            
            caesar_text += letters[caesar_index] # Concatenation of the alphabets to build the caesar_text
        
        return caesar_text # Returns the encrypted string as the output

    message = input("Enter the message to encrypt: \n").lower()
    offset_input = int(input("Enter the offset number: \n"))

    print(f"Your original text: {message}")
    print(f"Encrypted Message: {caesar_cipher_encrypt(message, offset_input)}")

elif work == "decode":
    print("We are currently working on this feature !")

else:
    print("Invalid Input")