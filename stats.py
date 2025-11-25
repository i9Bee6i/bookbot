def get_num_words(text):
    """Return total number of words in the text."""
    words = text.split()
    return len(words)


def get_chars_dict(text):
    """Return a dictionary of every character (lowercased) and its count."""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict_item):
    """Helper function for sorting — returns the 'num' value."""
    return dict_item["num"]


def chars_dict_to_sorted_list(char_counts):
    """
    Convert the char_counts dictionary into a sorted list of dictionaries.
    Skip non-alphabetical characters.
    Sort by count descending (highest first).
    """
    chars_list = []

    # convert to list of dicts
    for ch, num in char_counts.items():
        if ch.isalpha():  # skip spaces, punctuation, etc.
            chars_list.append({"char": ch, "num": num})

    # sort list in place (highest count first)
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
