import re

def main():       #  Open .txt file and prepare contents for processing
    with open("sample.txt", newline='') as material:  # Import file in lines
        for line in material:
            line_lc = re.sub(r'[^A-Za-z0-9\s]', "", (line.lower())) # Strip lines
            split_text = clean_text.split()
    return word_frequency(split_text)


def word_frequency():   # Compare and count words
    count_dict = {}
    for word in split_text:
        if word in count_dict:
            count_dict[word] = count_dict[word]+1
        else:
            count_dict[word] = 1
return count_dict


def find_top_20():
    sorted_data = sorted(count_dict, key=lambda  w: w[1])
    top_20 = list(zip(count_dict[]))

#  make a list of the words, and then list(zip(~words~, range(20)))
#    sorted(line_lc, key=lambda w[0])      #137, 230
