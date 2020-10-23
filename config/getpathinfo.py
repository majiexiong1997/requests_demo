import os

def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]

    return path

def get_result_path():
    str = r'C:\Users\majiexiong\PycharmProjects\requests_demo\result'
    path = os.listdir(str)

    return path




if __name__ == '__main__':
    print(get_result_path())