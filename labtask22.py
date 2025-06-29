name= "ZAHRA TUL HUSSAN SYED"
rollno= "23108195"
result = name + " " + rollno
print(result)
vowels = ('a', 'e', 'i', 'o', 'u')
def piglatinconverter(t):
    word = t.split()
    piglatinwords = []
    for word in word:
        if word[0] in vowels:
            pig_latin_word = word + 'hay'
        else:
            pig_latin_word = word[1:] + word[0] + 'ay'
        piglatinwords.append(pig_latin_word)
    return ' '.join(piglatinwords)
if __name__ == "__main__":
    i = input("enter the word or sentence: ")
    piglatintext = piglatinconverter(i)
    print("Pig Latin version:", piglatintext)


