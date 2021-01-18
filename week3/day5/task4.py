def words(word):
    up_count = 0
    low_count = 0
    for letter in word:
        if letter.isupper():
            up_count += 1
        elif letter.islower():
            low_count += 1

    if up_count > low_count:
        word = word.upper()
    else:
        word = word.lower()
    print(word)
words(input())
