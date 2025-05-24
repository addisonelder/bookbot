import sys
from stats import get_word_count, get_char_counts, get_char_dicts, sort_dict_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    string = get_book_text(book)
    count = get_word_count(string)
    chars = get_char_counts(string)
    dict = get_char_dicts(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    print("----------- Word Count ----------")
    print(f"Found {count} total words")

    print("--------- Character Count -------")

    for entry in dict:
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")

main()    
