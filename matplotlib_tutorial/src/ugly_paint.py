'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-03-14 17:37:11
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-03-14 17:37:16
FilePath: /visualzation/src/ugly_paint.py
Description: 
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved. 
'''
import matplotlib as mlp
mlp.use("Agg")

import matplotlib.pyplot as plt

# Simple data
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 3, 5]

# Basic plot with default settings
plt.plot(x, y)

# Set title and labels with minimal styling
plt.title('Ugly Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Display the plot
plt.savefig("figure/ugly plot.pdf")
