def find_character_in_string(string, char_to_find):
    for index in range(len(string)):
        if string[index] == char_to_find:
            return index 
    return -1  
input_string = input("Enter the string: ")
character_to_find = input("Enter the character to be searched: ")
index = find_character_in_string(input_string, character_to_find)
if index != -1:
    print(f"{character_to_find} is found in string at index: {index}")
else:
    print(f"{character_to_find} is not found in the string.")
