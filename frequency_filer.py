import re

#  freq_value variable for each word  (value in dict?)
#  dictionary with key = word, value = count ?
#  if nxt_word is in dictionary, increase freq_value +=1
#     for nxt_word in material  ?
#     nxt_word in material  if False on to next one
#           if True increment freq_value
#  line 208 word in material.key
#fdksfajdshf
#     re.sub  ???
#     re.split !!!


def create_dictionary():
    material_dict = {}
    with open("sample.txt", 'r', newline='') as material:
        for line in material:
            line_lower = re.sub(r'[^A-Za-z]', "", (line.lower()))
            for word in line_lower:
                material_dict[word.split:0]



def word_frequency():
    for nxt_word in material:
        if material != material_dict[something]:
            word_frequency()
        else:


def find_top_20():

#  make a list of the words, and then list(zip(~words~, range(20)))
#    sorted(material, key=lambda w[0])      #137, 230
#   zip highest freq to numbers 1-20   in a tuple???
