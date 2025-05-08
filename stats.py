def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def check_word_number(file_path):
    word_list = get_book_text(file_path).split()
    return len(word_list)

def get_num_letters(file_path):
    letter_nums = {}
    for l in get_book_text(file_path).lower():
        if l in letter_nums:
            letter_nums[l] += 1
        else:
            letter_nums[l] = 1
    return letter_nums

def list_sort(file_path):
    pass