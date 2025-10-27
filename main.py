from stats import count_words, count_char

def get_book_text(filepath): 
    with open(filepath) as file:
        return file.read()

def main():
    relative_path = "books/frankenstein.txt"
    book = get_book_text(relative_path)
    print(count_words(book), count_char(book))

if __name__ == "__main__":
    main()
