from tkinter import * 

root = Tk()
root.title("배체관리자")
root.geometry("300x200")

btn_1 = Button(root, text="(0, 0)", bg="green")
btn_2 = Button(root, text="(0, 1)", bg="red")
btn_3 = Button(root, text="(0, 2)", bg="blue")

btn_4 = Button(root, text="(1, 0)", bg="gray")
btn_5 = Button(root, text="(1, 1)", bg="yellow")
btn_6 = Button(root, text="(1, 2)", bg="pink")

btn_7 = Button(root, text="(2, 0)", bg="purple")
btn_8 = Button(root, text="(2, 1)", bg="orange")
btn_9 = Button(root, text="(2, 2)", bg="cyan")

btn_10 = Button(root, text="(3, 0)", bg="royalblue")
btn_11 = Button(root, text="(3, 1)", bg="beige")
btn_12 = Button(root, text="(3, 2)", bg="brown")

root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=3)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=3)

btn_1.grid(row=0, column=0, sticky="news")
btn_2.grid(row=0, column=1, sticky="news")
btn_3.grid(row=0, column=2, sticky="news")
btn_4.grid(row=1, column=0, columnspan = 2, sticky="news")
btn_6.grid(row=1, column=2, sticky="news")
btn_7.grid(row=2, column=0, rowspan = 2, sticky="news")
btn_8.grid(row=2, column=1, columnspan = 2, sticky="news")
btn_11.grid(row=3, column=1, sticky="news")
btn_12.grid(row=3, column=2, sticky="news")

root.mainloop()