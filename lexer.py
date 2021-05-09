import re

class TokenStream:
    tokens = []
    cursor = 0

def check_word(word):
    if (word == "epic"):
        print("Hooray! I found something epic")

class SchLexer:
    current_line = 0
    current_column = 0

    def __init__(self, input_buffer):
        self.buffer = input_buffer

    def parse(self):
        current_word = ""

        for char in self.buffer:
            if re.match(r'[\n\t ]', char):
                check_word(current_word)
                current_word = ""
                continue
            current_word += char
            

instance = SchLexer("epic shit")
instance.parse()