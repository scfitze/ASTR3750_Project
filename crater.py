#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:43:21 2023

@author: seanfitze
"""
import numpy as np
import cratersizedistr as cs

class Crater:
    def __init__(self, radius, position_x, position_y, visible):
        self.radius = radius
        self.position_x = position_x
        self.position_y = position_y
        self.visible = visible
        

class CraterFactory:
    def create_crater(self, range):
        """
        

        Returns A new crater
        -------
        TYPE
            Generates a new crater based on size frequency distribution and random position

        """
        radius = cs.random_crater_size()
        return Crater(radius, np.random.randint(0, range), np.random.randint(0, range), True)
   

# cf = CraterFactory()
# crater = cf.create_crater()
# print(crater.radius)
# print(crater.position_x, crater.position_y)
        