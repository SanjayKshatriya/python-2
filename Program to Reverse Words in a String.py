def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
input_string = "the sky is blue"
output_string = reverse_words(input_string)
print("Output:", output_string)
