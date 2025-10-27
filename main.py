import sys
from stats import count_words, count_char, sort_scribe

def get_book_text(filepath): 
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    book = get_book_text(relative_path)
    print("============BOOKBOT============")
    print(f"Analyzing book found at {relative_path}")
    print("---------- Word Count ---------")
    print(count_words(book))
    print("------- Character Count -------")
    for item in sort_scribe(count_char(book)):
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

if __name__ == "__main__":
    main()
