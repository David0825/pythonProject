# 导入unittest
import unittest
import name_function as name


# 继承unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗"""
        formatted_name = name.get_formatted_name('Janis', 'joplin')
        # 断言
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确处理像 Wolfgang Amadeus Mozart这样的姓名吗？"""
        fomatted_name = name.first_last_middle_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(fomatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main
