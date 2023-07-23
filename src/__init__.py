from .build_nested_path import crawl_directories
from .md_to_html import markdown_to_html
from .tree_node import TreeNode
from typing import Optional
import os

def build_html_tree(directory_path: str) -> Optional[TreeNode]:
    root = crawl_directories(directory_path)
    if not root:
        return None

    def build_html_tree_helper(node: TreeNode) -> None:
        for child in node.children:
            if child.children:
                build_html_tree_helper(child)
            else:
                file_path = os.path.join(directory_path, child.name)
                with open(file_path, "r") as f:
                    child.name = markdown_to_html(f.read())

    build_html_tree_helper(root)
    return root