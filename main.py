# -*- coding: UTF-8 -*-
# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import tkinter as tk
import tkinter.filedialog
import 转PDF
from 读取文件 import all_files_path

root = tk.Tk()

root.withdraw()
path = tkinter.filedialog.askdirectory(title='请选择需打印的文件夹')
path2 = tkinter.filedialog.askdirectory(title='请选择输出PDF的文件夹')

if __name__ == '__main__':

    files = all_files_path(path)
    for file in files:
        type = str(file).split(".")[len(str(file).split(".")) - 1]
        print(file)
        filename = str(file).split(path)[len(str(file).split(path)) - 1]
        # print(filename)
        filename = filename.replace('\\', '').lstrip(' ')
        print(filename)
        # filename = str(file).split("\\")[len(str(file).split("\\")) - 1]
        # print(file)
        if '不打印' in file:
            print("此文件无需打印")
        else:
            if type == 'pdf':
                转PDF.copy(file, path2, filename)
            elif type == 'xls' or type == 'xlsx' or type == 'xlsm':
                转PDF.Exceltopdf(file, path2, filename)
            elif type == 'doc' or type == 'docx':
                转PDF.wordtopdf(file, path2, filename)
            elif type == 'zip' or type == 'rar' or type == '7z':
                pass
            else:
                转PDF.copy(file, path2, filename)
