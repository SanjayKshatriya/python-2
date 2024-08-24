def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in statement:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
given_statement = "Saveetha School of Engineering Sample"
vowels, consonants = count_vowels_and_consonants(given_statement)
if vowels > consonants:
    max_type = "vowels"
    max_count = vowels
else:
    max_type = "consonants"
    max_count = consonants
print("Number of vowels =", vowels)
print("Number of consonants =", consonants)
print("Maximum is:", max_type, "with count =", max_count)
