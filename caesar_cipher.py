alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word=str()
def encrypt(word):
    for i in text:
        index = alphabet.index(i)+shift  
        
        if index > 25:
            #index=index-26                 #u can try different logic by using modulo (index % len(alphabet))        
            index=index%len(alphabet)       # so basically it will bring the letter to the start
            word = word + alphabet[index]
        else:
            word = word + alphabet[index]
    print(word)
def decrypt(word):
    for i in text:
        index = alphabet.index(i)-shift  
        index=index % len(alphabet)
        if index <0:
             index=index+26
             word = word + alphabet[index]
        else:
            word = word + alphabet[index]
    print(word)
a='y'
while a=='y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=="encode":
        encrypt(word)
    else:
        decrypt(word)
    a=str(input("do u want to continue:(y/n)"))