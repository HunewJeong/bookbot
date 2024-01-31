def count_letters(content):
    content_lower = content.lower()
    letter_count_dict ={}
    for letter in content_lower:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1

    return letter_count_dict

def list_organizer(content):
    letter_count_dict = count_letters(content)
    letter_count_lst = []
    for key, value in letter_count_dict.items():
        if key.isalpha():
            letter_count_lst.append((key,value))
    letter_count_lst.sort(key=lambda pair: pair[1], reverse = True)
    
    for pair in letter_count_lst:
        print(f"The '{pair[0]}' character was found '{pair[1]}' times")
    
    return letter_count_lst


    
    print(letter_count_tupl)
    #for i in range(0, len(letter_count_list)):
    #    print(f"The '{letter_count_list[i]}' character was found {} times")

def main():
    with open('books/frankenstein.txt') as f:
        content = f.read()
    
    #word_count = 0
    content_split = content.split()

    #for word in content_split:
    #    word_count += 1
    #print(f"word count: {word_count})

    #print(f"word count:{len(content_split)}")
    #print(f"letter count: {count_letters(content)}")
    print('--- Begin report of books/frankenstien.txt')
    print(f"{len(content_split)} words found in the document")
    print()
    list_organizer(content)
    print('--- End report ---')
          
          

main()
          


"""
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
"""

"""
with open('books/frankenstein.txt') as f: - 
This line is using Python's with keyword, 
which is used for automatically managing resources, 
in this case, a file. 

The open function is called 
with the name of the file you want to open,
and as f assigns the file object that open 
returns to the variable f.

The .read() method is called on f, the file object.
This method reads the entire file and returns it as a string,
which gets stored in the content variable.

So in essence, this block of code opens the specified file, 
reads all its content into memory as a single string, 
and then automatically closes the file. 

After this block of code executes, 
you can use the content variable, 
which contains the content of the file, 
in the rest of your program.
"""

