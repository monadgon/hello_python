# https://m.blog.naver.com/amethyst_lee/222011409761
import os
from tkinter import *

def btn_command():
    print("the button is clicked")

root = Tk()
root.title("한글 테스트")
root.geometry("800x800+0+0") # widthxheight+X+Yposition (not allowd space/Capital)
#root.resizable(False, True) # width, height resizable
btn1 = Button(root, text="Click Me!")
btn1.pack() # root에 btn1을 포함시킴

btn2 = Button(root, padx=5, pady=5, fg="white", bg="black", text="PaddingButton")
btn2.pack()
#[ToDo] 파일 위치를 실행 파일 위치와 같게 하는 방법 
photo = PhotoImage(file="C:\\PjtPython\\hello_python\\tkinter\\Gold_Star.png") #OK
btn3 = Button(root, image=photo, command=btn_command)
btn3.pack()

label1 = Label(root, text="hello")
label1.pack()

photo2 = PhotoImage(file="C:/PjtPython/hello_python/tkinter/iconfinder_star.png") #OK
label2 = Label(root, text="hello", image=photo2)
label2.pack()

root.mainloop() # 프레임(윈도우/창)이 종료 버튼을 기다림

