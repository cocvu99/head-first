import os
os.getcwd()
os.chdir('D:\head-first\python\chapter3\HeadFirstPython\chapter3')
os.getcwd()
data = open('sketch.txt')
for each_line in data:
        if not each_line.find(':') == -1:
                (role, line_spoken) = each_line.split(':', 1)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
data.close()
