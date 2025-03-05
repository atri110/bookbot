import sys

from stats import (
    count_book_words,
    count_characters,
    get_book_text,
    sort_characters_count,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_content = get_book_text(sys.argv[1])
    if file_content:
        words_count = count_book_words(file_content)
        characters_count = count_characters(file_content)
        sorted = sort_characters_count(characters_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        for item in sorted:
            if not item.isalpha():
                continue
            print(f"{item}: {sorted[item]}")
        print("============= END ===============")


if __name__ == "__main__":
    main()
