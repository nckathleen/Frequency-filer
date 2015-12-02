import re


def find_top_20(count_dict):
    # Sort results from most frequent to least.
    sorted_data = sorted(count_dict, key=lambda w: w[1])
    top_20 = (list(zip(sorted_data, count_dict[1])))
    return top_20


def word_frequency(split_text):
    # Compare and count words
    count_dict = {}
    for word in split_text:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return(count_dict)


def main():
    #  Open .txt file and prepare contents for processing
    split_text = ''
    line_lc = ''
    with open("shakespeare.txt", newline='') as material:  # Import file in lines
        for line in material:
            line_lc = re.sub(r'[^A-Za-z0-9\s]', "", (line.lower()))  # Strip lines
            split_text.append(line_lc.split())
            print("Another line!")
    word_frequency(split_text)
    find_top_20(count_dict)
    print(top_20)


#  make a list of the words, and then list(zip(~words~, range(20)))
#    sorted(line_lc, key=lambda w[0])      #137, 230
