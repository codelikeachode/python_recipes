def reverse(word):
    # Characters count
    char_count = len(word)
    
    i = char_count
    result = ""
    while i > 0:
        i = i - 1
        result += word[i]
        
    return result

stringReverse = reverse("string")
# stringReverse is "gnirts"

print(f"{stringReverse = }")