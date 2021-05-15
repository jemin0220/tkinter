import tkinter as tk
win = tk.Tk()
win.geometry('300x200')
win.title('버튼 위젯 소개')

def quit():
    win.quit()

btn_quit = tk.Button(text='종료', command=quit , width=10, height=3)
lbl_button = tk.Label(text='종료 버튼을 누르면 창을 종료합니다.', padx=3, pady=3, fg='yellow', bg='black')

lbl_button.pack()
btn_quit.pack()

win.mainloop()