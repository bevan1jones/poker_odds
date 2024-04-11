#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from collections import defaultdict
from itertools import combinations
from math import comb


# In[2]:


class PlayingCard:
     def __init__(self,suit,value,deck_number=1):
         self.suit = suit
         self.value = value


# In[3]:


class Deck:
    def __init__(self):
        self.cards = [PlayingCard(suit, value) for suit in ['heart', 'spade', 'club', 'diamond'] for value in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            raise ValueError("Deck is empty")
            


# In[4]:


class Player:
    def __init__ (self,player_id):
        self.player_id=player_id
        self.cards =[]
        self.best_hand=[]

    def deal_cards(self, deck, num_cards):
        for _ in range(num_cards):
            self.cards.append(deck.deal_card())



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




