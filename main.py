def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_num_words(text)
    char = get_num_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words found in the document: {count}")
    sort_char(char)
    print("--- End report ---")
    

def sort_on(dict):
    return dict[1]

def sort_char(char_list):
    sorted_list = sorted(char_list.items(), reverse=True, key=sort_on)
    for letter in sorted_list:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")
        else: 
            pass

def get_num_characters(text):
    alpha = {}
    string = text.lower()
    for letters in string:
        if letters in alpha:
            alpha[letters] += 1
        else:
            alpha[letters] = 1
    return alpha
        

def get_num_words(text):
    words = text.split()
    return len(words)
        

def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()