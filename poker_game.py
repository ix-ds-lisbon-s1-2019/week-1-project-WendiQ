#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:10:43 2019

@author: quwd
"""
import random
import sys
    
def winner(number_of_players):
    cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] 
    full_set = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] * 4
    # suits = ["clubs", "spades", "hearts", "diamonds"]
    
    # assign values to cards to compare them
    compare = {}
    for i in cards:
        compare[i] = cards.index(i)
    
    # draw cards for each player        
    players = {}
    i = 1
    while i <= int(number_of_players):
        name = input("What's the name of the player: ")
        draw = random.sample(full_set, 5)
        for card in draw:
            full_set.remove(card)
        players[name] = draw
        i += 1
        
    # print each player's cards
    for player, deals in players.items():
        print("Player {} has cards {}.".format(player, deals))
    
    # sort cards for each player
    for player, deals in players.items():
        for cd in deals:
            deals[deals.index(cd)] = compare[cd]
        players[player] = deals
        deals = deals.sort(reverse=True)
        
    # create a copy of players
    pla = players.copy()
    
    # compare cards
    for i in range(5):
        large = {}
        for player, deals in pla.items():
            large[player] = deals[i]
        large_ls = list(large.values())
        if large_ls.count(max(large_ls)) == 1:
            for player, card in large.items():
                if card != max(large_ls):
                    pla.pop(player)
            return("The winner is {}!".format((list(pla.keys())[0])))
        elif large_ls.count(max(large_ls)) > 1: 
            for player, card in large.items():
                if card != max(large_ls):
                    pla.pop(player)
                    
def NUMBER_OF_PLAYERS():
    number_of_players = input("What's the number of players: ")
    win = winner(number_of_players)
    return(win)
    
if __name__ == '__main__':
    globals()[sys.argv[1]]()
    
#    NUMBER_OF_PLAYERS()
#    globals()[sys.argv[1]]()
                    
#    class Cards():
#        def __init__(self, card):
#            self.name = cards.index(card)
#            
#        def __eq__(self, other):
#            if self is other:
#                return True
#            else:
#                return self.name == other.name
#                
#        def __gt__(self, other):
#            return self.name < other.name
#        
#        def __lt__(self, other):
#            return self.name < other.name