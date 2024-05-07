import pandas
import csv
from tkinter import *


def full_list_option(window):
    window.destroy()
    f_window = Tk()
    f_window.title("Full Stock")
    s_file = pandas.read_csv("Stock_Inventory.csv")
    t = Text(f_window, font=("Arial Black", 14, "bold"), width=52, )
    scrollbar = Scrollbar(f_window, orient='vertical', command=t.yview)
    t.config(yscrollcommand=scrollbar.set)
    for n in range(0, len(s_file["Stock_Name"])):
        s_name = "   Stock Name : " + s_file["Stock_Name"][n]
        s_ref = "   Stock Ref : " + s_file["Stock_Ref"][n]
        s_stock = "   Total Stock : " + str(s_file["Total_Stock"][n])
        n_line = "\n-------------------------------------------------------------------------" \
                 "--------------------------------------\n "
        t.insert(END, n_line)
        t.insert(END, s_name)
        t.insert(END, s_ref)
        t.insert(END, s_stock)
        t.insert(END, n_line)
    t.config(state='disabled')
    t.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(f_window))
    b_button.pack()

    # label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text=s_file["Stock_Name"][n], font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text=s_file["Stock_Ref"][n], font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text="Stock In : ", font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text=s_file["Stock_In"][n], font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text="Stock Out : ", font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text=s_file["Stock_Out"][n], font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text="Total Stock : ", font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text=s_file["Total_Stock"][n], font=("Arial Black", 14, "bold"))
    # label.pack()
    # label = Label(text="---------------------------------------------------------------------------------------",
    #               font=("Arial Black", 14, "bold"))
    # label.pack()


def search_result_name(s_input, s1_window):
    s1_window.destroy()
    s2_window = Tk()
    s2_window.minsize(width=700, height=800)
    s2_window.title("Search Result")
    s_file = pandas.read_csv("Stock_Inventory.csv")
    s_name = s_input
    for n in range(0, len(s_file["Stock_Name"])):
        if s_name == s_file["Stock_Name"][n]:
            label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Name"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Ref"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock In : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_In"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Out : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Out"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Total Stock : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Total_Stock"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            break
    else:
        label = Label(text="This stock name does not exist.", font=("Arial Black", 14, "bold"))
        label.pack()

    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s2_window))
    b_button.pack()


def search_result_ref(s_input, s1_window):
    s1_window.destroy()
    s2_window = Tk()
    s2_window.minsize(width=700, height=800)
    s2_window.title("Search Result")
    s_file = pandas.read_csv("Stock_Inventory.csv")
    s_name = s_input
    for n in range(0, len(s_file["Stock_Ref"])):
        if s_name == s_file["Stock_Ref"][n]:
            label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Name"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Ref"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock In : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_In"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Out : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Out"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Total Stock : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Total_Stock"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            break
    else:
        label = Label(text="This stock ref does not exist.", font=("Arial Black", 14, "bold"))
        label.pack()

    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s2_window))
    b_button.pack()


def search_result_partial_ref(s_input, s1_window):
    s1_window.destroy()
    s2_window = Tk()
    s2_window.minsize(width=700, height=800)
    s2_window.title("Search Result")
    s_file = pandas.read_csv("Stock_Inventory.csv")
    s_name = s_input
    for n in range(0, len(s_file["Stock_Ref"])):
        if s_name in s_file["Stock_Ref"][n]:
            label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Name"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Ref"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Total Stock : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Total_Stock"][n], font=("Arial Black", 14, "bold"))
            label.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s2_window))
    b_button.pack()


def search_result_partial_name(s_input, s1_window):
    s1_window.destroy()
    s2_window = Tk()
    s2_window.minsize(width=700, height=800)
    s2_window.title("Search Result")
    s_file = pandas.read_csv("Stock_Inventory.csv")
    s_name = s_input
    for n in range(0, len(s_file["Stock_Name"])):
        if s_name in s_file["Stock_Name"][n]:
            label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Name"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Stock_Ref"][n], font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text="Total Stock : ", font=("Arial Black", 14, "bold"))
            label.pack()
            label = Label(text=s_file["Total_Stock"][n], font=("Arial Black", 14, "bold"))
            label.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s2_window))
    b_button.pack()


def search_option_name(window):
    window.destroy()
    s1_window = Tk()
    s1_window.title("Stock Search")
    s1_window.minsize(width=700, height=800)
    label = Label(text="Please enter Stock Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    s_input = Entry()
    s_input.pack()
    s_button = Button(text="Search", font=("Arial Black", 14, "bold"),
                      command=lambda: search_result_name(s_input.get(), s1_window))
    s_button.pack()
    e_input = Entry()
    e_input.pack()
    e_button = Button(text="Partial Search", font=("Arial Black", 14, "bold"),
                      command=lambda: search_result_partial_name(e_input.get(), s1_window))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s1_window))
    b_button.pack()


def search_option_ref(window):
    window.destroy()
    s1_window = Tk()
    s1_window.title("Stock Search")
    s1_window.minsize(width=700, height=800)
    label = Label(text="Please enter Stock Ref : ", font=("Arial Black", 14, "bold"))
    label.pack()
    s_input = Entry()
    s_input.pack()
    s_button = Button(text="Search", font=("Arial Black", 14, "bold"),
                      command=lambda: search_result_ref(s_input.get(), s1_window))
    s_button.pack()
    e_input = Entry()
    e_input.pack()
    e_button = Button(text="Partial Search", font=("Arial Black", 14, "bold"),
                      command=lambda: search_result_partial_ref(e_input.get(), s1_window))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(s1_window))
    b_button.pack()


def search_option(window):
    window.destroy()
    e1_window = Tk()
    e1_window.minsize(width=700, height=800)
    e1_window.title("Search Stock")
    e_button = Button(text="Stock Name", font=("Arial Black", 14, "bold"),
                      command=lambda: search_option_name(e1_window))
    e_button.pack()
    e_button = Button(text="Stock Ref", font=("Arial Black", 14, "bold"),
                      command=lambda: search_option_ref(e1_window))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(e1_window))
    b_button.pack()


def stock_editing_in_real(window, date, s_name, s_in, e_name):
    s_file = pandas.read_csv("Stock_Inventory.csv")
    for n in range(0, len(s_file["Stock_Name"])):
        if s_name == s_file["Stock_Name"][n]:
            s_file.loc[n, 'Stock_In'] = s_file["Stock_In"][n].astype(int) + s_in
            s_file.loc[n, 'Total_Stock'] = (s_file["Total_Stock"][n].astype(int) + s_file["Stock_In"][n])
            s_file.to_csv("Stock_Inventory.csv", index=False)
    new_items = [date, s_name, s_in, e_name]
    with open("Stock_In.csv", 'a') as file:
        write = csv.writer(file)
        write.writerow(new_items)
        file.close()
    main_screen(window)


def stock_editing_out_real(window, date, s_name, s_out, e_name):
    s_file = pandas.read_csv("Stock_Inventory.csv")
    for n in range(0, len(s_file["Stock_Name"])):
        if s_name == s_file["Stock_Name"][n]:
            s_file.loc[n, 'Stock_Out'] = s_file["Stock_Out"][n].astype(int) + s_out
            s_file.loc[n, 'Total_Stock'] = s_file["Total_Stock"][n].astype(int) - s_file["Stock_Out"][n]
            s_file.to_csv("Stock_Inventory.csv", index=False)
    new_items = [date, s_name, s_out, e_name]
    with open("Stock_Out.csv", 'a') as file:
        write = csv.writer(file)
        write.writerow(new_items)
        file.close()
    main_screen(window)


def stock_editing_in(window):
    window.destroy()
    e2_window = Tk()
    e2_window.minsize(width=700, height=800)
    e2_window.title("Stock In")
    label = Label(text="Date : ", font=("Arial Black", 14, "bold"))
    label.pack()
    date_input = Entry()
    date_input.pack()
    label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    name_input = Entry()
    name_input.pack()
    label = Label(text="Stock In : ", font=("Arial Black", 14, "bold"))
    label.pack()
    out_input = Entry()
    out_input.pack()
    label = Label(text="Supplier Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    e_name_input = Entry()
    e_name_input.pack()
    e_button = Button(text="Done", font=("Arial Black", 14, "bold"),
                      command=lambda: stock_editing_in_real(e2_window, date_input.get(), name_input.get(),
                                                            int(out_input.get()), e_name_input.get()))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(e2_window))
    b_button.pack()


def stock_editing_out(window):
    window.destroy()
    e2_window = Tk()
    e2_window.minsize(width=700, height=800)
    e2_window.title("Stock Out")
    label = Label(text="Date : ", font=("Arial Black", 14, "bold"))
    label.pack()
    date_input = Entry()
    date_input.pack()
    label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    name_input = Entry()
    name_input.pack()
    label = Label(text="Stock Out : ", font=("Arial Black", 14, "bold"))
    label.pack()
    out_input = Entry()
    out_input.pack()
    label = Label(text="Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    e_name_input = Entry()
    e_name_input.pack()
    e_button = Button(text="Done", font=("Arial Black", 14, "bold"),
                      command=lambda: stock_editing_out_real(e2_window, date_input.get(), name_input.get(),
                                                             int(out_input.get()), e_name_input.get()))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(e2_window))
    b_button.pack()


def edit_option(window):
    window.destroy()
    e1_window = Tk()
    e1_window.minsize(width=700, height=800)
    e1_window.title("Edit Stock")
    e_button = Button(text="Stock Out", font=("Arial Black", 14, "bold"),
                      command=lambda: stock_editing_out(e1_window))
    e_button.pack()
    e_button = Button(text="Stock In", font=("Arial Black", 14, "bold"),
                      command=lambda: stock_editing_in(e1_window))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(e1_window))
    b_button.pack()


def adding_stock(window, a_name, a_ref, a_num):
    new_items = [a_name, a_ref, 0, 0, a_num]
    with open("Stock_Inventory.csv", 'a') as file:
        write = csv.writer(file)
        write.writerow(new_items)
        file.close()
    main_screen(window)


def add_option(window):
    window.destroy()
    a1_window = Tk()
    a1_window.minsize(width=700, height=800)
    a1_window.title("Add Stock")
    label = Label(text="Stock Name : ", font=("Arial Black", 14, "bold"))
    label.pack()
    name_input = Entry()
    name_input.pack()
    label = Label(text="Stock Ref : ", font=("Arial Black", 14, "bold"))
    label.pack()
    ref_input = Entry()
    ref_input.pack()
    label = Label(text="Stock In : ", font=("Arial Black", 14, "bold"))
    label.pack()
    num_input = Entry()
    num_input.pack()
    e_button = Button(text="Add", font=("Arial Black", 14, "bold"),
                      command=lambda: adding_stock(a1_window, name_input.get(), ref_input.get(),
                                                   int(num_input.get())))
    e_button.pack()
    b_button = Button(text="Back", font=("Arial Black", 14, "bold"),
                      command=lambda: main_screen(a1_window))
    b_button.pack()


def main_screen(s_window):
    s_window.destroy()
    window = Tk()
    window.title("Stock Management")
    window.minsize(width=700, height=800)

    search_button = Button(text="Search Stock", font=("Arial Black", 14, "bold"),
                           command=lambda: search_option(window))
    search_button.pack()
    edit_button = Button(text="Edit Stock", font=("Arial Black", 14, "bold"),
                         command=lambda: edit_option(window))
    edit_button.pack()
    full_button = Button(text="See Full Stock", font=("Arial Black", 14, "bold"),
                         command=lambda: full_list_option(window))
    full_button.pack()

    window.mainloop()


main_screen(Tk())
