def wordSort(preprocessed_words):
    """
    :param preprocessed_words: list of preprocessed words
    :return: list of words in alphabetical order
    :pre-condition: preprocessed_words is a valid list
    :post-condition: sorted array of words in alphabetical order
    :time complexity: Worst-case: O(nm) # Nested loops which iterates for max m characters * n words in list
    :space complexity: Worst-case: O(nm) # n*m operations based on n words which are characters of max size m.
    """
    # Do counting sort inside radix sort from least significant place to most significant place
    # Establish list as a nested array of 27 lists, each list represents one alphabet of
    # the 26 alphabets, with one more list for storing unindexable words

    # first find the word with longest characters
    # perform N times for N longest characters

    # String -> Characters -> Integers -> Digits -> Radix Sort

    max_length = len(max(preprocessed_words, key=len))

    # initial list which will become sorted after performing counting sort(s)
    final_sorted_list = preprocessed_words

    # iteratively call counting sort on every index from least significant digit to most

    for i in range(max_length):
        final_sorted_list = countingSort(final_sorted_list,max_length,max_length - i - 1)

    return final_sorted_list


def countingSort(array, size, index):
    """
    :param array: list of words - requires multiple calls to sort for all index up to size
    :param size: the size of the maximum index to handle
    :param index: the current index to sort all word[index] for
    :return: sorted list of words based on specified index
    :pre-condition: array, size, and index are valid values
    :post-condition: list must be stable and in alphabetical order based on specified index in word
    :time complexity: Worst-case: O(n) for n words in list
    :space complexity: Worst-case: O(n) # for n words in list
    """

    # Perform counting sort on all words in array
    # array[0] stores words that cannot be compared
    # array[1-27] represents alphabets $ - a - z

    # initialize table
    frequency_list = [[] for _ in range(28)]

    # store count of occurrence for each word index in the defined table
    for word in array:

        # if current word's length is not comparable, store it in the empty symbol sublist
        if len(word) - 1 < index:
            frequency_list[0].append(word)

        # else store word in the frequency list representing the alphabet for its index value
        else:
            if word[index] == "$":
                frequency_list[1].append(word)

            else:
                frequency_list[ord(word[index]) - 95].append(word)

    # define a list which represents the current sorted state of the list based
    # on sorting n index times of max string's length
    output_list = []

    for word_list in frequency_list:

        if word_list:
            for word in word_list:
                output_list.append(word)

    return output_list


def naive_bwt(string):
    # loop
    return False

def efficient_bwt(string):
    return False

def bwt_encoding(string):

    # create a table storing all possible rotations of the string
    rotations = [""] * len(string)

    for i in range(len(string)):

        j = i  # current index in string
        k = 0

        # copy second part from point of rotation

        while j < len(string):
            rotations[k] += string[j]
            k += 1
            j += 1

        # Copy first part from rotation

        j = 0
        while j < i:
            rotations[k] += string[j]
            j += 1
            k += 1

    # sort rows alphabetically
    sorted_list = wordSort(rotations)

    # return last column of table
    bwt_string = ""
    for rotation in sorted_list:
        bwt_string += rotation[len(rotation) - 1]

    return bwt_string


def main():

    # Assume my implementation only works for lower-case strings
    # as i did not handle ord() for upper-case strings
    print(bwt_encoding("banana" + "$"))




if __name__ == "__main__":
    main()