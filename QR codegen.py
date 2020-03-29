"""
QR code Generator using python and pyqrcode
"""

# importing the required libraries
# Note: pyqrcode is not built-in function, it need to be installed using "pip install pyqrcode"
import pyqrcode
import tkinter as tk


def generator():
    url = entry.get()
    qr = pyqrcode.create(url)
    save = qr.svg('myqrcode3.svg', scale=10)


qrcode = tk.Tk()
qrcode.title("QR code Generator")
qrcode.geometry("400x300")
qrcode.configure(bg="cyan")

label = tk.Label(qrcode, text="Enter Url")
label.grid(row=0, column=0)

entry = tk.Entry(qrcode)
entry.grid(row=1, column=0)

button = tk.Button(qrcode, text="Generate", command=generator)
button.grid(row=1, column=2)


qrcode.mainloop()
