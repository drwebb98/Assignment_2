#GUI
import tkinter
import os
import csv
import matplotlib
import matplotlib.pyplot
import matplotlib.image


# Creation of first GUI asking for file name input
class file_input:

    # Global variable so file_name can be used across modules
    def file_name():
        global file_name
        file_name = []

    # Creation of main GUI and widgets
    def file_GUI():
       
        global file_name_widget
        file_name_widget = tkinter.Tk()
        file_name_widget.wm_title("To the Max!(...imum Gradient...)")

        # Instructions on what to do
        label_widget = tkinter.Label(file_name_widget, text="   Please enter"+
        " the file name containing height data into the box below and then "+
        "press the button below.   ", height = 3)
        label_widget.pack()
        label_widget = tkinter.Label(file_name_widget, text="The file should"+
        " be in the format .txt and have spaces (' ') as the delimiters.")
        label_widget.pack()

        # Button to submit input
        enter_name_button = tkinter.Button(file_name_widget, text="Enter", 
        height = 3, width = 10, command= lambda: file_input.enter_button())
        enter_name_button.pack(side = 'bottom')

        # Text box for user to type file name
        global entry_widget
        entry_widget = tkinter.Entry(file_name_widget)
        entry_widget.insert(10, "")
        entry_widget.pack()
             
    # Action of enter_name_button with error messages to prevent code breaking        
    def enter_button():

        file_input.file_name = entry_widget.get()
        os.path.exists(file_input.file_name)
        if os.path.isfile(file_input.file_name):
            print (file_input.file_name + " Loaded")
            file_name_widget.destroy()
        elif len(file_input.file_name) == 0:
            print ("No file input detected, please try again")
            error1_widget = tkinter.Label(file_name_widget, text="No file" +
            " input detected, please try again")
            error1_widget.pack()
        elif ".txt" not in file_input.file_name:
            print("File type incorrect, please try again")
            error2_widget = tkinter.Label(file_name_widget, text="File type "+
            "incorrect, please try again")
            error2_widget.pack()
        else:
            print(".txt file not found in this directory, please try again")
            error3_widget = tkinter.Label(file_name_widget, text=".txt file "+
            "not found in this directory, please try again")
            error3_widget.pack()
        


# Creation of second GUI where output is produced
class output:
   
    # Save file as a .txt file, message to tell user file has been saved
    def save_txt_file(all_slopes, save_file_name):
        f2 = open(save_file_name +'_slopes.txt', 'w', newline='')
        writer = csv.writer(f2, delimiter=' ')
        for row in all_slopes:
            writer.writerow(row)
        f2.close()
    
        if os.path.isfile(save_file_name +'_slopes.txt'):
            label_widget = tkinter.Label(maps_widget, text="File Saved as " + 
            save_file_name + "_slopes.txt", bg = 'white', anchor = 'center')
            label_widget.pack(side = 'bottom')
            
        else:
            label_widget = tkinter.Label(maps_widget, text="File Not Saved. "+
            "Please Try Again.", bg = 'white', anchor = 'center')
            label_widget.pack(side = 'bottom')

    # Save file as a .png image file, message to tell user file has been saved
    def save_slopes_image(save_file_name):
        matplotlib.pyplot.savefig(save_file_name +'_slopes.png' ,dpi = 500, 
        bbox_inches = 'tight')
        
        if os.path.isfile(save_file_name + '_slopes.png'):
            label_widget = tkinter.Label(maps_widget, text="File Saved as " + 
            save_file_name + "_slopes.png", bg = 'white', anchor = 'center')
            label_widget.pack(side = 'bottom')
            
        else:
            label_widget = tkinter.Label(maps_widget, text="File Not Saved. "+
            "Please Try Again.", bg = 'white', anchor = 'center')
            label_widget.pack(side = 'bottom')
    
    # Exit command to leave the GUI and end the programme
    def exit():
        maps_widget.destroy()

    # Creation of main GUI and widgets
    def maps_GUI(fig0, fig1, all_slopes, save_file_name):

        global maps_widget
        maps_widget = tkinter.Tk()
        maps_widget.attributes('-fullscreen', True)
        maps_widget.wm_title("To the Max!(...imum Gradient...)")

        # Map of height data
        canvas1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig0, 
        master=maps_widget)
        canvas1._tkcanvas.place(relheight = 1, relwidth = 0.5, relx = 0,
        rely = 0)

        # Map of maximum gradients data and associated legend
        canvas2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig1, 
        master=maps_widget)
        canvas2._tkcanvas.place(relheight = 1, relwidth = 0.6, relx = 0.45, 
                                rely = 0)
        matplotlib.pyplot.colorbar(shrink = 0.8, label = "Angle of maximum "+
        "slope in degrees")

        # Map titles
        label_widget = tkinter.Label(maps_widget, text= save_file_name +
            " Height Data Map", bg = 'white', font = ('bold', 12))
        label_widget.place(relheight = 0.05, relx = 0.18, rely = 0.08)
        label_widget = tkinter.Label(maps_widget, text= save_file_name +
            " Maximum Gradient Map", bg = 'white', font = ('bold',12))
        label_widget.place(relheight = 0.05, relx = 0.6, rely = 0.08)
                
        # Button to save maximum gradient output as a .txt file
        save_txt_button = tkinter.Button(maps_widget, text="Save as a .txt"+
        " file", command= lambda: output.save_txt_file(all_slopes, 
        save_file_name))
        save_txt_button.place(relheight = 0.08, relx = 0.75, rely = 0.9)

        # Button to save maximum gradient output as a .png image file
        save_png_button = tkinter.Button(maps_widget, text="Save as a .png"+
        " file", command= lambda: output.save_slopes_image(save_file_name))
        save_png_button.place(relheight = 0.08, relx = 0.6, rely = 0.9)
        
        # Button to exit the programme
        exit_button = tkinter.Button(maps_widget,text="EXIT", 
        command= output.exit)
        exit_button.place(relheight = 0.08, relwidth = 0.09, relx = 0.9, 
        rely = 0.01)
        
        