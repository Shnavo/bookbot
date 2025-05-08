import stats
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# print(stats.list_sort("./books/frankenstein.txt"))
def main(file_path):
    # print(list_sort(file_path))
    print("============ BOOKBOT ============ \n"
          "Analyzing book found at books/frankenstein.txt... \n"
          "----------- Word Count ---------- \n"
          f"Found {stats.get_num_words(file_path)} total words \n"
          "--------- Character Count -------")
    for dict in stats.list_sort(file_path):
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main(sys.argv[1])