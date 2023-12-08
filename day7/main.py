from collections import Counter
from dataclasses import dataclass, field

ORDER = "AKQJT98765432"
ORDER_WITH_JOKER = "AKQT98765432J"


@dataclass
class Hand:
    cards: str
    bid: int
    replace_joker: bool
    type: int = field(init=False, repr=False)
    value: list[int] = field(init=False, repr=False)

    @classmethod
    def from_str(cls, s, replace_joker=False):
        cards, bid_s = s.split()
        return cls(cards, int(bid_s), replace_joker)

    def __post_init__(self):
        order = ORDER_WITH_JOKER if self.replace_joker else ORDER
        order2val = {}
        for i in range(len(order)):
            order2val[order[i]] = i
        self.value = list(map(order2val.__getitem__, self.cards))
        self.replace_joker_if_needed()
        if five_of_kind(self.cards):
            self.type = 0
        elif four_of_kind(self.cards):
            self.type = 1
        elif full_house(self.cards):
            self.type = 2
        elif three_of_kind(self.cards):
            self.type = 3
        elif two_pairs(self.cards):
            self.type = 4
        elif one_pair(self.cards):
            self.type = 5
        else:
            self.type = 6

    def replace_joker_if_needed(self):
        c = Counter(self.cards)
        if self.replace_joker and 0 < c["J"] < 5:
            mc = c.most_common(2)
            to_replace = mc[0][0] if mc[0][0] != "J" else mc[1][0]
            self.cards = self.cards.replace("J", to_replace)


def five_of_kind(cards):
    return len(set(cards)) == 1


def four_of_kind(cards):
    c = Counter(cards)
    return len(c) == 2 and c.most_common(1)[0][1] == 4


def full_house(cards):
    c = Counter(cards)
    return len(c) == 2 and c.most_common(1)[0][1] == 3


def three_of_kind(cards):
    c = Counter(cards)
    return len(c) == 3 and c.most_common(1)[0][1] == 3


def two_pairs(cards):
    c = Counter(cards)
    return len(c) == 3 and c.most_common(1)[0][1] == 2


def one_pair(cards):
    c = Counter(cards)
    return len(c) == 4


def solve(input_txt, replace_joker):
    with open(input_txt) as f:
        hands = []
        for line in map(lambda x: x.strip(), f.readlines()):
            hands.append(Hand.from_str(line, replace_joker=replace_joker))
        hands = sorted(hands, key=lambda hand: (hand.type, hand.value), reverse=True)
        res = 0
        for r, h in enumerate(hands):
            res += (r + 1) * h.bid
        return res


if __name__ == '__main__':
    print(solve("part1.txt", False))
    print(solve("part1.txt", True))
