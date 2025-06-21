'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-03-14 22:03:46
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-03-14 22:19:31
FilePath: /python_visualization_templates/src/fonts.py
Description: This is the demo of customizing fonts.
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved. 
'''
def draw_scatter(X=[1,2,3,4], y=[10,20,-10,50], fontsize=12, filepath="figure/my images.png",
                title="My title", lable="my label", x_lable="Xlable", y_lable="Ylabel", 
                ):
    # import modules

    # Modifying the backend of matplotlib
    import matplotlib as mlp
    mlp.use("Agg")

    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.font_manager import FontProperties

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams['font.size'] = fontsize

    # ! Attention
    # Change to your own locations
    font_geogria = FontProperties(fname="/home/xiyuanyang/.local/share/fonts/georgia.ttf")
    font_sonti = FontProperties(fname="/home/xiyuanyang/.local/share/fonts/songti.ttc")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x=X, y=y, color='red', label=lable, alpha=0.3, s=5)
    plt.title(title, fontproperties = font_geogria, fontsize = 18)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.legend()

    # ! Attention, suggest you to use the absolute path.
    plt.savefig(filepath)
    plt.close()

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)  # Create a DataFrame
iris_data['species'] = iris.target  # Add the target variable

# Extract features for plotting
X = iris_data['sepal length (cm)'].values  # Using sepal length as X
y = iris_data['sepal width (cm)'].values    # Using sepal width as y


# Call the draw_scatter function with the Iris data
draw_scatter(
    X=X, 
    y=y, 
    fontsize=12, 
    filepath="figure/iris_scatter.png",  # Ensure this directory exists
    title="Iris Dataset Scatter Plot", 
    lable="Sepal Points", 
    x_lable="Sepal Length (cm)", 
    y_lable="Sepal Width (cm)"
)
