import tkinter as tk


class textFile:
    # 写入TXT功能
    @staticmethod
    def write_txt_data(data: str or int):
        with open('C:\\Users\\chencheng\\PycharmProjects\\adsTask\\taskCode\\config\\log.txt', "a", encoding="utf-8") as f:
            f.write(data + '\n')
            f.close()

    # 获取剪切板的内容
    @staticmethod
    def clipboard():
        root = tk.Tk()
        root.withdraw()  # to hide the window
        variable = root.clipboard_get()
        return variable
