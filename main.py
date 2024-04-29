# This code is a simple implementation of the bubblesort and quicksort algorithms,
# it also includes a simple GUI and the possibility to run the algorithms multiple times to get an average time.

from enum import Enum

import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk

from sorts import bubble_sort, quicksort, merge_sort

import random

# Increase the recursion limit to avoid RecursionError if needed
import sys
sys.setrecursionlimit(4096)

# Number of times to run the sorting algorithms for an average
iteration_amount = 100
# determines how big the test array is
array_size = 1024


# Enum to specify the type of array to generate
class ArrayType(Enum):
    RANDOM = 0
    PARTIALLY_SORTED = 1
    REVERSE_SORTED = 2


array_mode = ArrayType.REVERSE_SORTED

# Determines how much a sorted array is shuffled before being passed to the sorting algorithm
degree_of_un_sortedness = 0.1


# Function to generate a partially sorted array with n elements and a specified number of swaps
def generate_partially_sorted_array(n, num_swaps=3):
    arr = list(range(1, n + 1))

    # Perform the specified number of swaps
    for _ in range(num_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_random_array(n):
    if array_mode == ArrayType.PARTIALLY_SORTED:
        # Create a partially sorted array
        sortable_arr = generate_partially_sorted_array(n, int(n * degree_of_un_sortedness))
    elif array_mode == ArrayType.RANDOM:
        # Create a 1D numpy array with a random permutation
        sortable_arr = np.random.permutation(n)
    elif array_mode == ArrayType.REVERSE_SORTED:
        # Create a reverse sorted array
        sortable_arr = list(range(n, 0, -1))
    else:
        raise ValueError("Invalid array mode")
    return sortable_arr

# shows a plot of the array


def show_plot(arr_to_plot):
    plt.figure(figsize=(8, 8))
    plt.bar(np.arange(array_size), arr_to_plot)
    plt.show()


# a sort function that accepts the names of any sorting function and the array to sort
def sort_once(sort_function):
    start = time.time()
    sort_function(generate_random_array(array_size))
    end = time.time()
    print(f"{sort_function.__name__} took {end - start:.4f} seconds")


# a sort function that accepts the names of any sorting function and the array to sort executing it n times and
# printing the average time
def average_sort(sort_function):
    start = time.time()
    for i in range(iteration_amount):
        sort_function(generate_random_array(array_size))
    end = time.time()
    print(f"{iteration_amount} {sort_function.__name__}s took {end - start:.4f} seconds")
    print(f"  taking {(end - start) / iteration_amount:.4f} seconds on average")


# The following code creates a simple window with four buttons, this allows to run the sorting algorithms
# make window with size 300x300
root = tk.Tk()
root.geometry("300x300")
root.title("Main Window")

button_bubble = tk.Button(root, text="single bubblesort", command=lambda: sort_once(bubble_sort))
button_bubble_average = tk.Button(root, text=f"{iteration_amount} bubblesort average",
                                  command=lambda: average_sort(bubble_sort))
button_quick = tk.Button(root, text="single quicksort", command=lambda: sort_once(quicksort))
button_bubble_quick = tk.Button(root, text=f"{iteration_amount}x quicksort average",
                                command=lambda: average_sort(quicksort))
button_merge = tk.Button(root, text="single merge sort", command=lambda: sort_once(merge_sort))
button_merge_average = tk.Button(root, text=f"{iteration_amount} merge sort average",
                                 command=lambda: average_sort(merge_sort))
button_quit = tk.Button(root, text="Quit", command=lambda: sys.exit())

# arrange the buttons in a grid
button_bubble.grid(row=0, column=0, padx=10, pady=10)
button_bubble_average.grid(row=0, column=1, padx=10, pady=10)
button_quick.grid(row=1, column=0, padx=10, pady=10)
button_bubble_quick.grid(row=1, column=1, padx=10, pady=10)
button_merge.grid(row=2, column=0, padx=10, pady=10)
button_merge_average.grid(row=2, column=1, padx=10, pady=10)
button_quit.grid(row=3, column=0, columnspan=2, padx=100, pady=100)

# start the main loop of the window
tk.mainloop()
