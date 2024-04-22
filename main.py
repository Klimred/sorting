# This code is a simple implementation of the bubblesort and quicksort algorithms,
# it also includes a simple GUI and the possibility to run the algorithms multiple times to get an average time.

import sys

import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk

# Increase the recursion limit to avoid RecursionError if needed
import sys
# sys.setrecursionlimit(2048)

# Create the main window


# Create a 1D numpy array of 1024 elements with a random permutation
unsorted_arr = np.random.permutation(1024)


def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(1, i, 1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


# Quicksort implementation from
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# using the first element as the pivot
def quicksort(arr):
    # if the array is empty or has only one element, no sorting is needed
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # put all elements smaller than the pivot in the
        # left array and all elements greater in the right array
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        # call quicksort recursively on the left
        # and right arrays and concatenate the results
        return quicksort(left) + [pivot] + quicksort(right)


# shows a plot of the array


def show_plot(arr_to_plot):
    plt.figure(figsize=(8, 8))
    plt.bar(np.arange(len(unsorted_arr)), arr_to_plot)
    plt.show()


def bubble_once():
    start = time.time()
    sorted_arr = bubble_sort(unsorted_arr.copy())
    end = time.time()
    print(f"Bubblesort took {end - start} seconds")


def bubble_average():
    iteration_amount = 100
    start = time.time()
    for i in range(iteration_amount):
        sorted_arr = bubble_sort(unsorted_arr.copy())
    end = time.time()
    print(f"Bubble sorts took {end - start} seconds")
    print(f"    taking {(end - start) / iteration_amount} seconds on average")


def quick_once():
    start = time.time()
    sorted_arr = quicksort(unsorted_arr.copy())
    end = time.time()
    print(f"Quicksort took {end - start} seconds")


def quick_average():
    iteration_amount = 100
    start = time.time()
    for i in range(iteration_amount):
        sorted_arr = quicksort(unsorted_arr.copy())
    end = time.time()
    print(f"Quick sorts took {end - start} seconds")
    print(f"    taking {(end - start) / iteration_amount} seconds on average")


# The following code creates a simple window with four buttons, this allows to run the sorting algorithms
# make window with size 300x300
root = tk.Tk()
root.geometry("300x300")
root.title("Main Window")

button_bubble = tk.Button(root, text="single bubblesort", command=lambda: bubble_once())
button_bubble_average = tk.Button(root, text="100x bubblesort average", command=lambda: bubble_average())
button_quick = tk.Button(root, text="single quicksort", command=lambda: quick_once())
button_bubble_quick = tk.Button(root, text="100x quicksort average", command=lambda: quick_average())
button_quit = tk.Button(root, text="Quit", command=lambda: sys.exit())

# arrange the buttons in a grid
button_bubble.grid(row=0, column=0, padx=10, pady=10)
button_bubble_average.grid(row=0, column=1, padx=10, pady=10)
button_quick.grid(row=1, column=0, padx=10, pady=10)
button_bubble_quick.grid(row=1, column=1, padx=10, pady=10)
button_quit.grid(row=2, column=0, columnspan=2, padx=100, pady=100)

# start the main loop of the window
tk.mainloop()


