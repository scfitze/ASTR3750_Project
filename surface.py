#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:15:43 2023

@author: seanfitze
"""

import crater as c
import matplotlib.pyplot as plt
import math

class Surface:
    def __init__(self, squared_size):
        self.squared_size = squared_size
        self.crater_lst = []
        self.crater_factory = c.CraterFactory()
        self.num_craters = 0
        
    def TakeTimeStep(self):
        self.AddCrater()
        self.PlotSurface()
    
    def AddCrater(self):
        # Create crater
        new_crater = self.crater_factory.CreateCrater(self.squared_size)
        # Add crater
        self.num_craters += 1
        # check for collisions
        for crater in self.crater_lst:
            if (self.isColliding(new_crater, crater)):
                print("Collision!")
                crater.UpdateVisiblePoints(new_crater)
                # Check if crater is erased
                if (crater.isErased()):
                    # Remove crater
                    self.crater_lst.remove(crater)
                    self.num_craters -= 1
                    print('Crater Erased')
        # Add crater last so it doesnt collide with itself
        self.crater_lst.append(new_crater)
        
    def PrintCraterMap(self):
        for i, row in enumerate(self.crater_map):
            print(self.crater_map[i])
    
    def PrintCraterList(self):
        print(self.crater_lst)
        
    def PlotSurface(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.squared_size)
        ax.set_ylim(0, self.squared_size)
        for crater in self.crater_lst:
            circle = plt.Circle((crater.position_x, crater.position_y), crater.radius, fill=True, color = 'gray', alpha=0.5, label='Crater')
            ax.add_patch(circle)
        # Display the plot
        plt.gca().set_aspect('equal', adjustable='box')  # Make sure the aspect ratio is equal
        plt.xlabel('km')
        plt.ylabel('km')
        plt.show()
        
    def isColliding(self, craterA, craterB):
        distance = math.sqrt((craterA.position_x - craterB.position_x)**2 + (craterA.position_y - craterB.position_y)**2)
        sum_radii = craterA.radius + craterB.radius
        return distance <= sum_radii
