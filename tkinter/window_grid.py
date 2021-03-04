# https://m.blog.naver.com/amethyst_lee/222011409761
import os
from tkinter import *

root = Tk()
root.title("한글 테스트")
root.geometry("800x480+0+0") # widthxheight+X+Yposition (not allowd space/Capital)
#root.resizable(False, True) # width, height resizable

label1 = Label(root, text="left", width=50, height=5, fg="white", bg="red", relief="solid")
#label1.pack()
photo2 = PhotoImage(file="C:/PjtPython/hello_python/tkinter/iconfinder_star.png") #OK
label2 = Label(root, text="hello", image=photo2)
#label2.pack()

label1.grid(row=1, column=0, sticky=N+E+W+S)
label2.grid(row=1, column=1, sticky=N+E+W+S)
root.mainloop() # 프레임(윈도우/창)이 종료 버튼을 기다림