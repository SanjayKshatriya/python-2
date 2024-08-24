def count_sentences_starting_with_b(text):
    lines = text.strip().split('\n')
    
    total_lines = len(lines)
    b_count = 0

    for line in lines:
        if line.strip().startswith('B'):
            b_count += 1
            
    return total_lines, b_count
input_text = '''The apple doesn't fall. 
All that glitters are not gold. 
A picture is worth a thousand words. 
Beggers can't be choosers. 
A bird in the hand. 
Better safe than sorry. 
An apple a day keeps doctor away. 
Blood is thicker than water.'''
total_lines, b_sentences = count_sentences_starting_with_b(input_text)
print("Total number of lines:", total_lines)
print("Number of Sentences that start with letter B:", b_sentences)
