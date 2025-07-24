#write a program to create a dictonary of hindi words with values as their english transition.Provide user an option to look it up
words = {
    "namaskar":"hello",
    "kya kar rahe ho":"what are you doing",
    "kaise ho ap":"how are you"
}
word = input("enter a word you want meaning of: ")
print(words[word])