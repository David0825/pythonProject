"""写入文件"""


class WriteMessage:

    def __init__(self):
        self.file_name = 'programming.txt'

    """写入空文件"""

    def write_file_by_file_not_exist(self):
        with open(self.file_name, 'w') as file_object:
            file_object.write('I love programming')

    """写入多行"""
    def write_file_more_line(self):
        with open(self.file_name,'w') as file_object:
            file_object.write('I love programming.\n')
            file_object.write('I love creating new games.\n')

    """附加到文件"""
    def write_message_file_append(self):
        with open(self.file_name,'a') as file_object:
            file_object.write("I also love finding meaning in large datasets.\n")
            file_object.write("I love creating apps that can run in a browser.\n")


write_message = WriteMessage()
write_message.write_file_by_file_not_exist()
write_message.write_file_more_line()
write_message.write_message_file_append()
