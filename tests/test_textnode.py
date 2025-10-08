import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode('test text', TextType.TEXT)
        node2 = TextNode('test', TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode('test text', TextType.TEXT)
        node2 = TextNode('test text', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode('test text', TextType.TEXT, 'https://www.test.com')
        node2 = TextNode('test text', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_default_url_none(self):
        node = TextNode('test text', TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_required_params(self):
        self.assertRaises(TypeError, TextNode)


if __name__ == '__main__':
    unittest.main()
