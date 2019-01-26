TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'

result = dict()
total_words = 0
total_sentences = 0
total_chars = 0
total_adjectives = 0


for sentence in TEXT.split('.'):
    sentence = sentence.strip()
    words_in_sentence = sentence.split(' ')
    word_count = len(words_in_sentence)

    result[sentence] = word_count
    total_words += word_count
    total_sentences += 1
    total_chars += len(sentence)

    for word in words_in_sentence:
        if word.endswith('ly'):
            total_adjectives += 1


print(f'Result: {result}')
print(f'Total Words: {total_words}')
print(f'Total Sentences: {total_sentences}')
print(f'Total Characters: {total_chars}')
print(f'Total Adjectives: {total_adjectives}')
