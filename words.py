def print_upper_words(words, must_start_with):
    """ prints out words from a list in uppercase,
        making new lines for each word
        """

    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print(word.upper())
                break  # break since you dont need to check the other letter


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
