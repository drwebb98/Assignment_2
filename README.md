# Assignment_2 README
**Assignment 2 GEOG5003M**

Student Number: 201488484

**[max_gradient.py](https://github.com/drwebb98/Assignment_2/blob/main/max_gradient.py) is the core programme.**  
**[gui.py](https://github.com/drwebb98/Assignment_2/blob/main/gui.py) is an imported module containing classes defining the two tkinter GUIs.**

***
This programme can be run within a python shell. 

When the software (max_gradient.py) is run, the user will be asked to input the name of a .txt file containing height data into a GUI created using tkinter. Messages will appear in both the GUI and the python shell to help the user input the correct information.
The programme will then produce two visuals; one of the height data and one showing the maximum gradient for each cell within the same area. These are created within matplotlib and presented within a second GUI.
The main programme is contained within max_gradient.py, with the information on how the two GUIs run being found in a separate imported module (gui.py) found within the same directory.

The inputted file should end in .txt and have spaces (' ') as the delimiters; the programme will otherwise provide error messages if this is not the case (see document on [development and testing](https://github.com/drwebb98/Assignment_2/blob/main/Development%20and%20Testing.txt)).

The original input file this software is based on is [snow_heights.txt](https://github.com/drwebb98/Assignment_2/blob/main/snow_heights.txt).
Other input files of larger sizes have also been provided to show the versatility of this programme: [test1.txt](https://github.com/drwebb98/Assignment_2/blob/main/test1.txt) ; [test2.txt](https://github.com/drwebb98/Assignment_2/blob/main/test2.txt)

***

**Classes, Variables and Functions:**

**max_gradient.py:**

`heights` = Complete height data extracted from a .txt file. Created using `heightrows` and `row`  
`heightrows` = Complete row of height data extracted from a .txt file  
`row` = Single integer height data extracted from a .txt file  
`all_slopes` = Complete slopes data created using `slopes_row`, `slopes_non`, `slopes_adj` and `slopes`  
`slopes_row` = Complete row of slopes data   
`slopes_non` = Calculation of gradients from the non-adjacent cells (`a,c,g,k`)  
`slopes_adj` = Calculation of gradients from the adjacent cells (`b,d,f,h`)  
`slopes` = Slopes data for the eight cells surrounding cell `e`  
`positions` = List of eight cells surrounding cell `e` (`a,b,c,d,f,g,k`)  
`file_name` = Inputted file name taken from `gui.file_input.file_name`  
`save_file_name` = `file_name` with .txt removed from the end of it so that it can be used to name new save files
`fig0` = Figure showing height data  
`fig1` = Figure showing slopes data  
`total_seconds_start` = Start of `time.perfcounter()` to calculate the amount of time the slope calculations take
`total_seconds_end` = End of `time.perfcounter()` to calculate the amount of time the slope calculations take

`e` = Central cell where the maximum gradient is being calculated  
`a,b,c,d,f,g,h,k` = Positions of cells surrounding cell `e`, used to calculate the gradients to/from the central cell (int). Arranged as below.  

a  b  c  
d  e  f  
g  h  k  

**gui.py:**

*class* **`file_input`**:  
`file_name()` = Contains the global variable `file_name` so that it can be implemented across modules and functions  
`enter_button()` = Action of the `entry widget` and associated `enter_name_button` contained within `file_GUI()`. Checks if the inputted file name exists, and if not will alert the user with error messages  
`file_GUI()` = Information stored on the widgets used to create the file input GUI in tkinter  
 
 Widgets within `file_GUI()`:  
`file_name_widget` = The main tkinter GUI frame that the other widgets are built on top of  
`label_widget` = Messages alerting the user if the file inputted is incorrect  
`enter_name_button` = Button to press when the user has inputted a file name  
`entry_widget` = Text box that users type the file name in to  



*class* **`output`**:  
`save_txt_file()` = Action of the `save_txt_button` contained within `maps_GUI()`. Saves the slopes map as a .txt file ending in `_slopes.txt` in the same directory the files are in. Associated positional arguments: `all_slopes` `save_file_name`  
`save_slopes_image()` = Action of the `save_png_button` contained within `maps_GUI()`. Saves the slopes map as a .png image file ending in `_slpoes.png` in the same directory the files are in. Associated positional argument: `save_file_name`  
`exit()` = Action of the `exit_button` contained within `maps_GUI()`. Exits the GUI and ends the programme  
`maps_GUI()` = Information stored on the widgets used to create the output map GUI in tkinter. Associated positional arguments: `fig0` `fig1` `all_slopes` `save_file_name`  

Widgets within `maps_GUI()`:  
`maps_widget` = The main tkinter GUI frame that the other widgets are built on top of  
`canvas1` = Creation of the heights map using data from `fig0` and matplotlib  
`canvas2` = Creation of the slopes map using data from `fig1` and matplotlib. A colourbar is also created here to act as a legend for the map  
`label_widget` = Titles of the two maps: `save_file_name` + "Height Data Map"   and   `save_file_name` + "Maximum Gradient Map"   
`save_txt_button` = Button to press when the user wants to save the slopes map as a .txt file. Runs `save_txt_file()`  
`save_png_button` = Button to press when the user wants to save the slopes map as a .png image file. Runs `save_slopes_image()`  
`exit_button` = Button to press when the user wants to exit the programme. Runs `exit()`

***

For information on software development, testing and references see [this document](https://github.com/drwebb98/Assignment_2/blob/main/Development%20and%20Testing.txt)

***

Known Issues:

* The programme will only work with .txt files that are delimited by spaces (' '). If the .txt files are delimited by other characters (e.g. `,` `;`), then the code will have to be altered (delimiter on line 42 of max_gradient.py).
* The programme will only work if the input file is in the same directory as the two .py module files.


***

Further Development:

* Allow .txt files with different delimiters such as `,` and `;` to work within the programme without altering the code each time it is used.  
* Update the slopes output so that it has values of `NoData` for the cells where the maximum gradient is not calculated. This will make the slopes output map the same size as the original height data input map (it is currently smaller by a one cell boundary on all sides of the map).  
* Create error messages if the user tries to save a file that already exists.  
* Let the user save the maximum gradients output map as different file types and to different locations.  

***

This software is available under the MIT License. See [LICENSE.txt](https://github.com/drwebb98/Assignment_2/blob/main/LICENSE.txt) for more information.

Data used in the creation of test1.txt and test2.txt:  
OS Terrain 50 (ASC geospatial data), Scale 1:50000, Ordnance Survey (GB), Using: EDINA Digimap Ordnance Survey Service
