from tkinter import *
from tkinter import ttk
from app.AppLogic import scan, send_post_request, send_ip

root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()
ttk.Label(frm, text='PC Hardware Scan').grid(column=0, row=0)
ttk.Button(frm, text='Scan PC', command=scan).grid(column=1, row=0)
ttk.Button(frm, text='Load report', command=send_post_request).grid(column=3, row=0)
ttk.Button(frm, text='Send IP', command=send_ip).grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=0)

root.mainloop()



