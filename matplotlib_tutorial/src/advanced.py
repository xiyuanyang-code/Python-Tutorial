'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-03-14 14:53:43
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-03-14 21:42:43
FilePath: /python_visualization_templates/src/advanced.py
Description: 
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved. 
'''
import matplotlib as mlp
mlp.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

np.random.seed(2024)


plt.rcParams['font.family'] = 'Serif'
plt.rcParams['font.size'] = 12
font = FontProperties(fname="/home/xiyuanyang/.local/share/fonts/georgia.ttf")
# Generating data
X = np.linspace(0, 10 ,5000)

# Define the linear relation
# The relation: y = k * x + b
k = 2.0
b = 2.0

# Generating the true value of Y
Y_true = k * X + b

# Adding noise
noise = np.random.normal(0, 3, size=Y_true.shape)
Y_noise = Y_true + noise

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x=X, y=Y_noise, color='red', label='Noisy data', alpha=0.3, s=5)
# plt.plot(X, Y_true, color='blue', label="Real Data", linewidth=3)
plt.title("Linear Relations with noise", fontproperties = font, fontsize = 18)
plt.xlabel("X values")
plt.ylabel("Y values (with noise)")
plt.legend()
plt.savefig("figure/Advanced.pdf")
plt.close()