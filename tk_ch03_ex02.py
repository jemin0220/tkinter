import tkinter as tk

# 버튼 클ㄹ릭 함수 change_msg
def change_msg():
    print('click', btn_ok['text'])
    if btn_ok['text'] == '클릭':
        btn_ok.config(text='확인')
    else:
        btn_ok.config(text='클릭')
        
    

win = tk.Tk()
win.geometry('200x100')
win.title('Button Widget')

btn_ok = tk.Button(text='확인', command=change_msg, width=10, height=3)

btn_ok.pack()

btn_ok.mainloop()