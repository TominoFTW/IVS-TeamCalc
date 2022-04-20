from tkinter import *
import webbrowser

window = Tk()
window.title("Calculator")

##
#function that opens the manual
def button_help_function():
    webbrowser.open_new('man.pdf')

# defining the "display" of the calculator using a label


label = Label(window, text="", height="2", anchor="se", font="Verdana 20 bold")
label.grid(column=1, row=0, columnspan=6, sticky="nesw")

##
# Global variable with current number
app_num = ""

##
# Global variable for the first operand of math functions
operand1 = 0

##
# Global variable for the second operand of math functions
operand2 = 0

##
# Global variable counter used in funtion "operation"
counter = 0

##
# function that writes the content of a button on to the display
# also stores current number in variable app_num
def button_press(num):
    global app_num
    app_num = app_num+str(num)
    label.configure(text=app_num)

##
# Function that handles all math operations (todo) that happen within the calculator
def button_operation(operand):
    global app_num
    global operand1
    global operand2
    global counter

    if len(app_num) == 0:
        button_clear_command()
        label.configure(text="SYNTAX ERROR")
    elif operand == "=":
        operand2 = float(app_num)
        operand1 += operand2
        label.configure(text=operand1)
        app_num = ""
        counter = 0
        operand2 = 0
        operand1 = 0
    elif operand == "+":
        counter += 1
        if counter >= 2:
            operand2 = float(app_num)
            operand1 += operand2
            app_num = ""
            label.configure(text=operand)
            return
        label.configure(text=operand)
        operand1 = float(app_num)
        app_num = ""




##
# function that deletes the last character from the display
# it also deletes the last
def button_delete_command():
    global app_num
    app_num = app_num[:-1]
    label.configure(text=app_num)

# function that cleares the whole display
def button_clear_command():
    global app_num
    app_num =""
    label.configure(text=app_num)

##
# configuring the weight of columns so we can use "sticky" option in the grid
Grid.rowconfigure(window, 0, weight=1)
for i in range(6):
    Grid.columnconfigure(window, i, weight=1)

##
# defining all buttons on the calculator window

##
# Button 0
# Button with the number 0
# When you press the button, the numbers 0 appears on the display
image = PhotoImage(file="button_img/0.png")
button_0 = Button(window, image=image, borderwidth="0", command=lambda : button_press(0))
button_0.image = image

##
# Button 1
# Button with the number 1
# When you press the button, the number 1 appears on the display
image = PhotoImage(file="button_img/1.png")
button_1 = Button(window, image=image, borderwidth="0", command=lambda : button_press(1))
button_1.image = image

##
# Button 2
# Button with the number 2
# When you press the button, the number 2 appears on the display
image = PhotoImage(file="button_img/2.png")
button_2 = Button(window, image=image, borderwidth="0", command=lambda : button_press(2))
button_2.image = image

##
# Button 3
# Button with the number 3
# When you press the button, the number 3 appears on the display
image = PhotoImage(file="button_img/3.png")
button_3 = Button(window, image=image, borderwidth="0", command=lambda : button_press(3))
button_3.image = image

##
# Button 4
# Button with the number 4
# When you press the button, the number 4 appears on the display
image = PhotoImage(file="button_img/4.png")
button_4 = Button(window, image=image, borderwidth="0", command=lambda : button_press(4))
button_4.image = image

##
# Button 5
# Button with the number 5
# When you press the button, the number 5 appears on the display
image = PhotoImage(file="button_img/5.png")
button_5 = Button(window, image=image, borderwidth="0", command=lambda : button_press(5))
button_5.image = image

##
# Button 6
# Button with the number 6
# When you press the button, the number 6 appears on the display
image = PhotoImage(file="button_img/6.png")
button_6 = Button(window, image=image, borderwidth="0", command=lambda : button_press(6))
button_6.image = image

##
# Button 7
# Button with the number 7
# When you press the button, the number 7 appears on the display
image = PhotoImage(file="button_img/7.png")
button_7 = Button(window, image=image, borderwidth="0", command=lambda : button_press(7))
button_7.image = image

##
# Button 8
# Button with the number
# When you press the button, the number 8 appears on the display
image = PhotoImage(file="button_img/8.png")
button_8 = Button(window, image=image, borderwidth="0", command=lambda : button_press(8))
button_8.image = image

##
# Button 9
# Button with the number 9
# When you press the button, the number 9 appears on the display
image = PhotoImage(file="button_img/9.png")
button_9 = Button(window, image=image, borderwidth="0", command=lambda : button_press(9))
button_9.image = image

##
# Button +
# Button with the operation +
# When you press the button, the the operation + gets carried out
# the + sign appears on the display
image = PhotoImage(file="button_img/+.png")
button_add = Button(window, image=image, borderwidth="0", command=lambda : button_operation("+"))
button_add.image = image

##
# Button -
# Button with the operation -
# When you press the button, the the operation - gets carried out
# the - sign appears on the display
image = PhotoImage(file="button_img/-.png")
button_sub = Button(window, image=image, borderwidth="0", command=lambda : button_operation("-"))
button_sub.image = image

##
# Button *
# Button with the operation *
# When you press the button, the the operation * gets carried out
# the * sign appears on the display
image = PhotoImage(file="button_img/*.png")
button_mul = Button(window, image=image, borderwidth="0", command=lambda : button_operation("*"))
button_mul.image = image

##
# Button /
# Button with the operation /
# When you press the button, the the operation / gets carried out
# the / sign appears on the display
image = PhotoImage(file="button_img/div.png")
button_div = Button(window, image=image, borderwidth="0", command=lambda : button_operation("/"))
button_div.image = image

##
# Button .
# Button with the . sign
# When you press the button, the a decimal point is placed behind your number
# the . sign appears on the display
image = PhotoImage(file="button_img/dot.png")
button_dot = Button(window, image=image, borderwidth="0", command=lambda : button_press("."))
button_dot.image = image

##
# Button abs
# Button with the operation absolute value
# When you press the button, the the operation abs gets carried out
# the abs sign appears on the display
image = PhotoImage(file="button_img/abs.png")
button_abs = Button(window, image=image, borderwidth="0", command=lambda : button_operation("abs"))
button_abs.image = image

##
# Button help
# Button with the help function
# When you press the button, the manual opens
image = PhotoImage(file="button_img/help.png")
button_help = Button(window, image=image, borderwidth="0", command=lambda : button_help_function()) # todo button help function
button_help.image = image

##
# Button !
# Button with the operation !
# When you press the button, the the operation ! gets carried out
# the ! sign appears on the display
image = PhotoImage(file="button_img/!.png")
button_factorial = Button(window,  image=image, borderwidth="0", command=lambda : button_operations("!"))
button_factorial.image = image

##
# Button delete
# Button with the operation delete
# When you press the button, last character placed on the display gets deleted

image = PhotoImage(file="button_img/del.png")
button_delete = Button(window, image=image, borderwidth="0", command=lambda : button_delete_command())
button_delete.image = image

##
# Button clear
# Button with the operation clear
# When you press the button, the whole display of the calculator gets cleared

image = PhotoImage(file="button_img/clear.png")
button_clear = Button(window, image=image, borderwidth="0", command=lambda : button_clear_command())
button_clear.image = image

##
# Button power
# Button with the operation ^
# When you press the button, the the operation ^ gets carried out
# the ^ sign appears on the display
image = PhotoImage(file="button_img/^.png")
button_ToThePower = Button(window, image=image, borderwidth="0", command=lambda : button_operation("^"))
button_ToThePower.image = image

##
# Button square root
# Button with the operation √
# When you press the button, the operation √ gets carried out
# the √ sign appears on the display
image = PhotoImage(file="button_img/√.png")
button_root = Button(window, image=image, borderwidth="0", command=lambda : button_operation("√"))
button_root.image = image

##
# Button equal to
# Button with the operation =
# When you press the button, the operation = gets carried out and the result is displayed
image = PhotoImage(file="button_img/=.png")
button_equals = Button(window, image=image, borderwidth="0", command=lambda : button_operation("="))
button_equals.image = image



##
# placing buttons from calculator into the window

button_0.grid(column=1, row=4, sticky="nesw", columnspan=2)
button_1.grid(column=1, row=3, sticky="nesw", columnspan=1)
button_2.grid(column=2, row=3, sticky="nesw", columnspan=1)
button_3.grid(column=3, row=3, sticky="nesw", columnspan=1)
button_4.grid(column=1, row=2, sticky="nesw", columnspan=1)
button_5.grid(column=2, row=2, sticky="nesw", columnspan=1)
button_6.grid(column=3, row=2, sticky="nesw", columnspan=1)
button_7.grid(column=1, row=1, sticky="nesw", columnspan=1)
button_8.grid(column=2, row=1, sticky="nesw", columnspan=1)
button_9.grid(column=3, row=1, sticky="nesw", columnspan=1)
button_add.grid(column=4, row=1, sticky="nesw", columnspan=1)
button_sub.grid(column=4, row=2, sticky="nesw", columnspan=1)
button_mul.grid(column=4, row=3, sticky="nesw", columnspan=1)
button_div.grid(column=4, row=4, sticky="nesw", columnspan=1)
button_dot.grid(column=3, row=4, sticky="nesw", columnspan=1)
button_abs.grid(column=5, row=2, sticky="nesw", columnspan=1)
button_help.grid(column=6, row=2, sticky="nesw", columnspan=1)
button_delete.grid(column=5, row=1, sticky="nesw", columnspan=1)
button_clear.grid(column=6, row=1, sticky="nesw", columnspan=1)
button_factorial.grid(column=5, row=4, sticky="nesw", columnspan=1)
button_root.grid(column=5, row=3, sticky="nesw", columnspan=1)
button_ToThePower.grid(column=6, row=3, sticky="nesw", columnspan=1)
button_equals.grid(column=6, row=4, sticky="nesw", columnspan=1)

##
# binding specific keys to there correct functions
window.bind("<BackSpace>", lambda event: button_delete_command())



window.mainloop()
