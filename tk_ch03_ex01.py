# 버튼 위젯
# tk_ch03_ex01.py

import tkinter as tk

# 창 생성
win = tk.Tk()
win.geometry('200x100')
win.title('Button Widget')

# 버튼 위젯 추가
btn_ok = tk.Button(text='확인' , width=10, height=3)

# 창 위젯 표시
btn_ok.pack()

# 창 실행
win.mainloop()