import os
import sys


def FilePath():
    path = os.path.dirname(sys.argv[0])
    file_path = os.path.join(path, 'statistic.ini')
    return file_path

def ResertStatistic():
    path = os.path.dirname(sys.argv[0])
    with open(path + '\statistic.ini', 'w+') as file:
        file.writelines('')
