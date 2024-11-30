import random

import config as CFG

class Tokens:

    def __init__(self, tokens: list) -> None:

        self.tokens = tokens
        random.shuffle(self.tokens)

    def count(self) -> int:
        return len(self.tokens)

    def shuffle(self):
        random.shuffle(self.tokens)

    def add(self, token):
        self.tokens.append(token)
        random.shuffle(self.tokens)

    def remove(self, token):
        self.tokens.remove(token)

    def get(self) -> str:
        t = random.choice(self.tokens)
        self.tokens.remove(t)
        return t

    def show(self):
        print(self.tokens)

if __name__ == "__main__":

    t = Tokens(CFG.START_INTRUDERS_TOKENS)
    t.show()

    t.add("QUEEN")
    t.show()
    t.remove("QUEEN")
    t.show()

    print(t.get())
    t.show()
