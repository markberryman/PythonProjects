class SpellChecker(object):
    @staticmethod
    def get_vowels():
        return { 'a', 'e', 'i', 'o', 'u' }

    @staticmethod
    def is_vowel(char):
        return char in SpellChecker.get_vowels()

    @staticmethod
    def trim_word_list(word, word_list):
        # trimming word list based on a few possible
        # optimizations based on the word's length and
        # the first character it starts with
        new_word_list = set()
        
        # reducing set of possible suggestions based on first
        # character of word
        if (SpellChecker.is_vowel(word[0]) is False):
            word_must_start_with_char_set = word[0]
        else:
            word_must_start_with_char_set = SpellChecker.get_vowels()

        for suggestion in word_list:
            # trim word list by removing words longer
            # than a possible suggestion for the word
            if (len(suggestion) <= len(word)):
                # trim list by removing words that don't
                # start with a character that could make up
                # a possible suggestion
                if (suggestion[0].lower() in word_must_start_with_char_set):
                    new_word_list.add(suggestion)

        #print("Removing {} words.".format(len(word_list) - len(new_word_list)))

        return new_word_list

    @staticmethod
    def recommend(word, word_list):
        # simplify things by lower-casing the word
        # right off the bat
        word = word.lower()
                
        reduced_word_list = SpellChecker.trim_word_list(word, word_list)
        
        # quick check for the case where the word only
        # differs in case; making an assumption that
        # it's likely that most words would be spelled
        # correctly on first try
        suggestion = SpellChecker.check_word(word, reduced_word_list)

        if (suggestion is not None):
            return suggestion

        suggestions = SpellChecker.create_suggestions(word)

        possible_suggestions = set()

        for suggestion in suggestions:
            word_match = SpellChecker.check_word(suggestion, reduced_word_list)
            if (word_match is not None):
                possible_suggestions.add(word_match)

        if (len(possible_suggestions) > 0):
            return possible_suggestions.pop()

        return "NO SUGGESTION"

    @staticmethod
    def create_suggestions(word):
        result = set()

        vowel_variations = SpellChecker.create_vowel_variations(word)
        repeated_letters_variations = set()

        for vowel_variation in vowel_variations:
            repeated_letters_variations = SpellChecker.create_repeated_letters_variations(vowel_variation)
            result = result.union(repeated_letters_variations)

        return result

    @staticmethod
    def create_repeated_letters_variations(word):
        result = set()
        result.add(word)

        # look for a block of repeated letters
        # if found, create word variants with the
        # block of repeated chars crunched down one char
        # at a time
        # (e.g, "xxx" -> { "xxx", "xx", "x" }
        repeated_char_count = 1

        for i in range(len(word)):
            if ((i != len(word) - 1) and (word[i] == word[i+1])):
                repeated_char_count += 1
            else:
                if (repeated_char_count > 1):
                    repeated_letter_variations = SpellChecker.create_repeated_letters_variations_helper(word, i, repeated_char_count)

                    for perm in repeated_letter_variations:
                        result = result.union(SpellChecker.create_repeated_letters_variations(perm))

                repeated_char_count = 1
            
        return result

    @staticmethod
    def create_repeated_letters_variations_helper(word, idx_last_repeat_char, repeated_char_count):
        # create variations with subsets of the repeated chars
        # don't return the original word though
        result = set()

        chars_after_repeated_char = word[idx_last_repeat_char + 1:]

        while (repeated_char_count > 1):
            word_with_collapsed_repeated_chars = word[:idx_last_repeat_char - repeated_char_count + 2] + chars_after_repeated_char

            result.add(word_with_collapsed_repeated_chars)

            repeated_char_count -= 1

        return result

    @staticmethod
    def create_vowel_variations(word):
        result = set()
        result.add(word)

        # look at each char in word
        # if it's a vowel, create variatons
        # of the word using every other vowel
        for i in range(len(word)):
            for word in result:
                if (SpellChecker.is_vowel(word[i])):
                    vowel_variations = SpellChecker.create_vowel_variations_helper(word, i)
                    result = result.union(vowel_variations)

        return result

    @staticmethod
    def create_vowel_variations_helper(word, idx):
        # create variations of word replacing vowel
        # at specified index
        result = set()
        
        vowels = SpellChecker.get_vowels()

        for vowel in vowels:
            # to enable char replacement we convert
            # the string to a list
            temp_word = list(word)
            temp_word[idx] = vowel

            # convert word back to string
            result.add("".join(temp_word))

        return result

    @staticmethod
    def check_word(word, word_list):
        result = None
                
        word_to_check_length = len(word)

        # I considered doing a set "in" check first 
        # in case we have a match w/o having to worry 
        # about case differences, but that would only happen
        # when we're looking up a word that exists in the word_list
        # and if that's the case, we have an initial check very
        # early on for this scenario so we wouldn't get any benefit
        # here; additionally, most of the words that will be
        # checked are the permutations of the original word which
        # might not (maybe highly likely) be in the word_list; in
        # this case, we're doing extra work w/ the set "in" check
        for suggestion in word_list:
            # do our case error handling here
            if (word == suggestion.lower()):
                # a match!
                result = suggestion
                break

        return result
