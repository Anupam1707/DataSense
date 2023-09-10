import matplotlib.pyplot as plt
import random
from sql_scripts import *

# Function to create and show a bar chart (horizontal or vertical) using .show()
def bar_chart(x_values, y_values, x_axis_label, y_axis_label, title, orientation='vertical'):
    color = ['#{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in x_values]
    fig, ax = plt.subplots(figsize=(8, 4))
    
    if orientation == 'vertical':
        ax.bar(x_values, y_values, color=color)
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
    elif orientation == 'horizontal':
        ax.barh(x_values, y_values, color=color)
        ax.set_xlabel(y_axis_label)
        ax.set_ylabel(x_axis_label)
    
    ax.set_title(title)
    plt.show()

# Function to create a pie chart and display it using .show()
def pie_chart(labels, sizes, title):
    colors = ['#{:02x}{:02x}{:02x}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in sizes]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')
    ax.set_title(title)

    plt.show()
