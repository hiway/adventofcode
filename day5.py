import collections


def part1_is_nice_string(test_string):
    """
    --- Day 5: Doesn't He Have Intern-Elves For This? ---

    Santa needs help figuring out which strings in his
        text file are naughty or nice.

    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only),
        like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row,
        like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy,
        even if they are part of one of the other requirements.

    For example:

    >>> part1_is_nice_string('ugknbfddgicrmopn')
    True

    is nice because it has at least three vowels (u...i...o...),
    a double letter (...dd...), and none of the disallowed substrings.


    >>> part1_is_nice_string('aaa')
    True

    is nice because it has at least three vowels and a double letter,
    even though the letters used by different rules overlap.


    >>> part1_is_nice_string('jchzalrnumimnmhp')
    False

    is naughty because it has no double letter.

    >>> part1_is_nice_string('haegwjzuvuyypxyu')
    False

    is naughty because it contains the string xy.


    >>> part1_is_nice_string('dvszwmarrgswjxmb')
    False


    is naughty because it contains only one vowel.

    How many strings are nice?
    """

    def contains_three_vowels(test_string):
        alpha = collections.Counter(test_string)
        vowels = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            vowels += alpha.get(vowel, 0)
        return vowels >= 3

    def double_letter(test_string):
        for x in range(len(test_string) - 1):
            if test_string[x] == test_string[x + 1]:
                return True
        return False

    def no_nasties(test_string):
        for nasty in ['ab', 'cd', 'pq', 'xy']:
            if nasty in test_string:
                return False
        return True

    return (contains_three_vowels(test_string)
            and double_letter(test_string)
            and no_nasties(test_string))
