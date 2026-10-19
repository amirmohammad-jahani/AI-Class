words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "you": "تو",
    "we": "ما",
    "they": "آنها",
    "book": "کتاب",
    "car": "ماشین"
}
sentence = "I love python and AI"

word_list = sentence.lower().split()

final_sentence = ""

for word in word_list:
    if word in words:
        final_sentence = final_sentence + words[word] + " "
    else:
        final_sentence = final_sentence + "[" + word + "] "

print(final_sentence)