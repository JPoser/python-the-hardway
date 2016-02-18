import ex25

sentence = "All good things come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_first_a_last_sorted(setnence)