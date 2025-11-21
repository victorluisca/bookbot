import sys

from stats import char_count_to_sorted_list, get_char_count, get_word_count


def get_book_contents(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def print_reports(book_path, word_count, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_sorted_list:
        if not dict["char"].isalpha():
            continue
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)
    char_count = get_char_count(book_contents)
    char_sorted_list = char_count_to_sorted_list(char_count)

    print_reports(book_path, word_count, char_sorted_list)


if __name__ == "__main__":
    main()
