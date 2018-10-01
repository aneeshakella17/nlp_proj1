import argparse
import string

# ap = argparse.ArgumentParser(description='Justify text within a file')
# ap.add_argument('-f', "--file", required = True, help = "file to justify");
# args = vars(ap);


def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result


our_dictionary = {};
dic = open("words_alpha.txt", 'r');
dic_words = dic.readlines();
for word in dic_words:
    word = word.strip();
    our_dictionary[word] = True;

file_name = "input.txt"
f = open(file_name, 'r');
lines = f.readlines();

justify_by = 0;


if(len(lines) > 0):
    try:
        justify_by = int(lines[0]);
    except:
        print("No number detected. Going to return file as is.")



orig_str = "";
new_str = "";

#remove any newlines
lines = [line.strip('\n') for line in lines[1::]];

#Remove any leading dashes and add necessary spaces;



for line_num in range(0, len(lines)):
    if(lines[line_num][-1] == "-"):

        pre_dash = 1;
        pre_word = "";

        while(lines[line_num][-1 - pre_dash] != " "):
           pre_word = lines[line_num][-1 - pre_dash] + pre_word
           pre_dash += 1;

        post_dash = 0;
        post_word = "";


        next_line_len = len(lines[line_num + 1]);
        while(next_line_len > post_dash and lines[line_num + 1][0 + post_dash] != " "):
            post_word += lines[line_num + 1][0 + post_dash];
            post_dash += 1;

        pre_word = remove_punctuation(pre_word);
        post_word = remove_punctuation(post_word)

        # print("1:", pre_word + post_word)
        # print("2:", our_dictionary.get(pre_word + post_word))
        # print(len(our_dictionary))
        if(our_dictionary.get(pre_word + post_word) == None):
            continue;
        else:
            lines[line_num] = lines[line_num][:-1];

    elif(lines[line_num][-1] != " "):
        lines[line_num] += " "


print(lines);
for line in lines:
    orig_str += line;

print(orig_str);


left_to_justify = len(orig_str);
start = 0;
while(left_to_justify >= 0):
    characters_in_line = min(justify_by, left_to_justify);

    # #check if you are splitting a word in the middle(if not use spaces);
    # if(characters_in_line > 2 and characters_in_line != left_to_justify):
    #
    #   if(orig_str[start + characters_in_line - 1].isalpha()
    #        and orig_str[start + characters_in_line -2].isalpha()):
    #         orig_str = orig_str[:start + characters_in_line - 1] + '-' + orig_str[start+characters_in_line - 1:];
    #         left_to_justify += 1



    new_str += orig_str[start:start + characters_in_line] + '\n';
    start += justify_by;
    left_to_justify -= justify_by;

print(new_str);
f = open("output.txt", 'w');
f.write(new_str);



