import unittest

from src.nodes.htmlnode import HtmlNode, ParentNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode('p', 'test value')
        node2 = HtmlNode('a', 'test link', None, {
            'href': 'https://www.google.com', 'target': '_blank'})
        node3 = HtmlNode(None, None, [node, node2], None)
        print(node)
        print(node2)
        print(node3)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_no_value(self):
        node = LeafNode('p', None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, 'just a static value')
        self.assertEqual(node.to_html(), 'just a static value')

    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')

    def test_leaf_to_html_a(self):
        node = LeafNode('a', 'test link', {
                        'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">test link</a>'
        )

    def test_leaf_to_html_div(self):
        node = LeafNode('div', 'a div')
        self.assertEqual(node.to_html(), '<div>a div</div>')


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == '__main__':
    unittest.main()
