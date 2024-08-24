def count_matching_characters(s1, s2):
    if len(s1) != len(s2):
        return "Strings must be of the same length."
    
    match_count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            match_count += 1
            
    return match_count
S1 = "what"
S2 = "watch"
result = count_matching_characters(S1, S2)
print(result)
