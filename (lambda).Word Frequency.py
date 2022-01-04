"""
Given a document
"Practice? makes' perfect. Practice!"

Return a 2d list containing each word and its count. 
Also, in the case of a tie, the word that appears earlier comes before the others of same
frequency in the list

Example:
doc = "Practice makes perfect. you'll only get Perfect by practice. just practice!"  
Answer:
[['practice', '3'], ['perfect', '2'], ['makes', '1'], ['youll', '1'], ['only', '1'], ['get', '1'], ['by', '1'], ['just', '1']]
"""


def word_count_engine(document):
    """
    My approach: use 2 hashmaps
    Space: O(n)
    Time: O(n*log(n))
    """
    freq = {}
    word2idx = {}

    # Eliminate any punctuations ',.! and lower case all characters
    document = "".join(
        char for char in document if char.isalpha() or char == " ").lower()

    # Maintain a frequency mapping
    tokens = document.split()

    # Get word 2 index mapping
    for i in range(len(tokens)):
        # Only record the first occurence
        if tokens[i] not in word2idx:
            word2idx[tokens[i]] = i

    for t in tokens:
        if t not in freq:
            freq[t] = "1"
        else:
            freq[t] = str(int(freq[t])+1)
    # Arrange by word order (arrange by frequency, then word order)
    result = sorted([[t, freq[t]] for t in freq], key=lambda x: (
        int(x[1]), -word2idx[x[0]]), reverse=True)
    return result


# Test cases
doc = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(doc))
