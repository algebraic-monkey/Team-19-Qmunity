from tkinter import *
from tkinter import messagebox
import webbrowser
GREY = "#515B52"
GREEN = "#61C332"


def redirect():
    webbrowser.open("https://www.nasdaq.com/market-activity/stocks/screener")
    return


def display(output):
    messagebox.showinfo("Best Stock Option", output)


def output():
    user_stocks = list(symbol_entry.get().split(","))
    print(user_stocks)
    if len(user_stocks) > 0:
        is_ok = messagebox.askokcancel(user_stocks,
                                       f"The stocks you entered are:\n Stocks:{user_stocks}\n Do you want to proceed?")
        if is_ok:
            try:
                func_output = ""
                display(func_output)
                pass
            except FileNotFoundError:
                pass
            else:
                pass
            finally:
                symbol_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "You cannot leave any of the fields empty!")

    return


# generate UI
window = Tk()
window.title("StocQ Up")
window.geometry("550x500")
window.config(padx=100, pady=50, bg="white")

bg = PhotoImage(file="bg_img.png")
canvas1 = Canvas(width=500, height=500, highlightthickness=0)
canvas1.place(x=-100, y=0)
canvas1.create_image(0, 0, image=bg, anchor="nw")

canvas = Canvas(width=170, height=157, highlightthickness=0, bg="white")
canvas.grid(row=0, column=1)
logo_img = PhotoImage(file="logo2.png")
logo = canvas.create_image(83, 77, image=logo_img)


buffer1 = Label(pady=40, text="", bg=GREY)
buffer1.grid(row=1, column=0)

symbol_label = Label(text="Stock Symbol:", bg=GREEN)
symbol_label.grid(row=2, column=0)
symbol_entry = Entry(width=33)
symbol_entry.grid(row=2, column=1)
redirect_btn = Button(text="Get Symbols", width=15, highlightthickness=0, bg=GREEN, command=redirect)
redirect_btn.grid(row=2, column=2)
out_btn = Button(text="Get Best Stock Option", width=44, highlightthickness=0, bg=GREEN, command=output)
out_btn.grid(row=3, column=1, columnspan=2)
symbol_entry.insert(0, "stock symbols separated by commas")
symbol_entry.focus()

window.mainloop()
