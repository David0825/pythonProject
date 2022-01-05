# 测试函数
# def get_formatted_name(first,last):
#     """生成整洁的姓名"""
#     full_name = f"{first} {last}"
#     return full_name.title()

# 未通过的测试
def get_formatted_name(first, last):
    """生成整洁的姓名"""
    full_name = f"{first} {last}"
    return full_name.title()


# 添加新函数
def first_last_middle_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
