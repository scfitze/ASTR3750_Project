#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:08:20 2023

@author: seanfitze, juliajohnston
"""

import matplotlib.pyplot as plt
import numpy as np
import surface as s

class Project:
    def __init__(self, surface):
        self.surface = surface
        self.crater_frequency = []
        self.timesteps = []
            
    def PlotCraterFrequency(self):
        plt.plot(self.timesteps, self.crater_frequency, label='Crater Frequency')
        plt.xlabel('time Step (1000 years)')
        plt.ylabel('Crater Frequency')
        plt.title('Crater Frequency Over Time')
        plt.legend()
        plt.show()
        
    def RunSim(self):
        for i in range(200):
            self.surface.TakeTimeStep()
            self.crater_frequency.append(self.surface.num_craters)
            self.timesteps.append(i)
        self.PlotCraterFrequency()
        # print(self.surface.crater_lst)
            
            
# Test sim            
p = Project(s.Surface(100))
p.RunSim()