"""读取整个文件"""


class FileReader:
    def __init__(self):
        self.fileName = 'pi_digits.txt'

    def readFile(self):
        with open(self.fileName) as file_object:
            contents = file_object.read()

        """read()函数到达文件末尾返回一个空字符串，删除空字符串可以使用rstrip()"""
        print(contents.rstrip())

    """逐行读取"""

    def read_file_line(self):
        with open(self.fileName) as file_object:
            for line in file_object:
                print(line.rstrip())

    """创建一个包含文件各行内容的列表"""

    def read_file_line_list(self):
        with open(self.fileName) as file_object:
            """readlines()将读取的行写入列表"""
            lines = file_object.readlines()

        for line in lines:
            print(line.rstrip())

    """使用文件中的内容"""

    def read_file_line_list_use(self):
        with open(self.fileName) as file_object:
            lines = file_object.readlines()
        pi_string = ''
        for line in lines:
            """去掉变量左边的空格 strip()"""
            pi_string += line.strip()
        print(pi_string)

    """处理包含一百万位大型文件"""
    def read_big_file(self):
        self.fileName = 'pi_million_digits.txt'
        with open(self.fileName) as file_object:
            lines = file_object.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.strip()
        print(f"{pi_string[:52]}")

    """判断圆周率中是否包含自己的生日"""
    def birthday_is_exist(self):
        self.fileName = 'pi_million_digits.txt'
        with open(self.fileName) as file_object:
            lines = file_object.readlines()
        pi_string = ''
        for line in lines:
            pi_string += line.strip()
        birthday = input("Enter your birthday,in the form mmddyy:")
        if birthday in pi_string:
            print("Your birthday appears in the first million digits of pi!")
        else:
            print("Your birthday does not appear in the first million digits of pi.")

file_reader = FileReader()
file_reader.readFile()
file_reader.read_file_line()
file_reader.read_file_line_list()
file_reader.read_file_line_list_use()
file_reader.read_big_file()
file_reader.birthday_is_exist()
