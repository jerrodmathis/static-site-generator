import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode('p', 'test value')
        node2 = HtmlNode('a', 'test link', None, {
            'href': 'https://www.google.com', 'target': '_blank'})
        node3 = HtmlNode(None, None, [node, node2], None)
        print(node)
        print(node2)
        print(node3)
