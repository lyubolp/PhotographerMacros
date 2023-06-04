"""
Modules containing all execution logic for Presets and Queries
"""
from typing import List
from PIL import Image

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
