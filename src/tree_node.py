import os
from typing import Optional, Union

class TreeNode:
    def __init__(self, name: str):
        self.name = name
        self.children: List[TreeNode] = []

    def add_child(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def __repr__(self, level: int = 0) -> str:
        result = "  " * level + f"- {self.name}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result