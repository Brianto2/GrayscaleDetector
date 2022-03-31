# Moves all the grayscale images from one folder to another folder
import os
import shutil
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image


# GUI stuff
def UI():
    # Main frame
    gui = Tk()
    gui.geometry("400x150")
    gui.title("BW Image Mover")

    src_path = StringVar()
    dst_path = StringVar()

    # first row, source folder
    s_label = Label(gui, text="Source Folder")
    s_entry = Entry(gui, textvariable=src_path)
    s_browse = ttk.Button(gui, text="Browse Folder", command=lambda: getFolderPath(src_path))

    s_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 5))
    s_entry.grid(row=0, column=1, padx=(10, 10), pady=(10, 5))
    s_browse.grid(row=0, column=2, padx=(10, 10), pady=(10, 5))

    # second row, destination folder
    d_label = Label(gui, text="Destination Folder")
    d_entry = Entry(gui, textvariable=dst_path)
    d_browse = ttk.Button(gui, text="Browse Folder", command=lambda: getFolderPath(dst_path))

    d_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 5))
    d_entry.grid(row=1, column=1, padx=(10, 10), pady=(10, 5))
    d_browse.grid(row=1, column=2, padx=(10, 10), pady=(10, 5))

    # start button
    c = ttk.Button(gui, text="move images", command=lambda: moveImages(src_path, dst_path))
    c.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    return gui


# Sets the directory when the button is clicked
def getFolderPath(folder_path):
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


# Determines which images in the source folder are grayscale images and moves them to the destination folder
def moveImages(src_folder, dst_folder):
    src = src_folder.get()
    dst = dst_folder.get()

    # Don't do anything unless both file paths are specified
    if dst == "" or src == "":
        messagebox.showwarning(title="BW Image Mover", message="Input source and destination folders")
        return
    # Source and destination cannot be the same
    if dst == src:
        messagebox.showwarning(title="BW Image Mover", message="Source and destination folders must be different")
        return
    # Get the user to confirm
    mstring = "Move files from " + src + " to " + dst + "?"  # string must be set before putting it into message=
    option = messagebox.askokcancel(title="BW Image Mover", message=mstring)  # returns True or False
    if not option:
        return

    # iterate through directory, locate and move grayscale images
    try:
        for root, dirs, files in os.walk(src):
            for name in files:
                # Check if the the file is already in the destination folder, skip if so
                if not os.path.samefile(dst, root):
                    f_img = os.path.join(root, name)
                    img = Image.open(f_img).convert('RGB')
                    # Gets the average color of a file
                    img = img.resize((1, 1), Image.ANTIALIAS)
                    imgcolor = img.getpixel((0, 0))

                    # On the color slider if all three values are equal then it is grayscale
                    if imgcolor[0] == imgcolor[1] == imgcolor[2]:
                        shutil.move(f_img, dst)
        messagebox.showinfo(title="BW Image Mover", message="Done")

    # Error handling
    except FileNotFoundError:
        messagebox.showwarning(title="BW Image Mover", message="Unable to locate folder")
    except PermissionError as e:
        messagebox.showwarning(title="BW Image Mover", message=e)
    except Exception as e:
        messagebox.showwarning(title="BW Image Mover", message=e)


# Run
def main():
    mainframe = UI()
    mainframe.mainloop()


if __name__ == "__main__":
    main()
