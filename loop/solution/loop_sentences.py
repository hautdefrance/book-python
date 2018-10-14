TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'

SENTENCES = TEXT.split('.')

result = list()
total_words = 0
total_sentences = 0
total_chars = 0


for sentence in SENTENCES:
    sentence = sentence.strip()
    words_in_sentence = sentence.split(' ')
    word_count = len(words_in_sentence)

    # {key: value}
    # {sentence: word_count}
    result.append({sentence: word_count})

    total_words += word_count
    total_sentences += 1
    total_chars += len(sentence)


print(f'Result: {result}')
print(f'Total Words: {total_words}')
print(f'Total Sentences: {total_sentences}')
print(f'Total Characters: {total_chars}')
