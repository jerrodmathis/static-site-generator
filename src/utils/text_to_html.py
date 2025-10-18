from src.nodes.htmlnode import HtmlNode, LeafNode
from src.nodes.textnode import TextNode, TextType


def text_node_to_html_node(node: TextNode) -> HtmlNode:
    match (node.text_type):
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode('b', node.text)
        case TextType.ITALIC:
            return LeafNode('i', node.text)
        case TextType.CODE:
            return LeafNode('code', node.text)
        case TextType.LINK:
            return LeafNode('a', node.text, {'href': node.url})
        case TextType.IMAGE:
            return LeafNode(
                'img',
                '',
                {'src': node.url, 'alt': node.text}
            )
        case _:
            raise Exception('text_type not supported')
