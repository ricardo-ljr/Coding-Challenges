# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.


class Solution:
    def arrangeWords(self, text: str) -> str:
        # make entire string lower capital
        text = text.lower()
        # store text in a list
        newText = text.split()

        # check for shortest string in list
        # Push to a new list in order
        inOrderList = sorted(newText, key=len)

        # capitalizE first item in list

        inOrderList[0].title()

        print(inOrderList)

        result = ' '  # final string result

        # Create String
        return (result.join(inOrderList).capitalize())
