import re


def find_top_20(count_dict):
    # Sort results from most frequent to least.
    sorted_data = sorted(count_dict.items(), key=lambda w: w[1], reverse=True)
    return sorted_data[:20]


def word_frequency(text):     # (split_text):
    # Compare and count words
    # for line in text:
    line_lc = re.sub(r'[^A-Za-z0-9\s]', "", text).lower()  # Strip lines
    split_text = line_lc.split()    # Split the text on blank spaces
    count_dict = {}
    for word in split_text:     # count occurances of each word
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return(count_dict)


def main():
    # Open .txt file and call functions to process text
    with open("sample.txt", newline='') as f:  # Import file in lines
        word_frequency(f)
        find_top_20()
        for word in find_top_20(count_dict):
            print(word[0], word[1])


if __name__ == '__main__':
    main()
