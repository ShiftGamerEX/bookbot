def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
        characters = {}
        for c in text:
            lowered = c.lower()
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
        return characters


def sort_on(d):
    return d["num"]


def  chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list