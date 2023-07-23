import os
from typing import Optional, Dict, Union, List

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

def build_tree(directory_path: str) -> Optional[TreeNode]:
    if not os.path.isdir(directory_path):
        return None

    root_name = os.path.basename(directory_path)
    root = TreeNode(root_name)

    contents = os.listdir(directory_path)
    for item in contents:
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path):
            child_tree = build_tree(item_path)
            if child_tree:
                root.add_child(child_tree)
        elif item.endswith(".md"):
            root.add_child(TreeNode(item))

    return root


# Example usage:
if __name__ == "__main__":
    content_dir = "/Users/abhinavmir/Desktop/Code/mfsg/tests/content"
    tree = build_tree(content_dir)
    if tree:
        print(tree)
