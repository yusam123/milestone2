import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
from flask import Flask, render_template
def draw(name,age,weight,height):
    path = 'plot.png'
    bmi = weight/height/height*703
    bmi = round(bmi,2)
    # Create a bar chart of the user's age, weight, height, and BMI
    labels = ['Age', 'Weight', 'Height', 'BMI']
    values = [age, weight, height, bmi]

    plt.bar(labels, values)

    # Add axis labels and title
    plt.xlabel('Measurement')
    plt.ylabel('Value')
    plt.title(f"{name}'s Age, Weight, Height, and BMI")
    # Add labels to the bars
    for i in range(len(labels)):
        plt.text(x=i, y=values[i], s=values[i], ha='center', va='bottom')
    plt.savefig(path, format='png')
    plt.close()
    return path

