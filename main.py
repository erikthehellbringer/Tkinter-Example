import tkinter
window = tkinter.Tk()
'''
Time convertor using Tkinter :)
Purpose of it is that I was learning GUI at the time. I learned how to position labels, entries(input), button.
Unlike C#, I had to calculate to put these in right order. Since Python doesn't have any Visual Studio Form like designer
interface.
'''
window.title("First GUI Program")
window.minsize(400,200)
window.config(padx=60, pady=60)

#only one function that converts day to hours,minutes and seconds

def button_clicked():
    day = float(input.get())
    hours_number.config(text= day*24)
    minutes_number.config(text=day * 24*60)
    seconds_number.config(text=day * 24*60*60)
#hours label. Had to create the conversion number seperately since it would broke it ???
hours_label = tkinter.Label(text= "Hours")
hours_number= tkinter.Label(text='0')
hours_number.grid(column=1,row=1)
hours_label.grid(column=2,row=1)

#same goes for minutes and seconds
minutes_label = tkinter.Label(text= "minutes")
minutes_number= tkinter.Label(text="0")
minutes_number.grid(column=1, row=2)
minutes_label.grid(column=2,row=2)

seconds_label= tkinter.Label(text= "seconds")
seconds_number = tkinter.Label(text='0')
seconds_number.grid(column=1, row=3)
seconds_label.grid(column=2,row=3)

#days label will be next to entry box
days_label = tkinter.Label(text = "days is equal to")
days_label.grid(column=1, row = 0)

#input entry. justified to center
input = tkinter.Entry(justify= 'center')
input.grid(column=2, row=0)

#button that activates the entry and the function. When the function works the func takes the number from entry puts it to a variable and converts it.
convertor_button = tkinter.Button(text="Calculate", command=button_clicked)
convertor_button.grid(column=3, row=0)
#mainloop that runs the program. Without it the program will work but nothing will show on the screen.
window.mainloop()