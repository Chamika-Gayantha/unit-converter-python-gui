import tkinter as tk  #tkinter use to Create GUI(windows,buttons..etc)
from tkinter import ttk, messagebox #ttk gives the Advaced widgets and msgBox shows Pop up Message
from PIL import Image, ImageTk


root = tk.Tk()                 #Create the Window
root.title("Unit Converter")   #Window's name
root.geometry("400x250")       #sets size (width x height)

img = Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Python\converter\bg.jpg")   # put the BG image
img = img.resize((400, 250))
bg = ImageTk.PhotoImage(img)



conversion_dict = {        #This Is  Dictionery used to Collection of Options
    "KM → Miles": lambda x: x * 0.621371,
    "Miles → KM": lambda x: x / 0.621371,
    "°C → °F": lambda x: (x * 9/5) + 32,   # lambda is quick function 
    "°F → °C": lambda x: (x - 32) * 5/9,   #like this function
    "KG → LBS": lambda x: x * 2.20462,     #  def convert(x):
    "LBS → KG": lambda x: x / 2.20462,     #    return x * 2.20462
    "Meters → Feet": lambda x: x * 3.28084,
    "Feet → Meters": lambda x: x / 3.28084,
    "Liters → Gallons": lambda x: x * 0.264172,
    "Gallons → Liters": lambda x: x / 0.264172
}



bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(root, text="Enter Value:").pack(pady=5)  #show text on the window,Enter Value
entry_value = tk.Entry(root)    #Entry-> Gives User inputs
entry_value.pack(pady=5) #pady=5 used to create space,pady means set the space vertical,padx means set the space horizatal

tk.Label(root, text="Select Conversion:").pack(pady=5)
combo = ttk.Combobox(root, values=list(conversion_dict.keys())) # takes all kes from dic,and ahowa all data as dropdown option
combo.pack(pady=5)

def convert():
    try:
        value = float(entry_value.get())  #get text from user input box
        func = conversion_dict[combo.get()] # get falue form dropdown box
        result = func(value)
        label_result.config(text=f"Result: {result:.2f}") #update the last label text
    except ValueError: #these are error handling
        messagebox.showerror("Invalid Input", "Please enter a valid number")
    except KeyError:
        messagebox.showerror("Select Conversion", "Please select a conversion type")

btn_convert = tk.Button(root, text="Convert", command=convert) #Creates button,When clicked -> runs convert() function
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="Result: ",font=("Arial", 14, "bold"),fg="black") #dispaly the op
label_result.pack(pady=10)

root.mainloop() #Keeps window open,Without this -> window closes immediately