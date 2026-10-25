def matching_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print(f"The words are {lst}")
    return ctr 

count = matching_words(['abc', 'cyc', 'xyz', 'aba', '1221'])    
print("Number of words having first and last character same", count)