from stats import get_num_words, character_count, sort_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    inputs = sys.argv
    if len(inputs) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = inputs[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    book_text = get_book_text(file_path)
    get_num_words(book_text)
    character_list = character_count(book_text)
    sort_list(character_list)
    print("============= END ===============")
    





main()