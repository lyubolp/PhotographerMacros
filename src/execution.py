"""
Modules containing all execution logic for Presets, Queries and Folder operations
"""
import os
from typing import List, Optional
from PIL import Image

from src.folder_operations import BaseOperation, BaseCriteria
from src.query import Query


# TODO: Add error handling
def execute_query(query_name: str, queries: List[Query], source_image: str):
    """
    Executes a query on an image
    """
    print([q.name for q in queries])
    if query_name not in [q.name for q in queries]:
        raise ValueError("Invalid query name")

    with Image.open(source_image) as image:
        query = [q for q in queries if q.name == query_name][0]
        value = query.executable(image)
        return value

# TODO: Add error handling
def execute_folder_operation(operation: BaseOperation, source_dir: str, destination_dir: str = '',
                             criteria: Optional[BaseCriteria] = None):
    """
    Executes a folder operation on a directory
    """
    if criteria is not None:
        files = criteria.filter(source_dir)
    else:
        files = os.listdir(source_dir)

    for filepath in files:
        source_path = os.path.join(source_dir, filepath)
        destination_path = os.path.join(destination_dir, filepath)

        operation.execute(source_path, destination_path)
