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
        for key in self.props.keys():
            props_html += f' {key}="{self.props[key]}"'
        return props_html

    def __repr__(self):
        return f'HtmlNode({self.tag}, {self.value}, {
            self.children}, {self.props})'
