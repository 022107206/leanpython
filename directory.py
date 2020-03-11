# os模块
import os

# 获取当前工作目录
print(os.getcwd())

# 更改目录
os.chdir('/Users/creed')
print(os.getcwd())

# 列出文件和目录
l = os.listdir('/Users/creed/workspace/git/leanpython')
for i in l:
    print(i)

# 新建目录
os.chdir('/Users/creed/workspace/git/leanpython')
# os.mkdir('test_mkdir')
c_dir = 'test1'
print(f'已经存在{c_dir}') if os.path.exists(c_dir) else os.mkdir(c_dir)

# 重命名目录
o_dir = 'test1'
n_dir = 'test2'
os.rename(o_dir, n_dir) if os.path.exists(o_dir) and not os.path.exists(n_dir) else print(f'已经存在{n_dir}或者没有{o_dir}')


# 创建新目录
def mk_dir(self):
    print('=== 创建目录 ===')
    if os.path.exists(self):
        print(f'目录{self}已经存在')
    else:
        os.mkdir(self)


# 删除目录
def del_dir(self):
    print('=== 删除目录 ===')
    if not os.path.exists(self):
        print(f'源目录{self}不存在')
    else:
        os.rmdir(self)


# 重命名目录
def rename_dir(old_dir, new_dir):
    # if os.path.exists(old_dir) and not os.path.exists(new_dir):
    #     os.rename(old_dir, new_dir)
    # else:
    #     print(f'已经存在{new_dir}或者没有{old_dir}')
    print('=== 重命名目录 ===')
    if not os.path.exists(old_dir):
        print(f'源目录{old_dir}不存在')
    elif os.path.exists(new_dir):
        print(f'目标目录{new_dir}已经存在')
    else:
        os.rename(old_dir, new_dir)
        print(f'源目录{old_dir}已经重命名为{new_dir}')


del_dir('test1_dir')
mk_dir('d1_dir')
rename_dir('d1_dir', 'd2_dir')

# 删除目录
d_dir = 'test2'
os.rmdir(d_dir)
print(os.listdir())
