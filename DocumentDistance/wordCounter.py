class WordCounter(object):
    """Abstract class."""


    def read_file(self, filename):
        """Read the text file with the given filename;
           return a list of the lines of text in the file."""

        lines = None

        try:
            file = open(filename)
            lines = file.readlines()
        except IOError:
            print("Error opening or reading input file: {}".format(filename))
            
        return lines

    def count_words(self, input):
        """Counts the number of words in the provided input string."""
        raise NotImplementedError()

class SimpleWordCounter(WordCounter):
    def _get_words_from_string(self, line):
        word_list = []          # accumulates words in line
        character_list = []     # accumulates characters in word

        for c in line:
            if c.isalnum():
                character_list.append(c)
            elif len(character_list) > 0:
                word = ''.join(character_list)
                word = word.lower()
                word_list.append(word)
                character_list = []

        # grab that last word in the line if it exists
        if len(character_list)>0:
            word = ''.join(character_list)
            word = string.lower(word)
            word_list.append(word)

        return word_list

    def count_words(self, input):
        word_list = []
        
        for line in input:
            words_in_line = self._get_words_from_string(line)
            word_list = word_list + words_in_line

        return word_list
