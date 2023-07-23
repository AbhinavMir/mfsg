import os
from typing import Optional
from .tree_node import TreeNode

def crawl_directories(directory_path: str) -> Optional[TreeNode]:
    if not os.path.isdir(directory_path):
        return None

    root_name = os.path.basename(directory_path)
    root = TreeNode(root_name)

    contents = os.listdir(directory_path)
    for item in contents:
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path):
            child_tree = crawl_directories(item_path)
            if child_tree:
                root.add_child(child_tree)
        elif item.endswith(".md"):
            root.add_child(TreeNode(item))

    return root
