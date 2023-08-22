"""This program is the Graphing Program of the App."""
import matplotlib.pyplot as plt
import numpy as np

#Function to Plot Horizontal Bar Graph, Vertical Bar Graph and Histogram
def plotb(*ls, t = "bv"):
    xval = []
    yval = []
    fig = plt.figure(figsize = (10, 5))
                     
    if len(ls) == 2:
            xval = ls[0]
            yval = ls[1]
            
            x = ls[0][-1]
            x = x.title()
            y = ls[1][-1]
            y = y.title()
            
            ls[0].remove(ls[0][-1])
            ls[1].remove(ls[1][-1])
    
            #Vertical Bar Graph
            if t == "bv":
                plt.bar(xval, yval, color = "blue")
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Industry Sales Analysis")
                plt.show()
                
            #Horizontal Bar Graph
            elif t == "bh":
                plt.barh(xval, yval, color = "blue")
                plt.xlabel(y)
                plt.ylabel(x)
                plt.title("Industry Sales Analysis")
                plt.show()

#Function to Plot a Pie Chart
def pie(dt):
    labels = dt.keys()
        
    y = np.array(list(dt.values))
    mylabels = labels
    plt.pie(y, labels = mylabels)
    plt.show()
