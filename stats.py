# class STATS:
#   def __init__(self):
#     self.text = text
  
def get_word_count(text):
  return len(text.split())

def get_char_count(text):
  char_count = {}
  text_array = text.split()
  for word in text_array:
    # word_array = word.split("")
    for letter in word:
      lower_case_letter = letter.lower()
      if lower_case_letter in char_count:
        char_count[lower_case_letter] += 1
      else:
        char_count[lower_case_letter] = 1
  return char_count

def sort_on(dict):
    return dict["num"]

def get_char_report(char_dict):
  sorted_char_array = []
  for key, value in char_dict.items():
    sorted_char_array.append({"char": key, "num": value})
  sorted_char_array.sort(reverse=True, key=sort_on)
  return sorted_char_array