def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry,the file {filename} does not exist.")
    else:
        # 计算该文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


"""静默失败 pass占位符"""
def count_words_error(filename):
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # 计算该文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddharth.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    count_words_error(filename)
