def circular_replace(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    modified_string = []
    
    for char in s:
        freq = frequency[char]
        new_char = chr(((ord(char) - ord('a') + freq) % 26) + ord('a'))
        modified_string.append(new_char)

    return ''.join(modified_string)
input_string = "ghee"
output_string = circular_replace(input_string)
print("Output:", output_string)
