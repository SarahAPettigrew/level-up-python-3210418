def sort_string(string):
  string = string.split(' ')
  list = sorted(string, key=str.casefold)
  final_string = ' '.join(list)

  return final_string


print(sort_string('sort these words alphabetically'))