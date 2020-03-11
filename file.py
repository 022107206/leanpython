import shutil
import os


def touch_file(self):
    file = open(self, 'w')
    file.close()
    print('this is fun touch_file()')


touch_file('/Users/creed/a2')

if __name__ == '__main__':
    print('this is file.py')


# 新建文件
def mk_file(self):
    f = open(os.getcwd() + '/' + self, 'w')
    f.close()


# 复制文件
def copy_file(old_file, new_file):
    print('=== 复制文件 ===')
    if old_file not in os.listdir():
        print(f'源文件{old_file}不存在')
    elif new_file in os.listdir():
        print(f'目标文件{new_file}已经存在')
    else:
        shutil.copy(old_file, new_file)
        print(f'新文件{new_file}创建成功')


# 删除文件
def del_file(self):
    print('=== 删除文件 ===')
    if self not in os.listdir():
        print(f'源文件{self}不存在')
    else:
        os.remove(self)
        print(f'文件{self}删除成功')


# 移动文件/重命名文件
def move_file(old_file, new_file):
    print('=== 移动文件 ===')
    if old_file not in os.listdir():
        print(f'源文件{old_file}不存在')
    elif new_file in os.listdir():
        print(f'目标文件{new_file}已经存在')
    else:
        shutil.move(old_file, new_file)
        print(f'源文件{old_file}已经移到{new_file}')


mk_file('n1.txt')
copy_file('n2.txt', 'f1.txt')
move_file('f1.txt', 'f2.txt')
del_file('f3.txt')


