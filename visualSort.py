import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import numpy as np

class SortVisualization:
    def __init__(self, data, axes):
        self.data = data
        self.initial_data = data.copy()
        self.x = np.arange(0, len(data), 1)
        self.axes = axes

    def bubbleSort(self, event):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.update_plot()
    
    def insertionSort(self, event):
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j = j - 1
                self.update_plot()
            self.data[j + 1] = key
            self.update_plot()

    def selectionSort(self, event):
        n = len(self.data)
        for i in range(n):
            minIndex = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[minIndex]:
                    minIndex = j
                    
            (self.data[i], self.data[minIndex]) = (self.data[minIndex], self.data[i])
            self.update_plot()

    def mergeSort(self, event):
        pass
    
    def resetGraph(self, event):
        self.data = self.initial_data.copy()
        self.update_plot()

    def update_plot(self):
        self.axes.clear()
        self.axes.bar(self.x, self.data)
        plt.pause(0.001)


def main():
    button1 = "Selection Sort"
    button2 = "Bubble Sort"
    button3 = "Insertion Sort"
    amount = 25
    data = np.random.randint(0, 100, amount)
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, amount)
    ax.set_ylim(0, 100)
    sort_visualization = SortVisualization(data, ax)
    
    plt.subplots_adjust(bottom=0.3)
    #size_radio = plt.axes([0.1, 0.2, 0.3, 0.05]) 
    size_input = plt.axes([0.17, 0.05, 0.08, 0.07])
    size_reset = plt.axes([0.27, 0.05, 0.15, 0.07])
    size_selection = plt.axes([0.43, 0.05, 0.15, 0.07])
    size_bubble = plt.axes([0.59, 0.05, 0.15, 0.07])
    size_insertion = plt.axes([0.75, 0.05, 0.15, 0.07])

    #radio_buttons = RadioButtons(size_radio, ("Ascending", "Descending"), active=0)
    input_box = TextBox(size_input, "Amount: ", initial=str(amount))
    reset_button = Button(size_reset, "Reset Graph", color="green", hovercolor="red")
    selection_button = Button(size_selection, button1, color="green", hovercolor="red")
    bubble_button = Button(size_bubble, button2, color="green", hovercolor="red")
    insertion_button = Button(size_insertion, button3, color="green", hovercolor="red")

    def update_amount(text):
        nonlocal amount
        amount = int(text)
        new_data = np.random.randint(0, 100, amount)
        sort_visualization.data = new_data
        sort_visualization.initial_data = new_data.copy()
        sort_visualization.x = np.arange(0, len(new_data), 1)
        sort_visualization.update_plot()
    
    input_box.on_submit(update_amount)
    reset_button.on_clicked(sort_visualization.resetGraph)
    selection_button.on_clicked(sort_visualization.selectionSort)
    bubble_button.on_clicked(sort_visualization.bubbleSort)
    insertion_button.on_clicked(sort_visualization.insertionSort)
    
    plt.show()

main()