from typing import Self, Dict, List, Optional


class HtmlNode():
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List[Self]] = None,
        props: Optional[Dict] = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_html = ''
        if self.props:
            for key in self.props.keys():
                props_html += f' {key}="{self.props[key]}"'
        return props_html

    def __repr__(self):
        return f'HtmlNode({self.tag}, {self.value}, {
            self.children}, {self.props})'


class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: Optional[Dict] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError('LeafNode must have a value')
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HtmlNode):
    def __init__(
        self,
        tag: str,
        children: List[HtmlNode],
        props: Optional[Dict] = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('ParentNode must have a tag')
        if not self.children:
            raise ValueError('ParentNode must have children')
        html = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html += child.to_html()
        html += f'</{self.tag}>'
        return html
