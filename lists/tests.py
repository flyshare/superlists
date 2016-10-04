from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page   # 在 views.py 中我们先 home_page,为了通过测试

# Create your tests here.


class HomePageTest(TestCase):
    """docstring for HomePageTest"""

    def test_root_url_resolves_to_home_page_view(self):
        """
        resolve() 是 Django内部函数,用于解析 url,并将其映射到相应的视图函数
        检查解析网站根目录'/'时,是否能找到名为 home_page()函数
        """
        found = resolve('/')
        # views 视图模块中的 home_page()函数
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """"""
        request = HttpRequest()
        # home_page()视图获取请求,返回响应.
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        # response.content 是 原始字节,不是 字符串,因此使用 b''
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
