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


def pre_and_post_dash(lines):
    pre_dash = 1;
    pre_word = "";

    while (lines[0][-1 - pre_dash] != " "):
        pre_word = lines[0][-1 - pre_dash] + pre_word
        pre_dash += 1;

    post_dash = 0;
    post_word = "";

    next_line_len = len(lines[1]);
    while (next_line_len > post_dash and lines[1][0 + post_dash] != " "):
        post_word += lines[1][0 + post_dash];
        post_dash += 1;

    pre_word = remove_punctuation(pre_word);
    post_word = remove_punctuation(post_word)


    return pre_word, post_word;

def main():
    our_dictionary = {};
    dic = open("words_alpha.txt", 'r');
    dic_words = dic.readlines();
    for word in dic_words:
        word = word.strip();
        our_dictionary[word] = True;

    file_name = "input3.txt"
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
    paragraphs = [];
    paragraph = [];
    for line in lines[1::]:
        if(line == '\n'):
            paragraphs.append(paragraph);
            paragraph = [];
        paragraph.append(line.strip('\n'));
    paragraphs.append(paragraph)



    #Remove any leading dashes and add necessary spaces;
    new_str = "";
    for i in range(0, len(paragraphs)):


        lines = paragraphs[i];

        if(i != len(paragraphs) - 1):
            lines.append("\n")


        orig_str = "";
        for line_num in range(0, len(lines)):
            if(len(lines[line_num]) <= 0):
                continue;
            elif(lines[line_num][-1] == "-"):
                pre_word, post_word = pre_and_post_dash([lines[line_num], lines[line_num + 1]]);
                if(our_dictionary.get(pre_word + post_word) == None):
                    continue;
                else:
                    lines[line_num] = lines[line_num][:-1];

            elif(lines[line_num][-1] != " "):
                lines[line_num] += " "

        for line in lines:
            orig_str += line;


        left_to_justify = len(orig_str);

        start = 0;
        while(left_to_justify > 0):
            characters_in_line = min(justify_by, left_to_justify);

            if(orig_str[start + characters_in_line - 1].isalpha()
                and orig_str[start + characters_in_line - 2].isalpha()):
                        if(len(orig_str) > start + characters_in_line and orig_str[start + characters_in_line].isalpha()):
                            orig_str = orig_str[:start+characters_in_line - 1] + '-' + orig_str[start + characters_in_line - 1:]
                            left_to_justify += 1;

            elif(orig_str[start + characters_in_line - 1].isalpha() and orig_str[start + characters_in_line - 2] == " "):
                orig_str = orig_str[:start + characters_in_line - 1] + ' ' + orig_str[start + characters_in_line - 1:];
                left_to_justify += 1;


            new_str += orig_str[start:start + characters_in_line] + '\n';
            start += characters_in_line;
            left_to_justify -= characters_in_line;

    f = open("output.txt", 'w');
    print(repr(new_str))
    f.write(new_str);


main();


