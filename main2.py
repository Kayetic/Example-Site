with open('data.txt') as original_file:
    data = original_file.read()

print(data)

with open('word_by_word.txt', 'w') as word_by_word_file:
    for word in data.split():
        word_by_word_file.write(word + '\n')
    word_by_word_file.close()
