import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # --- Argument check ---
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2nd argument is the book path
    book_path = sys.argv[1]

    # --- Analyze the book ---
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)

    # --- Print report ---
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
