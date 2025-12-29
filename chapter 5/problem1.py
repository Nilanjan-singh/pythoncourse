hindi={
    "Namste":"Hello",
    "Dhanyavad":"Thanks",
    "Ashirvad":"Blessings",
    "dost":"freind"
}
word=input("Enter the Hindi word to translate :")
print("english meaning:", hindi.get(word, "word not found"))