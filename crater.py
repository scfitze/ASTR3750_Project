#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:43:21 2023

@author: seanfitze
"""
import numpy as np
import cratersizedistr as cs
import math

class Crater:
    def __init__(self, radius, position_x, position_y, visible):
        self.radius = radius
        self.position_x = position_x
        self.position_y = position_y
        self.visible = visible
        self.total_points = 10
        self.rim_points = set(self.GenerateRimPoints(self.total_points)) # points to keep track of rim
        
    def GenerateRimPoints(self, num_points):
        rim_points = []
        for i in range(num_points):
            angle = 2 * math.pi * (i / num_points)
            x_on_rim = self.position_x + self.radius * math.cos(angle)
            y_on_rim = self.position_y + self.radius * math.sin(angle)
            rim_points.append((x_on_rim,y_on_rim))
        return rim_points
    
    def UpdateVisiblePoints(self, crater):
        for point in list(self.rim_points):
            if self.isPointColliding(point, crater):
                self.rim_points.remove(point)
            
    def isPointColliding(self, point, other_crater):
        distance = math.sqrt((point[0] - other_crater.position_x)**2 +(point[1] - other_crater.position_y)**2)
        return distance <= other_crater.radius
    
    def isErased(self, threshold=0.5):
        visibilitiy_percentage = len(self.rim_points)/self.total_points
        return visibilitiy_percentage < threshold
    

class CraterFactory:
    def CreateCrater(self, range):
        """
        

        Returns A new crater
        -------
        TYPE
            Generates a new asteroid based on size frequency distribution and random position

        """
        radius = cs.random_crater_size()
        return Crater(radius, np.random.randint(0, range), np.random.randint(0, range), True)
   
    
# def _generate_rim_points(self, num_points=100):
#         # Generate points around the crater rim
#         rim_points = []
#         for i in range(num_points):
#             angle = 2 * math.pi * (i / num_points)
#             x_on_rim = self.positionx + self.radius * math.cos(angle)
#             y_on_rim = self.positiony + self.radius * math.sin(angle)
#             rim_points.append((x_on_rim, y_on_rim))
#         return rim_points

# TESTS for RimPoints and collisions
# size = 100
# craterA = Crater(10, 50, 50, True)
# craterB = Crater(10, 40, 50, True)
# print(craterA.rim_points)
# fig, ax = plt.subplots()
# ax.set_xlim(0, size)
# ax.set_ylim(0, size) 
# circle = plt.Circle((craterA.position_x, craterA.position_y), craterA.radius, fill=True, color = 'gray', alpha=0.5, label='Crater')
# ax.add_patch(circle)
# circle = plt.Circle((craterB.position_x, craterB.position_y), craterB.radius, fill=True, color = 'gray', alpha=0.5, label='Crater')
# ax.add_patch(circle)
# craterA.UpdateVisiblePoints([craterB])
# print(craterA.isErased())
# for point in craterA.rim_points:
#     circle = plt.Circle((point[0], point[1]), 1, fill=True, color = 'gray', alpha=0.5, label='point')
#     ax.add_patch(circle)

# # Display the plot
# plt.gca().set_aspect('equal', adjustable='box')  # Make sure the aspect ratio is equal
# plt.xlabel('km')
# plt.ylabel('km')
# plt.show()

