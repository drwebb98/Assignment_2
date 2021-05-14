#To the Max!(...imum Gradient...)

import sys
import csv
import math
import matplotlib
import matplotlib.pyplot
import tkinter
import time
import gui
matplotlib.use('TkAgg')

heights = []
all_slopes = []


# tkinter GUI asking for .txt file input
gui.file_input.file_GUI()
tkinter.mainloop()


# Define file_name from user input
file_name = gui.file_input.file_name


# Retrieve data from .txt file
try:
    f = open(file_name , newline = '\r\n')
except FileNotFoundError:
    print("")
    print("Working file name not entered")
    print("This programme will now end")
    sys.exit()
except TypeError:
    print("")
    print("Working file name not entered")
    print("This programme will now end")
    sys.exit()
    
reader = csv.reader(f, delimiter = ' ')

try:
    for row in reader:    
        if row[-1] == '':
            del row[-1]                     
        heightrows = []
        heights.append(heightrows)                                  
        for value in row:                                       
            heightrows.append(int(float(value)))
except ValueError:
    print("")
    print("Values in .txt file are not formatted correctly")
    print("This programme will now end")
    sys.exit()
    
f.close()    
    

# Timer set for calculations
total_seconds_start = time.perf_counter()


# Calculate Slopes
for i in range(1,len(heights)-1):
    slopes_row = []
    for j in range(1,len(heights)-1):
        slopes = []

# Assign variables to cells surrounding the cell slope is being calculated for
        e = (heights[i][j])
        a = (heights[i-1][j-1])
        b = (heights[i-1][j])
        c = (heights[i-1][j+1])
        d = (heights[i][j-1])
        f = (heights[i][j+1])
        g = (heights[i+1][j-1])
        h = (heights[i+1][j])
        k = (heights[i+1][j+1])
        positions = [a,b,c,d,e,f,g,h,k]
        
        # Calculate slope for adjacent cells
        for adjacent in range(1,len(positions),2):
            
            tan = (e-(positions[adjacent]))/(1)
            rad = math.atan(tan)
            slope_adj = rad*(180/(math.pi))
            if slope_adj < 0:
                slope_adj = slope_adj*(-1)
            slopes.append(slope_adj)
            
        # Calculate slope for non adjacent cells
        for non_adjacent in range(0,len(positions),2):
            if positions == e:
                continue
            
            tan = (e-(positions[non_adjacent]))/(math.sqrt(2))
            rad = math.atan(tan)
            slope_non = rad*(180/(math.pi))
            if slope_non < 0:
                slope_non = slope_non*(-1)
            slopes.append(slope_non)
                                   
        e = max(slopes)
        e = round(e,1)
        slopes_row.append(e)

    all_slopes.append(slopes_row)
   
    

# Timer end   
total_seconds_end = time.perf_counter()
print("Total Calculation Time: " , round((total_seconds_end) - 
(total_seconds_start), 5), "seconds")


# Make heights figure
fig0 = matplotlib.pyplot.figure(figsize=(7,7))
matplotlib.pyplot.imshow(heights, cmap = "gray", vmin=0, vmax=255)


# Make slopes figure
fig1 = matplotlib.pyplot.figure(figsize=(8,8))
matplotlib.pyplot.imshow(all_slopes)
    

# Rename file name without .txt at the end
file_name = file_name[:(len(file_name)-4)]


# tkinter GUI showing outputs
gui.output.maps_GUI(fig0, fig1, all_slopes, file_name)
tkinter.mainloop()
