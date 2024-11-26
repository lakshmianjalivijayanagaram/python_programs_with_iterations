word=input("enter a value")
if word==word[::-1]:
    print(f"{word} is a palindrome")
else:
    print("not a palindrome")
