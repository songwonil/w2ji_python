'''
Created on 2020. 1. 22.

@author: User
'''

from tkinter import  *
from tkinter import ttk

# 함수 추가.
def button_pressed(val):
    print(val,"pressed")

#함수 추가할 부분
root = Tk()
root.title("계산기")
root.geometry("400x300")

#숫자 및 결과 표시창
number_entry = ttk.Entry(root , width=20)
number_entry.grid(row=0 , columnspan=1)

#숫자버튼
# command=lambda:뒤에 명령어 작성
button1 = ttk.Button(root , text ="1" , command=lambda:button_pressed("1"))
button1.grid(row=1 , column=0)
button2 = ttk.Button(root , text ="2" , command=lambda:button_pressed("2"))
button2.grid(row=1 , column=1)

#인터페이스(버튼 , 창) 추가 부분
root.mainloop()