# Author: Quanyue Xie
# Date: 10/21/2020
# Description： modify a insertion sort, so that it can sort string
#according to order of letter

def string_sort(string_list):
    #traverse every string in string_list
    for i in range(1, len(string_list)):
        #uppercase letter are converted to lowercase
        word = string_list[i].lower()
        j = i - 1
        compareWord = string_list[j].lower()
        index = 0
        while index < len(word):
            #the first letter of current string compare to compareWord
            firstWordLetter = word[index]
            compareWordLetter = compareWord[index]
            index += 1
            #accoring to insertion sort, change position
            if j >= 0 and firstWordLetter < compareWordLetter:
                string_list[j + 1] = string_list[j]
                j -= 1
                break
        string_list[j + 1] = word
    print(string_list)


if __name__ == "__main__":
    string_list = ["Zebra","apple","cat","false","place"]
    string_sort(string_list)
