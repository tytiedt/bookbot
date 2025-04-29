import sys
from stats import get_word_count, get_char_count, get_char_report

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  relative_file_path = sys.argv[1]
  book = get_book_text(relative_file_path)
  word_count = get_word_count(book)
  char_count = get_char_count(book)
  char_report = get_char_report(char_count)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {relative_file_path[2:]}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char in char_report:
    if char["char"].isalpha():
      print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")
main()