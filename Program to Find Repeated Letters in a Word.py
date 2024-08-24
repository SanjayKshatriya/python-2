def find_repeated_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    repeated_letters = [letter for letter, count in letter_count.items() if count > 1]
    return len(repeated_letters), repeated_letters
input_word = input("Enter the word: ")
num_repeated, repeated = find_repeated_letters(input_word)
print("Number of repeated letters =", num_repeated)
if num_repeated > 0:
    print("Repeated letter =", ' '.join(repeated))
else:
    print("No repeated letters found.")
