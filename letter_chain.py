import unittest


def get_letter_chain(word):
    max_chain = ""
    chain = ""
    last_letter = ""

    for letter in word:
        chain += letter

        if letter != last_letter:
            chain = ""
            chain += letter

        if len(chain) > len(max_chain):
            max_chain = chain

        last_letter = letter

    return max_chain


class TestLetterChain(unittest.TestCase):

    def test_letter_chain_in_the_begin(self):
        self.assertEqual(get_letter_chain("aaaraag"), "aaa")

    def test_letter_chain_in_the_middle(self):
        self.assertEqual(get_letter_chain("tlettter"), "ttt")

    def test_letter_chain_in_the_end(self):
        self.assertEqual(get_letter_chain("ffooo"), "ooo")

    def test_letter_chain_mix(self):
        self.assertEqual(get_letter_chain("ffgfooooaaaasa"), "oooo")

if __name__ == '__main__':
    unittest.main()