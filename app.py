def permutation(pattern, text):
    patterns = ''.join(sorted(pattern))
    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        sorted_substr = ''.join(sorted(text[i:i+pattern_len]))
        if sorted_substr == patterns:
            return "YES"

    return "NO"

data = [
    ('hack', 'indiahacks'),
    ('code', 'eddy'),
    ('coder', 'iamredoc'),
]

for pattern, text in data:
    result = permutation(pattern, text)
    print(result)