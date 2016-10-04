# _*_ coding:utf-8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 应用邀请她输入一个代表事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # 她在一个文本框中输入了 "Buy peacock feathers"
        # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        # # 这是 selenium 在输入框输入内容的方法
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后,页面更新了
        # 待办事项表格中显示了 "1. Buy peacock feathers"
        # 不但可以输入内容,还可以发送 特殊的按键,如ENTER/CTRL等修改键
        inputbox.send_keys('keys.ENTER')

        table = self.browser.find_element_by_id('id_list_table')    # 找不到触发异常
        rows = table.find_elements_by_tag_name('tr')    # 找不到返回一个 空 list
        # any()生成器表达器,类似于 列表推导,但更出色
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows), "New to-do item did not appear in table")

        # 页面中又显示了一个文本框,可以输入其他的待办事项
        # 她输入了 "Use peacock feathers to make a fly"
        # 伊迪丝做事很有条理
        # fail() 测试失败,生成错误信息
        self.fail('Finish the test!')

        # 页面再次更新,她的清单中显示了这两个待办事项
        [...]


if __name__ == '__main__':
    # 这函数会自动运行 测试类和方法
    # warning='ignore' 禁止抛出 ResourceWarning 异常
    # 现在的版本 可以不用这个参数
    unittest.main()
