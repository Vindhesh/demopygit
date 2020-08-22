import time
# Palindrome MY WAY
word = input("Enter your word: ")
word1 = list(word)
Pal = list(word)
print(f"You entered {Pal}")
Pal.reverse()
print(f"Reverse of the word is {Pal}")

if word1 == Pal:
    print("Hence \nYes, it is a palindrome")
else:
    print("Hence \nNO, it is not a palindrome")

time.sleep(3)