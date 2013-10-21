class BoyerMoore(object):
    """Boyer-Moore string searching algorithm using the "bad-character" rule.
    http://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm"""
    @staticmethod
    def search(pattern, text):
        result = False

        pattern_length = len(pattern)
        text_length = len(text)

        # we'll start checking at the first place
        # the pattern could possibly match
        # note that the alignment index corresponds
        # to the end of the pattern; we'll check chars
        # going backwards
        alignment_index = pattern_length - 1

        while (alignment_index < text_length):
            temp_alignment_index = alignment_index
            pattern_index = pattern_length - 1

            # look for pattern in text
            while (pattern_index >= 0 and
                   (pattern[pattern_index] == text[temp_alignment_index])):
                pattern_index -= 1
                temp_alignment_index -= 1

            if (pattern_index == -1):
                result = True
                break

            # no match, see if the mismatched character from
            # the text exists somewhere in the pattern
            while (pattern_index != -1):
                if (pattern[pattern_index] == text[temp_alignment_index]):
                    break
                
                pattern_index -= 1

            if (pattern_index == -1):
                # didn't find mismatched character anywhere in
                # the pattern
                alignment_index += pattern_length
            else:
                alignment_index += (pattern_length - 1) - pattern_index

        return result
