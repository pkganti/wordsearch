import os
import sys
import pdb

try:
    file_name = sys.argv[1]
    output_file = file_name.split('.')[0]+'.out'
except(IndexError):
    sys.exit("Please enter a valid file name")

matching_word_positions = {}


def reading_file_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # Removing the new line character from the list elements and save the row wise elements
        lines = [line.strip() for line in lines]
        line_break = lines.index('') #Getting index of the first blank line

        row_elements = lines[:line_break] #The elements list that we will be using
        words_input = lines[line_break+1:] #List of the words that we need to search for
        return ({"row_elements": row_elements, "words_input": words_input})

def horizontal_search(row_elements, start_pos, end_pos, words_input):
    for index, ele in enumerate(row_elements):

        # Left to right search
        for i in range(start_pos, end_pos+1):
            match_word = ""
            for j in range(i, end_pos+1):
                match_word += ele[j-1]
                if match_word in words_input:
                    if not matching_word_positions.has_key(match_word):
                        matching_word_positions[match_word] = "(%s, %s)(%s, %s)"%(i, index+1, j, index+1)

        # Right to left search
        for i in range(end_pos, start_pos-1, -1):
            match_word = ""
            for j in range(i, start_pos-1, -1):
                match_word += ele[j-1]
                if match_word in words_input:
                    if not matching_word_positions.has_key(match_word):
                        matching_word_positions[match_word] = "(%s, %s)(%s, %s)"%(i, index+1, j, index+1)

def vertical_search(elements, start_pos, end_pos, words_input):

    for index, ele in enumerate(elements):
        # Left to right search
        for i in range(start_pos, end_pos+1):
            match_word = ""
            for j in range(i, end_pos+1):
                match_word += ele[j-1]
                if match_word in words_input:
                    if not matching_word_positions.has_key(match_word):
                        matching_word_positions[match_word] = "(%s, %s)(%s, %s)"%(index+1, i, index+1, j)

        # Right to left search
        for i in range(end_pos, start_pos-1, -1):
            match_word = ""
            for j in range(i, start_pos-1, -1):
                match_word += ele[j-1]
                if match_word in words_input:
                    if not matching_word_positions.has_key(match_word):
                        matching_word_positions[match_word] = "(%s, %s)(%s, %s)"%(index+1, i, index+1, j)

def writing_file_output(file_name):
    with open(file_name, 'w') as out_file:
        for key, value in matching_word_positions.items():
            out_file.write("%s %s\n"%(key, value))

#Step1: Reading the lines and forming the elements list
data = reading_file_input(file_name)

# Here we try to inverse the list elements to vertically search the lists
columnwise_elements = []
for i in range(0,len(data['row_elements'])):
    word = ""
    for ele in data['row_elements']:
        word += ele[i]
    columnwise_elements.append(word)

# lets take the starting and ending coordinates to pass to the functions
start_pos = 1
end_pos = len(data['row_elements'])

#Step2: Horizontal search and update the matching position dictionary
horizontal_search(data['row_elements'], start_pos, end_pos, data['words_input'])

#Step3: Vertical search and update the matching position dictionary
vertical_search(columnwise_elements, start_pos, end_pos, data['words_input'])

#Step4: If the word in the input file is not found in puzzle add the word as Key and the value as not found
for input in data['words_input']:
    if not input in matching_word_positions.keys():
        matching_word_positions[input] = "not found"

#Step5: Writing the key value pairs to the output file
writing_file_output(output_file)
