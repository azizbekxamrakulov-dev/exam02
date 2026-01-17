text = input("Matn ichidagi har bir so'z necha marta qatnashganini aniqlang: ")
text = input("Katta-kichik harfni e'tiborga olmang: ")
def count_words(text):
    text = text.lower()
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count
count_words("salom salom dunyo")
# {"salom": 2, "dunyo": 1}
print(count_words("salom salom dunyo"))

count_words("Python python PYTHON") 
# {"python": 3}
print(count_words("Python python PYTHON"))