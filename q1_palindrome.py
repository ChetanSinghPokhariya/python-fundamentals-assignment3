word=input("Enter the word: ")
rev=""
for i in word:
    rev=i+rev
if word==rev:
    print("Its a Palindrome!")
else:
    print("Not a Palindrome")


    

