import re

def sort_list(my_list):
  def get_number(item):
    match = re.search(r'\d+', item)
    return int(match.group()) if match else 0

  return sorted(my_list, key=get_number)

def main():
    sort_list()
if  __name__ == '__main__':
    main()