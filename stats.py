def get_word_count(text: str):
    word_list = text.split()
    word_count = len(word_list)
    return word_count


def get_char_count(text: str):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def char_count_to_sorted_list(dict: dict[str, int]):
    char_count = []
    for key, value in dict.items():
        new_dict = {"char": key, "num": value}
        char_count.append(new_dict)
    char_count.sort(reverse=True, key=sort_on)
    return char_count
