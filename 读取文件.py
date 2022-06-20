# -*- coding: UTF-8 -*-

import os


def all_files_path(rootdir):
    filepaths: list[bytes | str] = []  # 初始化列表⽤来
    for root, dirs, files in os.walk(rootdir):  # 分别代表根⽬录、⽂件夹、⽂件
        # 遍历⽂件
        for file in files:
            # print(file)
            file_path = os.path.join(root, file)  # # 获取⽂件绝对路径
            filepaths.append(file_path)  # 将⽂件路径添加进列表
        for dir in dirs:  # 遍历⽬录下的⼦⽬录
            # print(dir)
            # dir_path = os.path.join(root, dir)  # 获取⼦⽬录路径
            all_files_path(dir)  # 递归调⽤
    return filepaths


if __name__ == "__main__":
    pass
