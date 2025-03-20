def word_count(str):
    words = str.split()
    return len(words)

def char_map(str):
    out = {}
    for c in str:
        lower_c = c.lower()
        if lower_c.isalpha():
            out[lower_c] = out.setdefault(lower_c, 0) + 1
    return out

def sort_on(tup):
    return tup[1]

def sorted_list_dicts(char_map:dict):
    items = char_map.items()
    return sorted(items, key=sort_on, reverse=True)