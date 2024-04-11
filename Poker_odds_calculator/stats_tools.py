#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict
import itertools
from math import comb


# In[2]:


def is_flush(cards):
    suits_count = defaultdict(int)
    for card in cards:
        suits_count[card.suit] += 1
    return any(count >= 5 for count in suits_count.values())

def is_straight_flush(cards):
    # Find all possible flushes
    flushes = [combo for combo in itertools.combinations(cards, 5) if is_flush(combo)]

    # Find all possible straights within the flushes
    straight_flushes = [combo for combo in flushes if is_straight(combo)]

    # Return True if there is at least one straight flush
    return len(straight_flushes) > 0

def is_four_of_a_kind(cards):
    values_count = defaultdict(int)
    for card in cards:
        values_count[card.value] += 1
    return any(count >= 4 for count in values_count.values())

def is_full_house(cards):
    values_count = defaultdict(int)
    for card in cards:
        values_count[card.value] += 1
    
    has_two_or_more = any(count >= 2 for count in values_count.values())
    has_three_or_more = any(count >= 3 for count in values_count.values())
            
    if has_three_or_more and len([count for count in values_count.values() if count >= 2]) >= 2:
        return True
    else:
        return False

def is_straight(cards):
    unique_values = set(card.value for card in cards)
    values = sorted(unique_values)
    straight_count = 0
    
    # Check for Ace-low straight
    if 1 in values and 10 in values and 11 in values and 12 in values and 13 in values:
        values_set = set(values)  # Convert values list to a set
        values_set.discard(1)  # Remove Ace if present
        values_set.add(14)     # Add Ace as the highest value
        values = sorted(values_set)  # Convert back to list
    
    for i in range(len(values) - 1):
        if values[i] + 1 == values[i + 1]:
            straight_count += 1
            if straight_count >= 4:
                return True  # Found a straight
        else:
            straight_count = 0  # Reset the count if not consecutive
    
    return False

def is_three_of_a_kind(cards):
    values_count = defaultdict(int)
    for card in cards:
        values_count[card.value] += 1
    return any(count >= 3 for count in values_count.values())

def is_two_pair(cards):
    values_count = defaultdict(int)
    for card in cards:
        values_count[card.value] += 1
    pairs = sum(count >= 2 for count in values_count.values())
    return pairs >= 2

def is_one_pair(cards):
    values_count = defaultdict(int)
    for card in cards:
        values_count[card.value] += 1
    return any(count >= 2 for count in values_count.values())

def is_high_card(cards):
    return True


# In[3]:


class Hands:
    def __init__ (self,hand_name):
        self.count = 0
        self.hand_name = hand_name
    def increment_count(self):
        self.count += 1
    def hand_odds(self,total_combinations):
        hand_odds = (self.count)/(total_combinations)*100
        print(f"{self.hand_name} count:{self.count}, {self.hand_name} odds:{hand_odds:.2f}% \n")


# In[1]:


def pre_flop_hand_counts(unknown_cards, known_cards,flush, straight_flush, four_of_a_kind, full_house, straight, three_of_a_kind, two_pair, one_pair):
    for flop1, flop2, flop3, turn_card, river_card in itertools.combinations(unknown_cards,5 ):
        community_cards = [flop1, flop2, flop3, turn_card, river_card]
        if all(card not in known_cards for card in community_cards):
            if is_one_pair(known_cards + community_cards):
                one_pair.increment_count()
                if is_two_pair(known_cards + community_cards):
                    two_pair.increment_count()               
                if is_three_of_a_kind(known_cards + community_cards):
                    three_of_a_kind.increment_count()
                    if is_full_house(known_cards + community_cards):
                        full_house.increment_count()
                    if is_four_of_a_kind(known_cards + community_cards):
                        four_of_a_kind.increment_count()
            if is_straight(known_cards + community_cards):
                straight.increment_count()
            if is_flush(known_cards + community_cards):
                flush.increment_count()
                if is_straight_flush(known_cards + community_cards):
                    straight_flush.increment_count()       


# In[4]:


def post_flop_hand_counts(unknown_cards, known_cards,flush, straight_flush, four_of_a_kind, full_house, straight, three_of_a_kind, two_pair, one_pair):
    for turn_card, river_card in itertools.combinations(unknown_cards, 2):
        if turn_card != river_card and turn_card not in known_cards and river_card not in known_cards:
            if is_one_pair(known_cards + [turn_card, river_card]):
                one_pair.increment_count()
                if is_two_pair(known_cards + [turn_card, river_card]):
                    two_pair.increment_count()               
                if is_three_of_a_kind(known_cards + [turn_card, river_card]):
                    three_of_a_kind.increment_count()
                    if is_full_house(known_cards + [turn_card, river_card]):
                        full_house.increment_count()
                    if is_four_of_a_kind(known_cards + [turn_card, river_card]):
                        four_of_a_kind.increment_count()
            if is_straight(known_cards + [turn_card, river_card]):
                straight.increment_count()
            if is_flush(known_cards + [turn_card, river_card]):
                flush.increment_count()
                if is_straight_flush(known_cards + [turn_card, river_card]):
                    straight_flush.increment_count()        


# In[5]:


def post_turn_hand_count(unknown_cards, known_cards,flush, straight_flush, four_of_a_kind, full_house, straight, three_of_a_kind, two_pair, one_pair):
    for river_card in unknown_cards:
        if river_card not in known_cards:
            if is_one_pair(known_cards + [river_card]):
                one_pair.increment_count()
                if is_two_pair(known_cards + [river_card]):
                    two_pair.increment_count()               
                if is_three_of_a_kind(known_cards + [river_card]):
                    three_of_a_kind.increment_count()
                    if is_full_house(known_cards + [river_card]):
                        full_house.increment_count()
                    if is_four_of_a_kind(known_cards + [river_card]):
                        four_of_a_kind.increment_count()
            if is_straight(known_cards + [river_card]):
                straight.increment_count()
            if is_flush(known_cards + [river_card]):
                flush.increment_count()
                if is_straight_flush(known_cards + [river_card]):
                    straight_flush.increment_count()


# In[ ]:





# In[ ]:




