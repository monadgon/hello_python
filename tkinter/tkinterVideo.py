# https://scribles.net/showing-video-image-on-tkinter-window-with-opencv/
# https://076923.github.io/posts/Python-tkinter-2/
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import cv2

class MainWindow():
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 20 # Interval in ms to get the latest frame

        self.i = 0
        self.variable=StringVar()
        self.label1 = tkinter.Label(self.window, text="hello", textvariable=self.variable, width=20, height=5, fg="white", bg="red", relief="solid")
        self.label1.grid(row=0, column=0)
        # Create canvas for image
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=1)

        # Update image on canvas
        self.update_image()

    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format

        # Update image
        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.image)

        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)

        self.window.after(self.interval, self.update_label)

    def update_label(self):
        self.i=self.i+1
        self.variable.set(str(self.i))
        #self.window.after(self.interval, self.update_label)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("800x480+0+0") # widthxheight+X+Yposition (not allowd space/Capital)
    MainWindow(root, cv2.VideoCapture(0))
    root.mainloop()