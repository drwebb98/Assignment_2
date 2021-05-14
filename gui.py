#GUI
import tkinter
import os
import csv
import matplotlib
import matplotlib.pyplot

class file_input:

    def file_name():
        global file_name
        file_name = []

    def file_GUI():
       
        global file_name_widget
        file_name_widget = tkinter.Tk()
        file_name_widget.wm_title("To the Max!(...imum Gradient...)")
        
        label_widget = tkinter.Label(file_name_widget, text="   Please enter"+
        " the file name containing height data into the box below and then "+
        "press the button below.   ", height = 3)
        label_widget.pack()
        label_widget = tkinter.Label(file_name_widget, text="The file should"+
        " be in the format .txt and have spaces (' ') as the delimiters.")
        label_widget.pack()
        
        enter_name_button = tkinter.Button(file_name_widget, text="Enter", 
        height = 3, width = 10, command= lambda: file_input.enter_button())
        enter_name_button.pack(side = 'bottom')

        global entry_widget
        entry_widget = tkinter.Entry(file_name_widget)
        entry_widget.insert(10, "")
        entry_widget.pack()
        

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
        



class output:
   
    def save_txt_file(all_slopes, file_name):
        f2 = open(file_name +'_slopes.txt', 'w', newline='')
        writer = csv.writer(f2, delimiter=' ')
        for row in all_slopes:
            writer.writerow(row)
        f2.close()
    
        if os.path.isfile(file_name +'_slopes.txt'):
            label_widget = tkinter.Label(maps_widget, text="File Saved as " + 
            file_name + "_slopes.txt")
            label_widget.place(relheight = 0.05, relx = 0.42, rely = 0.9)
            
        else:
            label_widget = tkinter.Label(maps_widget, text="File Not Saved. "+
            "Please Try Again.")
            label_widget.pack()
    
    def exit():
        maps_widget.destroy()

    def maps_GUI(fig0, fig1, all_slopes, file_name):

        global maps_widget
        maps_widget = tkinter.Tk()
        maps_widget.attributes('-fullscreen', True)
        maps_widget.wm_title("To the Max!(...imum Gradient...)")
        
        canvas1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig0, 
        master=maps_widget)
        canvas1._tkcanvas.place(relheight = 1, relwidth = 0.5, relx = 0,
        rely = 0)
        
        canvas2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig1, 
        master=maps_widget)
        canvas2._tkcanvas.place(relheight = 1, relwidth = 0.5, relx = 0.5, 
                                rely = 0)
        matplotlib.pyplot.colorbar(shrink = 0.8, label = "Angle of maximum "+
        "slope in degrees")
        
        save_txt_button = tkinter.Button(maps_widget, text="Save as a .txt"+
        " file", command= lambda: output.save_txt_file(all_slopes, file_name))
        save_txt_button.place(relheight = 0.08, relx = 0.72, rely = 0.9)
        
        exit_button = tkinter.Button(maps_widget,text="EXIT", 
        command= output.exit)
        exit_button.place(relheight = 0.08, relwidth = 0.09, relx = 0.9, 
        rely = 0.01)
        
        








