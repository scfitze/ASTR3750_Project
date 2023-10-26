#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:08:20 2023

@author: seanfitze, juliajohnston
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate random center coordinates (x, y) within a specified range
x_center = np.random.uniform(0, 10)  # Adjust the range as needed
y_center = np.random.uniform(0, 10)  # Adjust the range as needed

# Generate a random radius for the circle
radius = np.random.uniform(0.5, 2.0)  # Adjust the range as needed

# Create a figure and axis
fig, ax = plt.subplots()
# Plot the circle
circle = plt.Circle((x_center, y_center), radius, fill=True, color='gray', label='Crater')
ax.add_patch(circle)


# Set axis limits
ax.set_xlim(0, 10)  # Adjust the limits as needed
ax.set_ylim(0, 10)  # Adjust the limits as needed

# Label the axes
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Add a legend
plt.legend()

# Display the plot
plt.gca().set_aspect('equal', adjustable='box')  # Make sure the aspect ratio is equal
plt.show()