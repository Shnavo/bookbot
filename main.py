from stats import get_num_letters

def main(file_path):
    print(get_num_letters(file_path), "words found in the document" )

main("./books/frankenstein.txt")