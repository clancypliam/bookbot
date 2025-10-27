from stats import count_words, count_char, sort_scribe

def get_book_text(filepath): 
    with open(filepath) as file:
        return file.read()

def main():
    relative_path = "books/frankenstein.txt"
    book = get_book_text(relative_path)
    print("============BOOKBOT============")
    print("Analyzing book found at books/frankenstein.txt")
    print("---------- Word Count ---------")
    print(count_words(book))
    print("------- Character Count -------")
    for item in sort_scribe(count_char(book)):
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

if __name__ == "__main__":
    main()
