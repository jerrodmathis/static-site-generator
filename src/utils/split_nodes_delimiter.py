from src.nodes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        elif node.text.find(delimiter) == -1:
            new_nodes.append(node)
        else:
            nodes_to_transform = node.text.split(delimiter)
            for i in range(0, len(nodes_to_transform)):
                text = nodes_to_transform[i]
                if i % 2 == 0:
                    if len(text) > 0:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text, text_type))

    return new_nodes
