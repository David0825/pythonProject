"""异常"""


class DivisionCalculator:
    def __init__(self):
        self.division = 0

    """处理ZeroDivisionError"""

    def zero_division_error(self):
        # print(5/0)
        """使用try-except代码块"""
        try:
            print(5 / 0)
        except ZeroDivisionError:
            print("you can't divide by zero!")

    """使用异常避免崩溃"""

    def use_Exception(self):
        print("Give me two numbers,and I'll divide them.")
        print("Enter 'q' to quit.")
        while True:
            first_number = input("\nFirst number：")
            if first_number == 'q':
                break
            second_number = input("\nSecond number：")
            if second_number == 'q':
                break
            answer = int(first_number) / int(second_number)
            print(answer)

    """else代码块"""

    def use_try_except_avoid_Exception(self):
        print("Give me two numbers,and I'll divide them.")
        print("Enter 'q' to quit.")
        while True:
            first_number = input("\nFirst number：")
            if first_number == 'q':
                break
            second_number = input("\nSecond number：")
            if second_number == 'q':
                break

            try:
                answer = int(first_number) / int(second_number)
            except ZeroDivisionError:
                print("you can't divide by 0!")
            else:
                print(answer)

    """处理FileNotFoundError异常"""
    def file_not_found_error(self):
        file_name = 'alice.txt'
        try:
            with open(file_name, encoding='UTF-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Sorry,the file {file_name} does not exist.")

    """分析文本"""
    def analysis_txt(self):
        file_name = 'alice.txt'
        try:
            with open(file_name, encoding='UTF-8') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"Sorry,the file {file_name} does not exist.")
        else:
            #计算该文件大致包含多少个单词
            words = contents.split()
            num_words = len(words)
            print(f"The file {file_name} has about {num_words} words.")


division_calculator = DivisionCalculator()
# division_calculator.zero_division_error()
# division_calculator.use_Exception()
# division_calculator.use_try_except_avoid_Exception()
# division_calculator.file_not_found_error()
division_calculator.analysis_txt()
