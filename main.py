def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def check_word_number(file_path):
    word_list = get_book_text(file_path).split()
    return len(word_list)

def main(file_path):
    print(check_word_number(file_path), "words found in the document" )

main("./books/frankenstein.txt")