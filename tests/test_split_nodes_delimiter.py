import unittest

from src.nodes.textnode import TextNode, TextType
from src.utils.split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_not_text_type(self):
        node1 = TextNode("bolded", TextType.BOLD)
        node2 = TextNode("code", TextType.CODE)
        node3 = TextNode("italic", TextType.ITALIC)
        old_nodes = [node1, node2, node3]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertListEqual(old_nodes, new_nodes)

    def test_no_delimiter(self):
        node = TextNode("this doesn't contain a delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual([node], new_nodes)

    def test_convert_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ]
        )

    def test_with_multiple_delimiters(self):
        node = TextNode(
            "This is text **with** multiple delimiters **within** it.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text ", TextType.TEXT),
                TextNode("with", TextType.BOLD),
                TextNode(" multiple delimiters ", TextType.TEXT),
                TextNode("within", TextType.BOLD),
                TextNode(" it.", TextType.TEXT),
            ]
        )

    def test_with_start_del(self):
        node = TextNode("**bolded** text is in this sentence", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("bolded", TextType.BOLD),
                TextNode(" text is in this sentence", TextType.TEXT)
            ]
        )

    def test_with_back_to_back(self):
        node = TextNode("**bold****text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("bold", TextType.BOLD),
                TextNode("text", TextType.BOLD)
            ]
        )


if __name__ == '__main__':
    unittest.main()
