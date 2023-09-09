from tkinter import *


main_frame = Tk()
main_frame.title('My useless unit converter')
main_frame.minsize(width=200, height=100)
main_frame.config(padx=20, pady=20)

UNITS = ['kilometer', 'mile', 'yard', 'foot', 'meter']


def print_result(val):
    return f'is equal to {round(val,5)}'


def convert_from_km(target_unit):
    start = float(amount.get())
    match target_unit:
        case 'kilometer':
            result = start
        case 'mile':
            result = start / 1.609
        case 'yard':
            result = start * 1_093.6133
        case 'foot':
            result = start * 3_280.8399
        case 'meter':
            result = start * 1000
        case _:
            result = start
    lab_result.config(text=print_result(result))


def convert_from_mile(target_unit):
    start = float(amount.get())
    match target_unit:
        case 'kilometer':
            result = start * 1.609
        case 'mile':
            result = start
        case 'yard':
            result = start * 1760
        case 'foot':
            result = start * 5280
        case 'meter':
            result = start * 1609
        case _:
            result = start
    lab_result.config(text=print_result(result))


def convert_from_yard(target_unit):
    start = float(amount.get())
    match target_unit:
        case 'kilometer':
            result = start * 0.0009144
        case 'mile':
            result = start * 0.0005681818
        case 'yard':
            result = start
        case 'foot':
            result = start * 3
        case 'meter':
            result = start * 0.9144
        case _:
            result = start
    lab_result.config(text=print_result(result))


def convert_from_foot(target_unit):
    start = float(amount.get())
    match target_unit:
        case 'kilometer':
            result = start * 0.0003048
        case 'mile':
            result = start * 0.000189393939
        case 'yard':
            result = start / 3
        case 'foot':
            result = start
        case 'meter':
            result = start * 0.3048
        case _:
            result = start
    lab_result.config(text=print_result(result))


def convert_from_meter(target_unit):
    start = float(amount.get())
    match target_unit:
        case 'kilometer':
            result = start / 1000
        case 'mile':
            result = start / 1609
        case 'yard':
            result = start * 1.0936133
        case 'foot':
            result = start * 3.2808399
        case 'meter':
            result = start
        case _:
            result = start
    lab_result.config(text=print_result(result))


def convert_units(*args):
    start_unit = listbox1.get(listbox1.curselection())
    target_unit = listbox2.get(listbox2.curselection())
    match start_unit:
        case 'kilometer':
            convert_from_km(target_unit)
        case 'mile':
            convert_from_mile(target_unit)
        case 'yard':
            convert_from_yard(target_unit)
        case 'foot':
            convert_from_foot(target_unit)
        case 'meter':
            convert_from_meter(target_unit)
        case _:
            pass


amount = Entry(width=5)
amount.grid(column=0, row=0)

listbox1 = Listbox(height=5, exportselection=False)
for item in UNITS:
    listbox1.insert(UNITS.index(item), item)
listbox1.bind("<<ListboxSelect>>", convert_units)
listbox1.grid(column=1, row=0)

lab_result = Label(text='is equal to: 0', width=20)
lab_result.grid(column=2, row=0)

listbox2 = Listbox(height=5, exportselection=False)
for item in UNITS:
    listbox2.insert(UNITS.index(item), item)
listbox2.bind("<<ListboxSelect>>", convert_units)

listbox2.grid(column=3, row=0)




# def magic_trick():
#     fancy_label.config(text=input_field.get())
#
#
# fancy_label = Label(text='Example text', font=('Arial', 25, 'normal'))
# fancy_label.grid(column=0, row=0)
#
# new_button = Button(text='new button')
# new_button.grid(column=2,row=0)
#
# useful_button = Button(text='click me!', command=magic_trick)
# useful_button.grid(column=1, row=1)
#
# input_field = Entry(width=10)
# input_field.grid(column=3, row=2)


main_frame.mainloop()

