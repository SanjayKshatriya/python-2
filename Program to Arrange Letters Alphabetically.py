def arrange_letters(word):
    sorted_normal = sorted(word)
    sorted_reverse = sorted(word, reverse=True)
    normal_order = ' '.join(sorted_normal)
    reverse_order = ' '.join(sorted_reverse)
    
    return normal_order, reverse_order
input_word = input("Enter the word: ")
normal_order, reverse_order = arrange_letters(input_word)
print("Alphabetical Order Normal:", normal_order)
print("Alphabetical Order Reverse:", reverse_order)
