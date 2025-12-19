alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word=str()
def caeser(word,j):
    for i in text:
        index = alphabet.index(i)+int((shift*j))
        if index > 25:
            index=index-26                
            word = word + alphabet[index]
        elif index <0:
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
        caeser(word,1)
    else:
        caeser(word,-1)
    a=str(input("do u want to continue:(y/n)"))