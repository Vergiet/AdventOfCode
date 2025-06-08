#!/usr/bin/python3

import os
import re
import sys

from typing import List
from functools import lru_cache, reduce

sys.setrecursionlimit(2147483647)

HAND_TYPE_r = r"^(?=.{5}$).*?((?P<high_straight>(?!.*(?P<hscard>.).*(?P=hscard))[TJQKA]{5})|(?P<straight>(?!.*(?P<scard>.).*(?P=scard))(?:[A2345]{5}|[23456]{5}|[34567]{5}|[45678]{5}|[56789]{5}|[6789T]{5}|[789TJ]{5}|[89TJQ]{5}|[9TJQK]{5}))|(?P<five_of_a_kind>.)(?:.*(?P=five_of_a_kind)){4}|(?P<four_of_a_kind>.)(?:.*(?P=four_of_a_kind)){3}|(?P<full_house>(?=.*(?P<fh_card1>.)(?=(?:.*(?P=fh_card1)){2}))(?=.*(?P<fh_card2>(?!(?P=fh_card1)).)(?=.*(?P=fh_card2))).+)|(?P<three_of_a_kind>.)(?:.*(?P=three_of_a_kind)){2}|(?P<two_pair>(?=.*(?P<tp_card1>.)(?=.*(?P=tp_card1)))(?=.*(?P<tp_card2>(?!(?P=tp_card1)).)(?=.*(?P=tp_card2))).+)|(?P<two_of_a_kind>.).*(?P=two_of_a_kind))"

# None = high_card

# 0 = gehele string waar een match in zit
# 1 = begin en eind van de gehele match
# 2 = high_straight
# 4 = straight

# 6 = five_of_a_kind_card **
# 7 = four_of_a_kind_card **
# 8 = fullhouse **
# 9 = fh_card1
# 10 = fh_card2
# 11 = three_of_a_kind_card **
# 12 = two_pair **
# 13 = tp_card1
# 14 = tp_card2
# 15 = two_of_a_kind_card **

type_mapping = {
    "6": "five_of_a_kind",
    "7": "four_of_a_kind",
    "8": "full_house",
    "11": "three_of_a_kind",
    "12": "two_pair",
    "15": "one_pair"
}

hand_type_index = [
    "high_card",
    "one_pair",
    "two_pair",
    "three_of_a_kind",
    "full_house",
    "four_of_a_kind",
    "five_of_a_kind"
]


class Card(object):
    def __init__(self, card):
        self.card = card

    def set_value(self, card_index):
        self.card_value = card_index.index(self.card)

    def __eq__(self, other):
        return self.card_value == other.card_value

    def __lt__(self, other):
        return self.card_value < other.card_value

    def __gt__(self, other):
        return self.card_value > other.card_value

    def __ne__(self, other):
        return self.card_value != other.card_value

    def __str__(self):
        return f"{self.card}"

    def to_binary(self):
        return '{0:04b}'.format(self.card_value)


class Hand(object):
    def __init__(self, cards: List[Card], bid_value):
        self.cards = cards
        self.bid_value = bid_value
        self.get_hand_type()

    def cards_to_str(self):
        return f"{reduce(concat, self.cards)}"

    def get_hand_type(self):
        self.hand_type, self.hand_value = get_hand_type_info(
            self.cards_to_str())

    def to_binary(self):
        cards_as_bin = reduce(concat_binary, self.cards)
        return '{0:04b}'.format(self.hand_value)+cards_as_bin

    def __eq__(self, other):
        return (
            self.hand_value == other.hand_value and
            self.cards[0] == other.cards[0] and
            self.cards[1] == other.cards[1] and
            self.cards[2] == other.cards[2] and
            self.cards[3] == other.cards[3] and
            self.cards[4] == other.cards[4]
        )

    def __str__(self):
        return f"cards: {self.cards_to_str()} and bid: {self.bid_value}, and type: {self.hand_type} and value: {self.hand_value}"


def get_hand_type_info(hand):
    x = re.search(HAND_TYPE_r, hand)
    hand_type = None
    if x != None:
        for type_key in type_mapping:
            if x.group(int(type_key)):
                hand_type = type_mapping[type_key]

    if not hand_type:
        hand_type = "high_card"

    hand_type_value = hand_type_index.index(hand_type)

    return hand_type, int(hand_type_value)

def concat(a, b):
    return f"{a}{b}"


def concat_binary(a, b):
    if isinstance(a, Card):
        a = a.to_binary()
    return f"{a}{b.to_binary()}"


def parse_hand(cards, bid_value):
    card_list = []
    for card in cards:
        card_list.append(Card(card))

    return Hand(card_list, int(bid_value))


def read_file(file):
    filepath = os.path.join(os.path.split(__file__)[0], file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content


def parse_strings(item):
    cards, bid_value = item.split(" ")
    return parse_hand(cards, bid_value)


def parse_result(actual_result, expected_result, inputfile):
    if expected_result == actual_result:
        print("Success!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
    else:
        print("Catastrophic Failure!")
        print(f"inputfile: {inputfile}")
        print(f"expected_result: {expected_result}")
        print(f"actual_result: {actual_result}")
        print(f"diff: {expected_result-actual_result}")


def sort_binary(hand):
    as_int = int(hand.to_binary(), 2)
    return as_int


def main1(inputfile, expected_result_1=0, expected_result_2=0):

    card_index = []
    for card in "AKQJT98765432":
        card_index.append(card)

    card_index.reverse()

    print(read_file(inputfile))
    actual_result = 0

    hands = list(map(parse_strings, read_file(inputfile).splitlines()))
    for hand in hands:
        for card in hand.cards:
            card.set_value(card_index)

    hands_sorted = sorted(hands, key=sort_binary)

    for i in range(len(hands_sorted)):
        print(f"hand_sorted: {hands_sorted[i]}")
        print(f"hand_sorted_to_bin: {hands_sorted[i].to_binary()}")

    values = 0
    for hand in hands_sorted:
        index = hands_sorted.index(hand) + 1
        values += hand.bid_value * index

    actual_result = values

    parse_result(actual_result, expected_result_1, inputfile)


def main2(inputfile, expected_result_1=0, expected_result_2=0):
    card_index = []
    for card in "AKQJT98765432J":
        card_index.append(card)

    card_index.reverse()

    print(read_file(inputfile))
    actual_result = 0

    hands = list(map(parse_strings, read_file(inputfile).splitlines()))
    for hand in hands:
        print(hand)
        for card in hand.cards:
            card.set_value(card_index)

    hands_sorted = sorted(hands, key=sort_binary)

    values = 0
    for hand in hands_sorted:
        index = hands_sorted.index(hand) + 1
        values += hand.bid_value * index

    actual_result = values

    parse_result(actual_result, expected_result_2, inputfile)

if __name__ == "__main__":
    for inputfile in (
        ("example", 6440, 5905),
        ("input", 247815719, 0),
    ):
        main1(*inputfile)
        main2(*inputfile)
