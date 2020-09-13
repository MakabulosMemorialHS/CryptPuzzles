#!/usr/bin/env python
#
# Caesar Cipher
#
import Tkinter as tk

## Create the Window and the Panels
##

## Create the main window
main_window = tk.Tk()

## Create a Title For the Window and Place it at the
## First (TOP) position.
title_label = tk.Label(master=main_window, text="SHIFT CIPHER")
title_label.pack()

## Create a Box for the Key
##
key_hbox = tk.Frame(master=main_window)
key_hbox.pack()

## Put in a label and an entry for the key
key_label = tk.Label(master = key_hbox, text="Key : ")
key_entry = tk.Entry(master = key_hbox)
key_label.grid(row=0, column=0)
key_entry.grid(row=0, column=1)

## Now we need a huge box for the plaintext and
## the ciphertext and their labels.
text_frame = tk.Frame(master = main_window)
text_frame.pack()   # Pack this box into the main window.


plaintext_frame = tk.Frame(master = text_frame)
plaintext_frame.grid(row = 0, column = 0)

plaintext_label = tk.Label(master = plaintext_frame, text = "Plaintext");
plaintext       = tk.Text(master = plaintext_frame)
plaintext_label.grid(row = 0, column = 0)
plaintext.grid(row = 1, column = 0)

ciphertext_frame = tk.Frame(master = text_frame)
ciphertext_frame.grid(row = 0, column = 1)

ciphertext_label = tk.Label(master = ciphertext_frame, text = "Ciphertext");
ciphertext       = tk.Text(master = ciphertext_frame)
ciphertext_label.grid(row = 0, column = 0)
ciphertext.grid(row = 1, column = 0)

main_window.mainloop()


