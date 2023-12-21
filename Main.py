#Modules / Packages / Libraries
import tkinter as tk
from tkinter import *
from tkinter import StringVar, OptionMenu
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
from PIL import ImageTk, Image

import re
import random
from random import randint
import datetime
import subprocess

#Indexes
list_box_i = 1
i = 0

#Dictionary
orders = {}
orders[i] = {}

#Variable declaration and initialization
global root

global Name
Name = None 

global ChosenFlavor
ChosenFlavor = None

ForSize = None

global size_price
size_price = None

global ChosenAddOns
ChosenAddOns = None

global addprc
addprc = None

global items
items = None

global subtotal
subtotal = None

global TOTAL
TOTAL = None

global PAYMENT
PAYMENT = None

global CHANGE
CHANGE = None

global REWARD
REWARD = None

global RESIBO
RESIBO = None

global num_input
num_input = None

qty_click_flag = False
payment_click_flag = False

#Functions
def text_input(text):
    #Restriced characters to a string type character and 30 character limit 
    return ((text.isalpha() or text.isspace()) and len(username.get()) <= 30) or text == ""

    #Flavors
def flavor_selection():
    global ChosenFlavor  
    ChosenFlavor = Flavors.get()

    if ChosenFlavor == 'Milky Way (Vanilla)':
        flavor1 = 'Milky Way (Vanilla)'
        ChosenFlavor = flavor1

        print("Flavor:",flavor1)
        Item_Column.delete(list_box_i-1, tk.END)
        Item_Column.insert(list_box_i, ChosenFlavor)
        print()
        
    elif ChosenFlavor == 'Mars (Chocolate)':
        flavor2 = 'Mars (Chocolate)'
        ChosenFlavor = flavor2
        
        print("Flavor:",flavor2)
        Item_Column.delete(list_box_i-1, tk.END)
        Item_Column.insert(list_box_i, ChosenFlavor)
        print()
                      
    elif ChosenFlavor == 'Dreamy Banana Split (Special)':
        flavor3 = 'Dreamy Banana Split (Special)'
        ChosenFlavor = flavor3
        
        print("Flavor:",flavor3)
        Item_Column.delete(list_box_i-1, tk.END)
        Item_Column.insert(list_box_i, ChosenFlavor)
        print()
        
    elif ChosenFlavor == 'Solar System (Assorted)':
        flavor4 = 'Solar System (Assorted)'
        ChosenFlavor = flavor4

        print("Flavor:",flavor4)
        Item_Column.delete(list_box_i-1, tk.END)
        Item_Column.insert(list_box_i, ChosenFlavor)
        print()
        
    else:
        messagebox.showwarning('Oops!', 'Something went wrong')

    orders[i]["flavor"] = ChosenFlavor

    #Size
def size_selection(ForSize):
    global ChosenSize
    global size_price

    if ForSize == 'Dwarf (S): ₱20':
        #Code for Dwarf (Small) size selection
        size1 = 'Dwarf (S): ₱20'
        ChosenSize = size1

        price1 = 20
        size_price = price1

        print("Size:",size1)
        Price1_Column.delete(list_box_i-1, tk.END)
        Price1_Column.insert(list_box_i, ChosenSize)
        print()
                                    
    elif ForSize == 'Terra (M): ₱40':
        # Code for Terra (Medium) size selection
        size2 = 'Terra (M): ₱40'
        ChosenSize = size2

        price2 = 40
        size_price = price2

        print("Size:",size2)
        Price1_Column.delete(list_box_i-1, tk.END)
        Price1_Column.insert(list_box_i, ChosenSize)
        print()
       
    elif ForSize == 'Titan (L): ₱65':
        # Code for Titan (Large) size selection
        size3 = 'Titan (L): ₱65'
        ChosenSize = size3

        price3 = 65
        size_price = price3

        print("Size:",size3)
        Price1_Column.delete(list_box_i-1, tk.END)
        Price1_Column.insert(list_box_i, ChosenSize)
        print()
        
    elif ForSize == 'Sizes:':
        print("Error, please choose a Size")
        Price1_Column.delete(list_box_i-1, tk.END)
       
    else:
        messagebox.showwarning('Oops!', 'Something went wrong')

    orders[i]["size"] = ChosenSize
    orders[i]["price"] = size_price

    #Add-ons
def addOns_selection():
    global ChosenAddOns
    global addprc
    ChosenAddOns = AddOns.get()

    if ChosenAddOns == 'Nips':
        AddOn1 = 'Nips'
        ChosenAddOns = AddOn1

        price1 = 10
        addprc = price1
        
        print("Add-on:",AddOn1)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()
            
    elif ChosenAddOns == 'ChocoChips':
        AddOn2 = 'ChocoChips'
        ChosenAddOns = AddOn2

        price2 = 10
        addprc = price2

        print("Add-on:",AddOn2)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()
              
    elif ChosenAddOns == 'Sprinkles':
        AddOn3 = 'Sprinkles'
        ChosenAddOns = AddOn3

        price3 = 10
        addprc = price3

        print("Add-on:",AddOn3)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()
            
    elif ChosenAddOns == 'Mallows':
        AddOn4 = 'Mallows'
        ChosenAddOns = AddOn4

        price4 = 10
        addprc = price4

        print("Add-on:",AddOn4)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()

    elif ChosenAddOns == 'Nuts':
        AddOn5 = 'Nuts'
        ChosenAddOns = AddOn5

        price5 = 10
        addprc = price5

        print("Add-on:",AddOn5)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()

    elif ChosenAddOns == 'Cherry':
        AddOn6 = 'Cherry'
        ChosenAddOns = AddOn6

        price6 = 10
        addprc = price6

        print("Add-on:",AddOn6)
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()

    elif ChosenAddOns == 'NoAddOns':
        AddOn7 = 'NoAddOns'
        ChosenAddOns = AddOn7

        price0 = 0
        addprc = price0

        print("No Add On")
        Add_On_Column.delete(list_box_i-1, tk.END)
        Add_On_Column.insert(list_box_i, ChosenAddOns)
        print()

        
    else:
        messagebox.showwarning('Oops!', 'Something went wrong')
        

    orders[i]["addon"] = ChosenAddOns
    orders[i]["addprc"] = addprc

#Home
def Home():
    global home_triggered
    home_triggered = messagebox.askyesno('Confirmation', 'Do you wish to return back to login?')

    if home_triggered == True:
        root.withdraw()
        subprocess.Popen(["login.py"], shell=True)

    else:
        return
#Submit()
def Submit():
    global Name
    global i
    global items
    global subtotal
    global addprc
    global size_price
    items = num_items.get()
    Name = username.get()
    
    #Input validation
    if Name == None or Name == '':
        messagebox.showwarning('INVALID', 'Please input a name')
        
    elif Flavors.get() == "0" or ChosenFlavor == None or ChosenFlavor == '0':
        messagebox.showwarning('INVALID', 'Please Choose a flavor')

    elif Selected_Option.get() == 'Sizes:':
        messagebox.showwarning('INVALID', 'Please Choose a size')

    elif AddOns.get() == "0" or ChosenAddOns == None or ChosenAddOns == '0':
        messagebox.showwarning('INVALID', 'Please Choose an add-on')

    elif items == None or items == '' or items == "0":
        messagebox.showwarning('INVALID', 'Please input an amount atleast 1')
        
    else:
        are_you_sure = messagebox.askyesno('Confirmation', 'Do you wish to continue?')

        if are_you_sure == True:
            print(ChosenSize)
            print("Customer's Name:",Name)
            orders[i]["quantity"] = items
                
            subtotal1 = float(size_price) + float(addprc)
            subtotal = subtotal1 * float(items) 

            orders[i]["price"] = subtotal

            print()
            loop_order()

        if are_you_sure == False:
            return

def undo():
    global prompt_undo
    global list_box_i
    global qty_click_flag
    global i

    #Decrement the listbox
    list_box_i -= 1
    prompt_undo = messagebox.askyesno('Confirmation', 'Do you want to go back to the previous set of ice cream of your order?')

    if prompt_undo == True:
        #Decrement the order index
        i -= 1

        if list_box_i == 1:
            Undo.configure(state='disable')
            num_items.set("0")
            qty_click_flag = False
            Item_Column.delete(0, END)
            Price1_Column.delete(0, END)
            Add_On_Column.delete(0, END)
            Quantity_Column.delete(0, END)
            Price2_Column.delete(0, END)
                 
        else:
            #Delete the item based on listbox
            Item_Column.delete(list_box_i-1, END)
            Price1_Column.delete(list_box_i-1, END)
            Add_On_Column.delete(list_box_i-1, END)
            Quantity_Column.delete(list_box_i-1, END)
            Price2_Column.delete(list_box_i-1, END)
        
        #Reset previous input when back
        num_items.set(items)
        Flavors.set(ChosenFlavor)
        print(ChosenFlavor)
        Selected_Option.set(ChosenSize)
        print(Selected_Option.get())
        AddOns.set(ChosenAddOns)
        print(ChosenAddOns)

        #Recalibration of values for decremented dictionary
        orders[i]["price"] = subtotal
        orders[i]["addon"] = ChosenAddOns
        orders[i]["addprc"] = addprc
        orders[i]["size"] = ChosenSize
        orders[i]["price"] = size_price
        orders[i]["flavor"] = ChosenFlavor
    
    elif prompt_undo == False:
        #increment the decremented listbox value to return the current listbox value
        list_box_i +=1

def void():
    confirmation = messagebox.askyesno("CONFIRMATION.", "Do you want to reset the current order? The whole current data will be lost.")
    
    if confirmation == True:
        global list_box_i
        global i
        global orders
        global qty_click_flag
        global payment_click_flag
        
        #Reset dictionary
        orders[i].clear()

        #Reset index values
        list_box_i = 1
        i = 0
        orders = {}
        orders[i] = {}
        
        #Reset on click state to false
        qty_click_flag = False
        payment_click_flag = False
        print("ADMIN: Dictionary Cleared. Reset to 0")
        
        #Reset input states
        Customer_Name_Entry.configure(state='normal')
        username.set("")
        Customer_Name_Entry.delete(0,END)
        print("ADMIN: Customer Name set to normal. CLEARED")
        
        Input_Qty.configure(state='normal')
        Input_Qty.delete(0,END)
        num_items.set("0")
        print("ADMIN: Input Quantity set to normal. CLEARED")
        
        Submit.configure(state='normal')
        print("ADMIN: Submit Button set to normal")
        
        Payment_Entry.configure(state='normal')
        Payment_Entry.delete(0,END)
        Payment_Entry.configure(state='disabled')
        print("ADMIN: Payment RESET")
        
        Payment.set("0.0")
        Change_Var.set("0.0")
        Total_Var.set("0.0")
        print("ADMIN: Payment, Change, and Total CLEARED")
        
        Flavors.set("0")
        Selected_Option.set("Sizes:")
        AddOns.set("0")
        Milky_Way.configure(state='normal')
        Mars.configure(state='normal')
        Dreamy_Banana_Split.configure(state='normal')
        Solar_System.configure(state='normal')
        Size_Dropdown.configure(state='normal')
        Nips.configure(state='normal')
        Choco_Chips.configure(state='normal')
        Sprinkles.configure(state='normal')
        Marsh_Mallows.configure(state='normal')
        Nuts.configure(state='normal')
        Cherry.configure(state='normal')
        No_AddOns.configure(state='normal')
        print("ADMIN: All Options RESETS")

        Plushie.config(bg="white")
        Keychain.config(bg="white")
        Jacket.config(bg="white")
        T_Shirt.config(bg="white")
        Onion.config(bg="white")

        PLUSHIE_Label.place_forget()
        KEYCHAIN_Label.place_forget()
        JACKET_Label.place_forget()
        TSHIRT_Label.place_forget()
        ONION_Label.place_forget()
            
        print("ADMIN: Random Values RESET")
        
        #Return to transaction
        Transac_Frame.place(x=20, y=50)
        Item_Label.place(x = 20, y = 32)
        Price1_Label.place(x = 122, y = 32)
        Add_On_Label.place(x = 224, y = 32)
        Quantity_Label.place(x = 326, y = 32)
        Price2_Label.place(x = 428, y = 32)

        Reward_Var.set("")
        Receipt_Var.set("")
        Item_Column.delete(0,END)
        Price1_Column.delete(0,END)
        Add_On_Column.delete(0,END)
        Quantity_Column.delete(0,END)
        Price2_Column.delete(0,END)

        Item_Column.place(x = 20, y = 50)
        Price1_Column.place(x = 122, y = 50)
        Add_On_Column.place(x = 224, y = 50)
        Quantity_Column.place(x = 327, y = 50)
        Price2_Column.place(x = 426, y = 50)
        Print.place_forget()

        print("ADMIN: Variables CLEARED")

        Transaction_Button.configure(state = 'disabled')
        Receipt_Button.configure(state = 'disabled')
        print("ADMIN: Transaction CLEARED")
        print("ADMIN: Receipt CLEARED")

        print("ADMIN: GUI RESETS")
        print()
        print ("-------------------------------------------------------------")
        messagebox.showinfo("INFORMATION.", "DDLite POS System resets")
    
#Loop Order:
def loop_order():
    global i
    global prompt_loop_order
    global list_box_i
    global ChosenFlavor
    global ChosenSize
    global ChosenAddOns

    prompt_loop_order = messagebox.askyesno('Confirmation', 'Do you want another set of ice cream to your order')

    if prompt_loop_order == True:

        #Increment indexes to make a fresh input containers
        i += 1
        list_box_i += 1
        orders[i] = {}

        #Display previous order when ordering another items
        Item_Column.insert(list_box_i-1, f"{ChosenFlavor}\n\n")
        Price1_Column.insert(list_box_i-1, f"{ChosenSize}\n\n")
        Add_On_Column.insert(list_box_i-1, f"{ChosenAddOns}\n\n")
        Quantity_Column.insert(list_box_i-1, f"Qty: {items}\n\n")
        Price2_Column.insert(list_box_i-1, f"₱{subtotal}\n\n")

        Customer_Name_Entry.configure(state='disabled')
        Undo.configure(state='normal')
        Flavors.set("0")
        Selected_Option.set("Sizes:")
        AddOns.set("0")
        Input_Qty.delete(0, END)

        #Delete the current listbox input displays to avoid overlapping and overwriting of listbox order displays
        Item_Column.delete(list_box_i-1, END)
        Price1_Column.delete(list_box_i-1, END)
        Add_On_Column.delete(list_box_i-1, END)
        print("-------------------------------------------------------------")

    elif prompt_loop_order == False:
        #Disable input states to avoid unpacking errors
        Customer_Name_Entry.configure(state='disabled')
        Undo.configure(state='disable')
        Input_Qty.configure(state='disabled')
        Submit.configure(state='disabled')
        enter_button.configure(state='normal')
        Payment_Entry.configure(state='normal')
        Milky_Way.configure(state='disabled')
        Mars.configure(state='disabled')
        Dreamy_Banana_Split.configure(state='disabled')
        Solar_System.configure(state='disabled')
        Size_Dropdown.configure(state='disabled')
        Nips.configure(state='disabled')
        Choco_Chips.configure(state='disabled')
        Sprinkles.configure(state='disabled')
        Marsh_Mallows.configure(state='disabled')
        Nuts.configure(state='disabled')
        Cherry.configure(state='disabled')
        No_AddOns.configure(state='disabled')

        #Delete any current listbox display to prevent unecessary overlapping and overwriting of listbox order displays
        Input_Qty.delete(0, END)
        Item_Column.delete(0, tk.END)
        Price1_Column.delete(0, tk.END)
        Add_On_Column.delete(0, tk.END)
        Quantity_Column.delete(0, tk.END)
        Price2_Column.delete(0, tk.END)
        Transaction_Dictionary()

def Transaction_Dictionary():
    global TOTAL
    global subtotal
    global addprc
    global list_box_i

    #initialize variables with 0 or blank string in order to be available of usage
    s = ""
    TOTAL = 0
    QTY = 0
    subtotal = 0

    #Unpacking of dictionary
    for order in orders.values():

        if not order:
            continue
        
        #Sort orders in order to organize the extraction of the values without overwriting them no matter what order the input is triggered or transferred 
        order = dict(sorted(order.items(), key=lambda x: x[0]))
        
        #Get the values and provide the expectations
        order = tuple(order.values())
        ChosenAddOns, addprc, ChosenFlavor, subtotal, items, ChosenSize = order

        #Recomputation for final cost
        QTY += float(items)
        TOTAL += subtotal

        #string format
        s += f"{ChosenFlavor}|{ChosenSize}|Additional ₱{addprc} for add-on: {ChosenAddOns}|Qty: {items} = ₱{subtotal}\n"

        #Update the listbox of transaction
        Item_Column.insert(list_box_i, f"{ChosenFlavor}\n\n")
        Price1_Column.insert(list_box_i, f"{ChosenSize}\n\n")
        if ChosenAddOns == 'NoAddOns':
            Add_On_Column.insert(list_box_i-1, f"NoAddOns\n\n")
        else:
            Add_On_Column.insert(list_box_i, f"Additional ₱{addprc} for add-on: {ChosenAddOns}\n\n")
        Quantity_Column.insert(list_box_i, f"Qty: {items}\n\n")
        Price2_Column.insert(list_box_i, f"₱{subtotal}\n\n")
        
        #list_box_i += 1 <- failsafe just in case if there would be a display listbox error when unpacking 

    #Print the transaction to terminal to check if the data is right
    print("Your order is/are:")
    print(s)
    print ("Quantity:",QTY)
    print ("Total: ₱", float(abs(TOTAL)))
    print()

    update_TOTAL()
    
def update_TOTAL():
    global TOTAL
    Total_Var.set(float(TOTAL))

def enter_Payment():
    global PAYMENT
    global CHANGE
    global TOTAL

    PAYMENT = Payment.get()

    if PAYMENT == '':
        print("INVALID. Please pay atleast the required amount")
        messagebox.showwarning("INVALID", "Please pay atleast the required amount")
        print()
        return
    
    PAYMENT = float(PAYMENT)
    TOTAL = float(TOTAL)
    
    #Calculation 
    if PAYMENT >= TOTAL:
        CHANGE = PAYMENT - TOTAL
        print("Change:", CHANGE)
        enter_button.configure(state='disabled')
        Payment_Entry.configure(state='disabled')
        update_CHANGE()

    elif PAYMENT <= 0:
        print("INVALID. Please pay atleast the required amount")
        messagebox.showwarning("INVALID", "Please pay atleast the required amount")
        print()
        
    else:
        CHANGE = TOTAL - PAYMENT
        messagebox.showwarning("INVALID", "Please pay atleast the required amount")
        print ("Sorry, we can't accept you payment.")
        print ("You still need ₱",CHANGE,"to purchase this item.")
        print ("Please pay atleast the required amount of ₱", TOTAL)
        print()

def update_CHANGE():
    print()
    Change_Var.set(float(CHANGE))
    
    if TOTAL > 300:
        update_color(0)
        
    else:
        update_REWARD()
    
#-----------------------------------------------------------------------------------------------------------------------    
#Random Items color event and validation handler
#Event handler. This block of function keeps track of the number of color updates that have been performed.
def update_color(ctr: int):
    change_color()

    #If the counter performed above 10 updates of changes, stop the code.
    if ctr > 10:
        stop_color_update()
        return 
    
    #this will be handled
    #100 means 100 milliseconds and this handles the que for update_color to be called again
    #and if the function is called again, it will have a new set of randomly assigned colors because it incremente the function's counter by +1
    root.after(100, lambda: update_color(ctr + 1))

#Color randomizer
def change_color():
    #Responsible of randomizing any color amd listing 5 of them for our 5 items
    color = ['#{:06x}'.format(randint(0, 0xFFFFFF)) for _ in range(5)]

    #Set the background color of the button
    #It must differ to each other to achieve flashing light effect
    Plushie.config(bg=color[0])
    Keychain.config(bg=color[1])
    Jacket.config(bg=color[2])
    T_Shirt.config(bg=color[3])
    Onion.config(bg=color[4])

#End session of colors
#This is called if the counter of update_color reaches above 10
def stop_color_update():
    root.after_cancel(update_color)
    print_reward()
#-----------------------------------------------------------------------------------------------------------------------

#Won reward indicator
#bg colors of won reward are set to green to indicate the won reward as well as displaying the image of the item
def print_reward():
    global REWARD
    item_randomizer = {"PLUSHIE", "KEYCHAIN", "JACKET", "T-SHIRT", "ONION"}
    REWARD = random.choice(tuple(item_randomizer))

    if REWARD == "PLUSHIE":
        Plushie.config(bg='green')
        list(map(lambda widget: widget.config(bg='white'), [Keychain, Jacket, T_Shirt, Onion]))
        PLUSHIE_Label.place(x=0, y=0)

    elif REWARD == "KEYCHAIN":
        Keychain.config(bg='green')
        list(map(lambda widget: widget.config(bg='white'), [Plushie, Jacket, T_Shirt, Onion]))
        KEYCHAIN_Label.place(x=0, y=0)

    elif REWARD == "JACKET":
        Jacket.config(bg='green')
        list(map(lambda widget: widget.config(bg='white'), [Plushie, Keychain, T_Shirt, Onion]))
        JACKET_Label.place(x=0, y=0)

    elif REWARD == "T-SHIRT":
        T_Shirt.config(bg='green')
        list(map(lambda widget: widget.config(bg='white'), [Plushie, Keychain, Jacket, Onion]))
        TSHIRT_Label.place(x=0, y=0)

    elif REWARD == "ONION":
        Onion.config(bg='green')
        list(map(lambda widget: widget.config(bg='white'), [Plushie, Keychain, Jacket, T_Shirt]))
        ONION_Label.place(x=0, y=0)
        
    else:
        print("Error. Something went wrong: print_reward()")
    
    update_REWARD()

def update_REWARD():
    if TOTAL > 300:
        Reward_Var.set(REWARD)
        print("Reward:", REWARD)
        print()

    else:
        Reward_Var.set("None")
        print("No Reward")
        print()

    Receipt_Button.configure(state = 'normal')
    Receipt()

def Receipt():
    global RESIBO
    dt = datetime.datetime.now()
    Name = username.get()

    global RESIBO
    RESIBO = ""
    
    RESIBO += "                           RECEIPT                          " 
    RESIBO += "\n"
    RESIBO += "                       =DREAMY D' LITE=                     "
    RESIBO += "\n"
    RESIBO += "               'Taste the Dream of an Ice Cream'            "

    RESIBO += "\n"
    RESIBO += "\n"
    RESIBO += "Address: Mema Bahay, Brgy. Kahitanongbaranggay, Imus, Cavite\n"
    RESIBO += "Cashier: Marco Tecson \n"

    #Assuming `dt` is a datetime object representing the current date and time
    #%a : weekday, %b : month, %d : day, %Y : year
    #%I : 12 hour clock, %M : minutes, %p : am/pm
    RESIBO += "Date: " + dt.strftime("%a, %b %d, %Y") + " Time: " + dt.strftime("%I:%M %p") + "\n"
    RESIBO += "\n"
    RESIBO += "Customer's Name: " + Name + "\n"
    RESIBO += "\n"

    RESIBO += "=============================================================\n"
    RESIBO += "ITEM/S                         QTY           ITEM PRICE  \n"
    RESIBO += "\n"

    for order in orders.values():

        if not order:
            continue

        order = dict(sorted(order.items(), key=lambda x: x[0]))
        order = tuple(order.values())
        ChosenAddOns, addprc, ChosenFlavor, subtotal, items, ChosenSize = order
        
        #ljust are whitespace handlers
        RESIBO += '{}'.format(ChosenFlavor.ljust(31))+'{}'.format(str(items).ljust(15))+'₱{}'.format(str(float(subtotal)).ljust(10))+"\n"
        RESIBO += '{}'.format(ChosenSize.ljust(32))+"\n"
        RESIBO += '{}'.format(ChosenAddOns+': ₱'+f"{addprc}".ljust(49))+"\n"
        
    RESIBO += "=============================================================\n"

    RESIBO += "TOTAL                                         ₱"+'{}'.format(str(float(TOTAL)))+"\n"
    RESIBO += "PAYMENT                                       ₱"+'{}'.format(str(float(PAYMENT)))+"\n"
    RESIBO += "CHANGE                                        ₱"+'{}'.format(str(float(CHANGE)))+"\n"
    RESIBO += "=============================================================\n"

    if TOTAL > 300:
        RESIBO += "   Since your purchase is above Php 300, congratulations!   \n"
        RESIBO += "                   You won a random item!                   \n"
        RESIBO += "       Your free mystery random item will be:"+'{}'.format(REWARD)+"\n"
        
        if REWARD == 'ONION':
            RESIBO += "                   Better luck next time!                   \n"
            
            
        else:
            RESIBO += "     ✧･ﾟ:✧Thank you for your purchase! Please come again!✧:･ﾟ✧ \n"
            
    else:
        RESIBO += "     ✧･ﾟ:✧Thank you for your purchase! Please come again!✧:･ﾟ✧ \n"

    print(RESIBO)

def show_transaction_frame():
    Receipt_Button.configure(state = 'normal')
    Transaction_Button.configure(state = 'disabled')
    
    Transac_Frame.place(x=20, y=50)
    Receipt_Frame.place_forget()
    Item_Label.place(x = 20, y = 32)
    Price1_Label.place(x = 122, y = 32)
    Add_On_Label.place(x = 224, y = 32)
    Price2_Label.place(x = 326, y = 32)
    Quantity_Label.place(x = 428, y = 32)

    Transac_Frame.place(x=20, y=50)
    Item_Column.place(x = 20, y = 50)
    Price1_Column.place(x = 122, y = 50)
    Add_On_Column.place(x = 224, y = 50)
    Quantity_Column.place(x = 327, y = 50)
    Price2_Column.place(x = 426, y = 50)

    Print.place_forget()


    
def show_receipt_frame():
    Transaction_Button.configure(state = 'normal')
    Receipt_Button.configure(state = 'disabled')
    
    Receipt_Frame.place(x=90, y=32)
    Transac_Frame.place_forget()
    Item_Label.place_forget()
    Price1_Label.place_forget()
    Add_On_Label.place_forget()
    Price2_Label.place_forget()
    Quantity_Label.place_forget()

    Item_Column.place_forget()
    Price1_Column.place_forget()
    Add_On_Column.place_forget()
    Price2_Column.place_forget()
    Quantity_Column.place_forget()

    Print.place(x= 400, y=490)

    Receipt_Var.set(RESIBO)

def print_receipt():
    global pdf
    height = len(RESIBO.splitlines()) + 8
    pdf = FPDF("P", "mm", (126, height*8 / 2.5))
    pdf.add_page()
    pdf.set_font('Courier', '', 8)
    pdf.multi_cell(0, 3, RESIBO)
    receipt_file = f"Receipt_{username.get()}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    pdf.output(receipt_file)
    subprocess.Popen([receipt_file], shell=True)

#Number Input
    #Clicking the entry is bounded in this function. qty_click_flag is the state of the entry. 
    #if If the entry is clicked and qty_click_flag == False, make the state true and set it to blank 
def on_input_qty_click():
    global qty_click_flag
    if not qty_click_flag:
        qty_click_flag = True
        num_items.set("")

def on_input_payment_click():
    global payment_click_flag
    if not payment_click_flag:
        payment_click_flag = True
        Payment.set("")    

def qty_input(inp):
    #Restriction entry to input 4 digits (million) and numbers only. 
    return (len(num_items.get()) <= 5 and inp.isdigit()) or inp == ""
    
def num_input(inp):
    #Restriction entry to input 9 digits (billion) and numbers only. '.' is accepted as an exception of restricted character. 
    #Checking if the input is blank or 0 then validate as true in order to make the restrictions of input work
    if inp == "" or inp == 0:
        return True
    return inp.count(".") < 2 and ''.join(inp.split('.')).isdigit() and len(Payment.get()) <= 9

#Button Click
def button_click(value):
    Input_Qty.insert(END, str(value))
    Payment_Entry.insert(END, str(value))

def backspace_name(event):
    content = Customer_Name_Entry.get()
    backspacing = content[:-1]
    Customer_Name_Entry.delete(0, END)
    Customer_Name_Entry.insert(0, backspacing)

def backspace_num(event):
    content = Input_Qty.get()
    backspacing = content[:-1]
    Input_Qty.delete(0, END)
    Input_Qty.insert(0, backspacing)

def backspace_pay(event):
    content = Payment_Entry.get()
    backspacing = content[:-1]
    Payment_Entry.delete(0, END)
    Payment_Entry.insert(0, backspacing)

def Decimal():
    Payment_Entry.insert(END, ".")


#Main function
#root
root = Tk()
root.title("Dreamy D'lights")
root.configure(bg='#2A2F4F')
root.geometry('1215x900')
root.iconbitmap("DDL_1.ico")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
#root.resizable(False, False)  # Disable window resizing



# Frames
s= ttk.Style()

main_frame = ttk.Frame(root, height= 900, width= 1215, style='Main.TFrame')
s.configure('Main.TFrame', background ='#2A2F4F')

top_frame = ttk.Frame(main_frame, height= 75, width=730, relief=tk.RAISED, borderwidth = 5, style='TopFrame.TFrame')
s.configure('TopFrame.TFrame', background ='#363C66')

flavors_frame = ttk.Frame(main_frame, height=115, width=730, relief=tk.RAISED, borderwidth = 5, style='FlavorsFrame.TFrame')
s.configure('FlavorsFrame.TFrame', background ='#917FB3')

size_frame = ttk.Frame(main_frame, height=55, width=195, relief=tk.RAISED, borderwidth = 5, style='SizeFrame.TFrame')
s.configure('SizeFrame.TFrame', background ='#917FB3') 

addons_frame = ttk.Frame(main_frame, height=225, width=410,  relief=tk.RAISED, borderwidth = 5, style='AddFrame.TFrame')
s.configure('AddFrame.TFrame', background ='#917FB3') 

quantity_frame = ttk.Frame(main_frame, height= 45, width=195,  relief=tk.RAISED, borderwidth = 5, style='QuantityFrame.TFrame')
s.configure('QuantityFrame.TFrame', background ='#917FB3') 

random_frame = ttk.Frame(main_frame, height=280, width=600,  relief=tk.RAISED, borderwidth = 5, style='RandomFrame.TFrame')
s.configure('RandomFrame.TFrame', background ='#E5BEEC') 

calcu_frame = ttk.Frame(main_frame, height=190, width = 440,  relief=tk.RAISED, borderwidth = 5, style='CalcuFrame.TFrame')
s.configure('CalcuFrame.TFrame', background ='#917FB3') 

transact_frame = ttk.Frame(main_frame, height=545, width = 570,  relief=tk.RAISED, borderwidth = 5, style='TransactFrame.TFrame')
s.configure('TransactFrame.TFrame', background ='#FDE2F3') 

Description_frame = ttk.Frame(top_frame, height= 65, width=275, relief=tk.SUNKEN, borderwidth = 5, style='DescFrame.TFrame')
s.configure('DescFrame.TFrame', background ='white')

Reward_Picture_frame = ttk.Frame(random_frame, height= 265, width=250, relief=tk.SUNKEN, borderwidth = 5, style='Reward_Picture.TFrame')
s.configure('Reward_Picture.TFrame', background ='#FDE2F3')



#Header (Label)
DDLite_Header = Label (top_frame, text = "Dreamy 'D Lite Ice Cream", height = 1,
    font = ('Georgia',21,'italic'), wraplength = 500, bg = '#363C66', fg='white')

Description_Label = Label (Description_frame, text = "Total purchase of more than ₱300\nwill recieve one free random item!", height = 2,
    font = ('Georgia',12,'italic'), wraplength = 295, bg = 'white', justify='left')



#Sections (Labels)
Flavor_Section = Label(flavors_frame, text = "Flavors -------------------------------------------------------------------------------",
    font = ('Georgia',15,'bold'), wraplength = 800, bg = '#917FB3', fg='white')

Sizes_Section = Label (size_frame, text = "--------------------",
    font = ('Georgia',15,'bold'), wraplength = 600, bg = '#917FB3', fg='white')

Add_ons_Section = Label (addons_frame, text = "Add-ons ₱10 each -------------------------",
    font = ('Georgia',15,'bold'), wraplength = 600, bg = '#917FB3', fg='white')

Random_Item_Section = Label (main_frame, text = "----------------------------------------------------------------------",
    font = ('Georgia',15,'bold'), wraplength = 700, bg = '#2A2F4F', fg='white')
    
Random_Item_Title = Label (main_frame, text = "REWARD", font = ('Georgia',15,'bold'), wraplength = 600, bg = '#2A2F4F', fg='white')



#Customer Name (Label)
Customer_Name_Label = Label (top_frame, text="Customer's Name: ",font = ('Georgia', 12, 'bold'),bg = '#363C66', fg='white')

#Customer Name (Entry)
CustomerName = root.register(text_input)
username = StringVar()
Customer_Name_Entry = Entry(top_frame, font=('Georgia', 10), validate="key", validatecommand=(CustomerName, '%P'), textvariable=username)
Customer_Name_Entry.bind("<BackSpace>", backspace_name)




#Flavors (Radio Buttons)
Flavors = StringVar()
Flavors.set("0")

    #Milky Way (Vanilla) Configurations
Milky_Way_Image = PhotoImage(file="MilkyWay.png")
Milky_Way = Radiobutton (flavors_frame, image = Milky_Way_Image, width = 120, height = 35, variable = Flavors,
    border = 6, relief = "raised", highlightthickness=9, value="Milky Way (Vanilla)", command = flavor_selection)
Milky_Way.configure(bg='beige')

    #Mars (Chocolate) Configurations
Mars_Image = PhotoImage(file="Mars.png")
Mars = Radiobutton (flavors_frame, image = Mars_Image, width = 120, height = 35, variable = Flavors,
    border = 6, relief = "raised", highlightthickness=9, value="Mars (Chocolate)", command = flavor_selection)
Mars.configure(bg='beige')

    #Dreamy Banana Split (Special) Configurations
Dreamy_Banana_Split_Image = PhotoImage(file="DBananaSplit.png")
Dreamy_Banana_Split = Radiobutton (flavors_frame, image = Dreamy_Banana_Split_Image, width = 120, height = 35, variable = Flavors,
    border = 6, relief = "raised", highlightthickness=9, value="Dreamy Banana Split (Special)", command = flavor_selection)
Dreamy_Banana_Split.configure(bg='beige')

    #Solar System (Assorted) Configurations
Solar_System_Image = PhotoImage(file="SolarSystem.png")
Solar_System = Radiobutton (flavors_frame, image = Solar_System_Image, width = 120, height = 35, variable = Flavors,
    border = 6, relief = "raised", highlightthickness=9, value="Solar System (Assorted)", command = flavor_selection)
Solar_System.configure(bg='beige')



#Sizes (Option Menu)
Sizes = ["Sizes:","Dwarf (S): ₱20", "Terra (M): ₱40", "Titan (L): ₱65"]
Selected_Option = tk.StringVar()
Selected_Option.set(Sizes[0])
Size_Dropdown = OptionMenu (size_frame, Selected_Option, *Sizes, command=size_selection)
Size_Dropdown.configure(font = ('Georgia',15,'bold'), bg='saddlebrown', fg='white', width=10)

#Add-ons (Buttons)
AddOns = StringVar()
AddOns.set("0")
    
    #Nips
Nips_Image = PhotoImage(file="Nips.png")
Nips = Radiobutton (addons_frame, image=Nips_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="Nips", command = addOns_selection)

    #Choco Chips
Choco_Chips_Image = PhotoImage(file="Choco_Chips.png")
Choco_Chips = Radiobutton (addons_frame, image=Choco_Chips_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="ChocoChips", command = addOns_selection)

    #Sprinkles
Sprinkles_Image = PhotoImage(file="Sprinkles.png")
Sprinkles = Radiobutton (addons_frame, image=Sprinkles_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="Sprinkles", command = addOns_selection)

    #Mallows
Marsh_Mallows_Image = PhotoImage(file="Mallows.png")
Marsh_Mallows = Radiobutton (addons_frame, image=Marsh_Mallows_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="Mallows", command = addOns_selection)

    #Nuts
Nuts_Image = PhotoImage(file="Nuts.png")
Nuts = Radiobutton (addons_frame, image=Nuts_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="Nuts", command = addOns_selection)

    #Cherry
Cherry_Image = PhotoImage(file="Cherry.png")
Cherry = Radiobutton (addons_frame, image=Cherry_Image, width=140, height=50, bg='saddlebrown', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="Cherry", command = addOns_selection)
    
    #No Add-Ons
No_AddOns = Radiobutton (addons_frame, text="✖", width=3, height=11, bg='gainsboro', variable = AddOns,
    border = 2, relief = "raised", highlightthickness=1, value="NoAddOns", command = addOns_selection)


#Quantity (Label)
Quantity = Label (quantity_frame, text = "Quantity:", font = ('Georgia',15,'bold'), wraplength=500, bg = '#917FB3', fg='white')

#Quantity (Entry)
qty_input = root.register(qty_input)
num_items = StringVar()
num_items.set("0")
Input_Qty = Entry (quantity_frame, width = 7, font = ('Georgia',12), validate="key", validatecommand=(qty_input, '%P'), textvariable = num_items)
Input_Qty.bind("<Button-1>", lambda event: on_input_qty_click())
Input_Qty.bind("<BackSpace>", backspace_num)


#Logo (Button)
Logo_Image = Image.open("DDL_2.png")
resize_Logo_image = Logo_Image.resize((75,50))
New_Logo_Image = ImageTk.PhotoImage(resize_Logo_image)
Logo_Button = Button (top_frame, image= New_Logo_Image, width=75, height=50, bg='black', command=Home)
Logo_Button.place(x=0, y=5)

#Submit (Button)
Submit = Button (main_frame, text="Submit", width=10, height=5, bg='gainsboro', command = Submit)


#Undo (Button)
Undo = Button (main_frame, text="Void", width=14, height=2, bg='gainsboro', state='disable', command = undo)


#Void (Button)
Void = Button (main_frame, text="Reset", width=14, height=2, bg='gainsboro', command = void)


#Item Randomizer
    #Plushie
Plushie_Image = PhotoImage(file="Plushie.png")
Plushie = Label (random_frame, image = Plushie_Image, font = ('Georgia',12), width = 120, height = 35, border = 15, highlightthickness=1, highlightbackground="black")

    #Keychain
Keychain_Image = PhotoImage(file="KeyChain.png")
Keychain = Label (random_frame, image = Keychain_Image, font = ('Georgia',12), width = 120, height = 35, border = 15, highlightthickness=1, highlightbackground="black")

    #Jacket
Jacket_Image = PhotoImage(file="Jacket.png")
Jacket = Label (random_frame, image = Jacket_Image, font = ('Georgia',12), width = 120, height = 35, border = 15, highlightthickness=1, highlightbackground="black")

    #T-Shirt
T_Shirt_Image = PhotoImage(file="T-Shirt.png")
T_Shirt = Label (random_frame, image = T_Shirt_Image, font = ('Georgia',12), width = 120, height = 35, border = 15, highlightthickness=1, highlightbackground="black")

    #Onion    
Onion_Image = PhotoImage(file="Onion.png")
Onion = Label (random_frame, image = Onion_Image, font = ('Georgia',12), width = 120, height = 35, border = 15, highlightthickness=1, highlightbackground="black")

#Reward pictures
PLUSHIE_Image = Image.open("PLUSHIE_PIC.png")
resize_PLUSHIE_image = PLUSHIE_Image.resize((236,251))
New_PLUSHIE_Image = ImageTk.PhotoImage(resize_PLUSHIE_image)
PLUSHIE_Label = Label (Reward_Picture_frame, image= New_PLUSHIE_Image, width=236, height=251)
       
KEYCHAIN_Image = Image.open("KEYCHAIN_PIC.png")
resize_KEYCHAIN_image = KEYCHAIN_Image.resize((236,251))
New_KEYCHAIN_Image = ImageTk.PhotoImage(resize_KEYCHAIN_image)
KEYCHAIN_Label = Label (Reward_Picture_frame, image= New_KEYCHAIN_Image, width=236, height=251)
        
JACKET_Image = Image.open("JACKET_PIC.png")
resize_JACKET_image = JACKET_Image.resize((236,251))
New_JACKET_Image = ImageTk.PhotoImage(resize_JACKET_image)
JACKET_Label = Label (Reward_Picture_frame, image= New_JACKET_Image, width=236, height=251)
        
TSHIRT_Image = Image.open("TSHIRT_PIC.png")
resize_TSHIRT_image = TSHIRT_Image.resize((236,251))
New_TSHIRT_Image = ImageTk.PhotoImage(resize_TSHIRT_image)
TSHIRT_Label = Label (Reward_Picture_frame, image= New_TSHIRT_Image, width=236, height=251)
        
ONION_Image = Image.open("ONION_PIC.png")
resize_ONION_image = ONION_Image.resize((236,251))
New_ONION_Image = ImageTk.PhotoImage(resize_ONION_image)
ONION_Label = Label (Reward_Picture_frame, image= New_ONION_Image, width=236, height=251)


#Payment (Label)
Payment_Label = Label (calcu_frame, text="Payment: ",font = ('Georgia',12, 'bold'),bg = '#917FB3', fg='white')
Payment_Peso_Sign = Label (calcu_frame, text="₱",font = ('Georgia',12, 'bold'),bg = '#917FB3', fg='white')

#Payment (Entry)
num_input = root.register(num_input)
Payment = StringVar()
Payment.set("0.0")
Payment_Entry = Entry (calcu_frame, font = ('Georgia',12), width = 16, justify='left', validate="key", validatecommand=(num_input, '%P'), textvariable = Payment, state = 'disabled')
Payment_Entry.bind("<Button-1>", lambda event: on_input_payment_click())
Payment_Entry.bind("<BackSpace>", backspace_pay)


#Change (Label)
Change_Var = StringVar()
Change_Var.set("0.0")

Change_Label = Label (calcu_frame, text="Change:",font = ('Georgia',12, 'bold'), bg='#917FB3', fg='white')
Change_Peso_Sign = Label (calcu_frame, text="₱",font = ('Georgia',12, 'bold'),bg = '#917FB3', fg='white')
Change_Box = Label (calcu_frame, font = ('Georgia',10), width = 20, textvariable = Change_Var, anchor='w', justify='left', bg='white', relief=SUNKEN)

#Reward (Label)
Reward_Var = StringVar()
Reward_Var.set("")

Reward_Label = Label (calcu_frame, text="Reward: ",font = ('Georgia',12, 'bold'),bg = '#917FB3', fg='white')
Reward_Box = Label (calcu_frame, font = ('Georgia',10), width = 17, textvariable = Reward_Var, anchor='w', justify='left', bg='white', relief=SUNKEN)



#RECEIPT
    #Receipt Button
Receipt_Button = Button (transact_frame, text="Receipt", width=9, height=1, bg='lightgrey', relief=tk.RAISED, state = 'disabled',borderwidth=1, command=show_receipt_frame)

    #Receipt Frame
Receipt_Frame = ttk.Frame(transact_frame, height= 430, width=440, relief=tk.SUNKEN, borderwidth = 5, style='ReceiptFrame.TFrame')
s.configure('ReceiptFrame.TFrame', background ='white')

    #Receipt Container
Receipt_Var = StringVar()
Receipt_Var.set("")
Receipt_Container = Label (Receipt_Frame, width = 60, height = 29, relief = SUNKEN, borderwidth = 1, textvariable = Receipt_Var, anchor = 'nw', justify = 'left', wraplength = 500, font = ('Courier', 8))

    #Print receipt
Print = Button (transact_frame, text="Print", width=14, height=2, bg='gainsboro', relief=tk.RAISED, borderwidth=1, command=print_receipt)


#TRANSACTION
    #Transaction Button
Transaction_Button = Button (transact_frame, text="Transaction", width=9, height=1, bg='lightgrey', relief=RAISED, borderwidth=1, state = 'disabled',  command=show_transaction_frame)

Item_Label = Label (transact_frame, text = "Flavor", width = 14, height = 1, bg = 'gainsboro', relief = RAISED, anchor='w', borderwidth = 1)

Price1_Label = Label (transact_frame, text = "Size", width = 14, height = 1, bg = 'gainsboro', relief = RAISED, anchor='w', borderwidth = 1)

Add_On_Label = Label (transact_frame, text = "Add-On", width = 14, height = 1, bg = 'gainsboro', relief = RAISED, anchor='w', borderwidth = 1)

Price2_Label = Label (transact_frame, text = "Price", width = 14, height = 1, bg='gainsboro', relief = RAISED, anchor='w', borderwidth = 1)

Quantity_Label = Label (transact_frame, text = "Quantity", width = 14, height = 1, bg='gainsboro',relief = RAISED, anchor='w', borderwidth = 1)

#Transaction Frame
Transac_Frame = ttk.Frame(transact_frame, height= 430, width=510, relief=tk.SUNKEN, borderwidth = 5, style='TransacFrame.TFrame')
s.configure('TransacFrame.TFrame')

    #Columns
Item_Column = Listbox (transact_frame, width = 17, height = 27, relief = SUNKEN, borderwidth = 1, justify='left')

Price1_Column = Listbox (transact_frame, width = 17, height = 27, relief = SUNKEN, borderwidth = 1, justify='left')

Add_On_Column = Listbox (transact_frame, width = 17, height = 27, relief = SUNKEN, borderwidth = 1, justify='left')

Price2_Column = Listbox (transact_frame, width = 17, height = 27, relief = SUNKEN, borderwidth = 1, justify='left')

Quantity_Column = Listbox (transact_frame, width = 16, height = 27, relief = SUNKEN, borderwidth = 1, justify='left')
    

#Total (Labels)
Total_Var = StringVar()
Total_Var.set("0.0")

Total_Label = Label (calcu_frame, text="Total: ", font = ('Georgia',12, 'bold') ,bg = '#917FB3', fg='white')
Total_Peso_Sign = Label (calcu_frame, text="₱",font = ('Georgia', 12, 'bold') ,bg = '#917FB3', fg='white')
Total_Box = Label (calcu_frame, font = ('Georgia',10), width = 20, textvariable=Total_Var, anchor='w', justify='left', relief=SUNKEN, bg='white')





#Screen Display
    #Frames
main_frame.pack()
top_frame.place(x=15, y=25)
flavors_frame.place(x=15, y=100)
size_frame.place(x=425, y=215)
addons_frame.place(x=15, y=215)
quantity_frame.place(x=425, y=270)
random_frame.place(x=15, y=490)
transact_frame.place(x=630, y=225)
calcu_frame.place(x=760, y=25)
Description_frame.place(x=440, y=0)
Reward_Picture_frame.place(x=325, y=0)

    #Header
DDLite_Header.place(x = 85, y = 1)
Description_Label.place(x=0, y=5)

    #Customer Name
Customer_Name_Label.place(x = 85, y = 39)
Customer_Name_Entry.place(x = 240, y = 39)

    #Flavors
Flavor_Section.place(x = 0, y = 0)
Milky_Way.place(x = 1, y = 30)
Mars.place(x = 180, y = 30)
Dreamy_Banana_Split.place(x = 360, y = 30)
Solar_System.place(x = 540, y = 30)

    #Sizes
Sizes_Section.place(x = 0, y = 0)
Size_Dropdown.place(x = 0, y = 0)

    #Add-ons
Add_ons_Section.place(x = 0, y = 0)
Nips.place(x = 5, y = 30)
Choco_Chips.place(x = 175, y = 30)
Sprinkles.place(x = 5, y = 150)
Marsh_Mallows.place(x = 5, y = 90)
Nuts.place(x = 175, y = 90)
Cherry.place(x = 175, y = 150)
No_AddOns.place(x = 345, y = 30)

    #Quantity
Quantity.place(x = 0, y = 0)
Input_Qty.place(x = 105, y = 5)    

    #Home
Logo_Button.place(x=0, y=5)

    #Submit
Submit.place(x = 540, y = 355)

    #Undo
Undo.place(x = 432, y = 355)

    #Void
Void.place(x = 432, y = 400)

    #Item Randomizer
Random_Item_Section.place(x = 30, y = 450)
Random_Item_Title.place(x = 255, y = 450)
Plushie.place(x = 0, y = 5)
Keychain.place(x = 160, y = 5)
Jacket.place(x = 160, y = 85)
T_Shirt.place(x = 0, y = 85)
Onion.place(x = 80, y = 165)

    #Total
Total_Label.place(x = 0, y = 95)
Total_Peso_Sign.place(x = 0, y = 115)
Total_Box.place(x = 19, y = 115)

    #Payment
Payment_Label.place(x=0, y=0)
Payment_Peso_Sign.place(x=0, y=22)
Payment_Entry.place(x=19, y=22)

    #Change
Change_Label.place(x=0, y=49)
Change_Peso_Sign.place(x=0, y=72)
Change_Box.place(x=19, y=72)

    #Reward
Reward_Label.place(x=0, y=135)
Reward_Box.place(x=0, y=155)

    #Transaction
Transaction_Button.place(x = 20, y = 8)
Item_Label.place(x = 20, y = 32)
Price1_Label.place(x = 122, y = 32)
Add_On_Label.place(x = 224, y = 32)
Quantity_Label.place(x = 326, y = 32)
Price2_Label.place(x = 428, y = 32)

    #Receipt
Receipt_Button.place(x = 91, y = 8)
Receipt_Frame.place_forget()
Receipt_Container.place(x=0, y=0)


Transac_Frame.place(x=20, y=50)
Item_Column.place(x = 20, y = 50)
Price1_Column.place(x = 122, y = 50)
Add_On_Column.place(x = 224, y = 50)
Quantity_Column.place(x = 327, y = 50)
Price2_Column.place(x = 426, y = 50)



#Number Buttons
Button_Frame = Frame(calcu_frame)
Button_Frame.place(x=200, y=1)

Dec_Point = Button(Button_Frame, text=".", width=9, height=2, bg='gainsboro', command=Decimal)
Dec_Point.grid(row=3, column=1)

enter_button = Button(Button_Frame, text="Enter", width=9, height=2, bg='gainsboro', command=enter_Payment, state='disabled')
enter_button.grid(row=3, column=2)

number_buttons = []
row = 0
column = 0

#Looping (Numbers)
for x in range(10):
    button = Button(Button_Frame, text=str(x), width=9, height=2, bg='gainsboro', command=lambda val=x: button_click(val))
    button.grid(row=row, column=column, padx=0, pady=0)
    number_buttons.append(button)
    column += 1
    if column > 2:
        column = 0
        row += 1


#Program Loop
root.mainloop()
