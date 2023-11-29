#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:15:43 2023

@author: seanfitze
"""

import crater as c
import matplotlib.pyplot as plt

class Surface:
    def __init__(self, squared_size):
        self.squared_size = squared_size
        self.crater_map = [[0 for _ in range(squared_size)] for _ in range(squared_size)]
        self.crater_lst = {}
        self.crater_factory = c.CraterFactory()
        self.num_craters = 0
        
    def TakeTimeStep(self):
        self.AddCrater()
        #TODO Check for wiped out craters
        self.PlotSurface()
    
    def AddCrater(self):
        # Create crater
        crater = self.crater_factory.CreateCrater(self.squared_size)
        # TODO: check for collisions
        if (crater.position_x, crater.position_y) not in self.crater_lst:
            self.crater_lst[(crater.position_x, crater.position_y)] = [crater]
        else:
            self.crater_lst[(crater.position_x, crater.position_y)].append(crater)
        # Add crater to map TODO: Do I still need this?
        self.crater_map[crater.position_x][crater.position_y] = 1
        self.num_craters += 1
        
    def PrintCraterMap(self):
        for i, row in enumerate(self.crater_map):
            print(self.crater_map[i])
    
    def PrintCraterList(self):
        print(self.crater_lst)
        
    def PlotSurface(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.squared_size)
        ax.set_ylim(0, self.squared_size)
        for position, craters in self.crater_lst.items():
            for crater in craters:
                # Only display visible craters
                if (crater.visible == True):    
                    circle = plt.Circle((crater.position_x, crater.position_y), crater.radius, fill=True, color = 'gray', label='Crater')
                    ax.add_patch(circle)
        # Display the plot
        plt.gca().set_aspect('equal', adjustable='box')  # Make sure the aspect ratio is equal
        plt.show()
        
    def isColliding(craterA, craterB):
        distance = math.sqrt((craterA.position_x - craterB.position_x)**2 + (craterA.position_y - craterB.position_y)**2)
        sum_radii = craterA.radius + craterB.radius
    
   # Check if createrOld is wiped out from craterNew
   # Find python function for this?
    # def isWipedOut(craterOld, craterNew):
        # Calculate area covered 
        # if area covered is over 50% wipe that bithc out (check how much of the rim is covered)
