# -*- coding: UTF-8 -*-

from win32com.client import DispatchEx  # DispatchEx创建多线程应用，Dispatch创建单线程应用


def wordtopdf(path, path1, filename):
    w = DispatchEx("Word.Application")
    # w.visible = 1  # 显示Excel
    # path = r'C:\Users\Administrator\Desktop\值班表\新建文件夹\test.docx'
    doc = w.Documents.Open(path, ReadOnly=1)  # 打开文件
    doc.ExportAsFixedFormat(OutputFileName=path1 + "/" + filename + ".pdf",  # 输出文件路径及文件名
                            ExportFormat=17)  # 代码17为转换成pdf，代码18为转换成pws
    print("操作完成")
    w.Quit()


def Exceltopdf(path, path1, filename):
    app = DispatchEx("Excel.Application")
    # app.visible = 1  # 显示Excel
    # path = r'C:\Users\Administrator\Desktop\值班表\新建文件夹\12312.xls'
    wb = app.workbooks.Open(path, ReadOnly=1)       # 打开文件
    # print(type(wb))
    wb.ExportAsFixedFormat(0, path1 + "/" + filename)   # 保存，参数0表示保存为pdf，第二个参数为保存路径
    print("操作完成")
    app.Quit()


def copy(path, path1, filename):
    # path = r'C:\Users\Administrator\Desktop\值班表\新建文件夹\12312.xls'
    with open(path, 'rb') as rstream:       # 只读打开原文件
        container = rstream.read()      # 读取原文件放进容器
        # path1 = r'C:\Users\Administrator\Desktop\值班表\12312.xls'
        with open(path1 + "/" + filename, 'wb') as wstream:  # 打开新文件
            wstream.write(container)        # 新文件中写入容器内容
    print("操作完成")


if __name__ == '__main__':
    pass
