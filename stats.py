def word_count(str):
    words = str.split()
    return len(words)

def char_map(str):
    out = {}
    for c in str:
        lower_c = c.lower()
        if lower_c in out:
            out[lower_c] += 1
        else:
            out[lower_c] = 1
    return out

def sort_on(dict):
    return dict["count"]

def sorted_list_dicts(char_map):
    out = []
    for c in char_map:
        out.append({"char": c, "count": char_map[c]})
    out.sort(reverse=True, key=sort_on)
    return out