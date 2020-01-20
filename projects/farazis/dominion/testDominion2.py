# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:00:00 2020

@author: farazis
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#Define get nv (number of victory cards)
nV = testUtility.get_nv(len(player_names))

#Define get nv (number of curse cards)
nC = testUtility.get_nc(len(player_names))

#Define box
box = testUtility.get_boxes(nV)

#[Bug Introduced]: changing all cards to Market
for item in box:
    box[item] = [Dominion.Market()]*10

#Define supply order
supply_order = testUtility.get_supply_order()

#Define supply 
supply = testUtility.get_supply(player_names, nV, nC, box)

#Define get players (Costruct the Player objects)
players = testUtility.get_players(player_names)

#Define play the game
testUtility.play_game(supply_order, supply, players)          

#Define final score
testUtility.display_final_score(players)