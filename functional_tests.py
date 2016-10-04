# _*_ coding:utf-8 _*_

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """
        就算 test 出错,这两个方法也会照样执行
        唯一例外:就是 setUp()自己出了异常,后面的就不执行了
        类似与: try/finally
        """
        self.browser = webdriver.Firefox()
        # 隐式等待 Selenium 测试中经常用到的方法
        # 告诉 Selenium 如果需要就等待 3s
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项引用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含 "TO-Do" 这个词
        # unittest 有很多这种断言函数:
        # assertEqual\assertTrue\assertFalse...
        self.assertIn('To-Do', self.browser.title)

        # fail() 测试失败,生成错误信息
        self.fail('Finish the test!')


if __name__ == '__main__':
    # 这函数会自动运行 测试类和方法
    # warning='ignore' 禁止抛出 ResourceWarning 异常
    # 现在的版本 可以不用这个参数
    unittest.main()
