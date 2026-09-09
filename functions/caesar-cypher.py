"""Original Solution
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount


def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()
"""

# More pythonic version
import string

ALPHABET = string.ascii_uppercase


def get_message() -> str:
    return input("Please enter a message to encrypt: ")


def get_cipher_key() -> int:
    return int(input("Please enter a key (whole number from 1-25): "))


def encrypt_message(message, shift, alphabet) -> str:
    encrypted = []

    for char in message.upper():
        if char in alphabet:
            new_pos = (alphabet.index(char) + shift) % 26
            encrypted.append(alphabet[new_pos])
        else:
            encrypted.append(char)

    return "".join(encrypted)


def main():
    message = get_message()
    key = get_cipher_key()
    encrypted = encrypt_message(message, key, ALPHABET)
    print(f"Encrypted Message: {encrypted}")


if __name__ == "__main__":
    main()