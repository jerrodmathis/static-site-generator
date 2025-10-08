import unittest


from src.textnode import TextNode, TextType
from src.utils import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, 'This is a text node')

    def test_bold(self):
        node = TextNode('bolded text', TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'bolded text')

    def test_italic(self):
        node = TextNode('italicized text', TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'italicized text')

    def test_code(self):
        node = TextNode('print(x + y)', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'print(x + y)')

    def test_link(self):
        node = TextNode('Google', TextType.LINK,
                        'https://www.google.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'Google')
        self.assertEqual(
            html_node.props,
            {'href': 'https://www.google.com'}
        )

    def test_image(self):
        node = TextNode('dog', TextType.IMAGE,
                        'https://dog.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(
            html_node.props,
            {'src': 'https://dog.com', 'alt': 'dog'}
        )

    def test_nonexistent(self):
        node = TextNode('heading', 'HEADING')
        self.assertRaises(Exception, text_node_to_html_node, node)


if __name__ == '__main__':
    unittest.main()
