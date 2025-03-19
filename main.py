from stats import word_count, char_map, sorted_list_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------""")
        file_contents = f.read()
        n_words = word_count(file_contents)
        print(f"Found {n_words} total words")
        print("--------- Character Count -------")

        book_char_map = char_map(file_contents)
        # print(book_char_map)
        sorted_list = sorted_list_dicts(book_char_map)
        for char_dict in sorted_list:
            if char_dict['char'].isalpha():
                print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        get_book_text(book)

main()