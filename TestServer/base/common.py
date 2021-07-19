import platform


# 判断是否是windows环境
def isMyWindows():
    if platform.system() == 'Windows':
        return True
    else:
        return False
