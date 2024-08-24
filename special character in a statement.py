def count_special_characters(statement):
    special_characters = 0
    for char in statement:
        if not char.isalnum() and not char.isspace():
            special_characters += 1
    return special_characters
given_statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."
result = count_special_characters(given_statement)
print("Number of special Characters:", result)
