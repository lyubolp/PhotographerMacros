"""
Modules containing all execution logic for Presets and Queries
"""
from typing import List
from PIL import Image

from query import Query


# TODO: Add error handling
def execute_query(query_name: str, queries: List[Query], source_image: str):
    print([q.name for q in queries])
    if query_name not in [q.name for q in queries]:
        raise ValueError("Invalid query name")
    
    with Image.open(source_image) as im:
        query = [q for q in queries if q.name == query_name][0]
        value = query.executable(im)
        return value
