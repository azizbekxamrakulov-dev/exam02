def find_longest_name(names):
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest


print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
print(find_longest_name(['Bo', 'Ali', 'Zara']))