def boyer_moore_horspool(text, pattern):
    len_text = len(text)
    len_pattern = len(pattern)

    # Edge cases
    if len_pattern > len_text:
        return -1
    if len_pattern == 0:
        return 0 if len_text == 0 else -1

    # Bad Match Table
    bad_match_table = {}
    for i in range(len_pattern - 1):
        bad_match_table[pattern[i]] = len_pattern - i - 1

    i = len_pattern - 1  # start comparing from the end of the pattern
    while i < len_text:
        match = True
        for j in range(len_pattern):
            text_char = text[i - j]
            pattern_char = pattern[len_pattern - 1 - j]
            if text_char != pattern_char:
                match = False
                # shift by bad match table value or whole pattern length
                i += bad_match_table.get(text_char, len_pattern)
                break
        if match:
            return i - len_pattern + 1

    return -1


print(boyer_moore_horspool("Short and sweet", "sweet"))
