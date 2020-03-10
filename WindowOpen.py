#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author 弈云

import autolog as au
import requests
import re
import webbrowser
import tkinter as tk
import tkinter.messagebox

user_data = []
def read_user_data():
    f = open(r'C:\Users\23567\Desktop\python test\test.txt', 'r', encoding='utf-8')
    for data in f.readlines():
        if len(data) != 0:
            user_data.append(data.strip('\n'))
    f.close()


def main():

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('自动登陆器')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x250')  # 这里的乘是小x

    # 第5步，用户信息
    tk.Label(window, text='Class ID:', font=('Arial', 14)).place(x=5, y=5)
    tk.Label(window, text='Account:', font=('Arial', 14)).place(x=5, y=45)
    tk.Label(window, text='Password:', font=('Arial', 14)).place(x=5, y=85)

    # 课程ID
    var_class_id = tk.StringVar()
    var_class_id.set(user_data[0])
    entry_class_id = tk.Entry(window, textvariable=var_class_id, font=('Arial', 14))
    entry_class_id.place(x=120, y=5)
    # 用户名

    var_account = tk.StringVar()
    var_account.set(user_data[1])
    entry_account = tk.Entry(window, textvariable=var_account, font=('Arial', 14))
    entry_account.place(x=120, y=45)
    # 用户密码
    var_password = tk.StringVar()
    var_password.set(user_data[2])
    entry_password = tk.Entry(window, textvariable=var_password, font=('Arial', 14))
    entry_password.place(x=120, y=85)

    def login():
        user1 = au.User(entry_class_id.get(), entry_account.get(), entry_password.get())
        responseRes = requests.post(user1.postUrl, data=user1.postData, headers=user1.header)

        if tkinter.messagebox.askyesno(title='提示', message='是否保存密码？'):
            f = open(r'C:\Users\23567\Desktop\python test\test.txt', 'w', encoding='utf-8')
            f.write(entry_class_id.get() + '\n' + entry_account.get() + '\n' + entry_password.get())
            f.close()

        pattern = re.compile(r'gensee://6170.*3b0a')
        url = re.findall(pattern, responseRes.text)
        # print(url)
        if len(url) != 0:
            webbrowser.open(url[0], new=0, autoraise=True)
        else:
            tkinter.messagebox.showerror(title='ID或密码错误', message='请重新输入')

    log = tk.Button(window, text='Login', font=('Arial', 12), width=10, height=3, command=login)
    log.place(x=365, y=25)

    # 第5步，主窗口循环显示
    window.mainloop()


if __name__ == "__main__":
    read_user_data()
    main()

