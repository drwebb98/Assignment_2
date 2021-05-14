# Assignment_2 README
**Assignment 2 GEOG5003M**

**[max_gradient.py](https://github.com/drwebb98/Assignment_2/blob/main/max_gradient.py) is the core programme.**  
**[gui.py](https://github.com/drwebb98/Assignment_2/blob/main/gui.py) is an imported module containing classes defining the two tkinter GUIs.**

***
This programme can be run within a python shell. 

When the software is run, the user will be asked to input the name of a .txt file containing height data into a GUI created using tkinter. Messages will appear in both the GUI and the python shell to help the user input the correct information.
The programme will then produce two visuals; one of the height data and one showing the maximum gradient for each cell within the same area. These are created within matplotlib and presented within a second GUI.
The main programme is contained within max_gradient.py, with the information on how the two GUIs run being found in a separate imported module (gui.py) found within the same directory.

The inputted file should end in .txt and have spaces (' ') as the delimiters; the programme will otherwise provide error messages if this is not the case (see document on [development and testing](https://github.com/drwebb98/Assignment_2/blob/main/Development%20and%20Testing.txt)).

The original input file this software is based on is [snow_heights.txt](https://github.com/drwebb98/Assignment_2/blob/main/snow_heights.txt).
Other input files of larger sizes have also been provided to show the versatility of this programme: [test1.txt](https://github.com/drwebb98/Assignment_2/blob/main/test1.txt) ; [test2.txt](https://github.com/drwebb98/Assignment_2/blob/main/test2.txt)

***

**Variables:**

max_gradient.py:

`heights` = Complete height data extracted from a .txt file. Created using `heightrows` and `row`  
`heightrows` = Complete row of height data extracted from a .txt file  
`row` = Height data extracted from a .txt file  
`all_slopes` = Complete slopes data created using `slopes_row`, `slopes_non`, `slopes_adj` and `slopes`  
`slopes_row` = Complete row of slopes data   
`slopes_non` = Calculation of gradients from the non-adjacent cells (a,c,g,k)  
`slopes_adj` = Calculation of gradients from the adjacent cells (b,d,f,h)  
`slopes` = Slopes data for the eight cells surrounding cell `e`  
`positions` = List of eight cells surrounding cell `e` (a,b,c,d,f,g,k)  
`file_name` = Inputted file name taken from `gui.file_input.file_name`  
`fig0` = Figure showing height data  
`fig1` = Figure showing slopes data  

`a,b,c,d,f,g,h,k` = Positions of cells surrounding cell `e`, used to calculate the gradients to/from the central cell (int). Arranged as below.  
`e` = Central cell where the maximum gradient is being calculated  

a  b  c  
d  e  f  
g  h  k  

gui.py:

*class* `file_input`:


*class* `output`:

***

For information on software development, testing and references see [this document](https://github.com/drwebb98/Assignment_2/blob/main/Development%20and%20Testing.txt)))

***

Known Issues:

* The programme will only work with .txt files that are delimited by spaces (' '). If the .txt files are delimited by other characters (e.g. `,` `;`), then the code will have to be altered (delimiter on line 40 of max_gradient.py).


***

Further Development:

* Allow .txt files with different delimiters such as `,` and `;` to work within the programme.  
* Update the slopes output so that it has values of `NoData` for the cells where the maximum gradient is not calculated. This will make the slopes output map the same size as the original height data input map.  
* Add buttons to save the heights and slopes maps as gifs.

***

This software is available under the MIT License. See [LICENSE.txt](https://github.com/drwebb98/Assignment_2/blob/main/LICENSE.txt) for more information.

Data used in the creation of test1.txt and test2.txt:  
OS Terrain 50 (ASC geospatial data), Scale 1:50000, Ordnance Survey (GB), Using: EDINA Digimap Ordnance Survey Service

