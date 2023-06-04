"""
Contains logic for parsing the queries saved in the JSON
"""
import json
from typing import List

from dominant_color import calculate_dominant_color
from query import Query

objects = {
    "dominant_color": calculate_dominant_color,
}


def load_queries(path="queries.json", objects_dict=None) -> List[Query]:
    """
    Parses the queries from a JSON file

    :param path: Path to the JSON file containing the file queries
    :param objects_dict: A mapping of the filters
        - contains tuples of the function to be called and the type
    :return: List containing `Query` instances
    """
    if objects_dict is None:
        objects_dict = objects

    with open(path) as file_handler:
        queries_dict = json.loads(file_handler.read())["queries"]

    result = []
    for query in queries_dict:

        name = query['name']
        del query['name']

        description = ""

        if 'description' in query:
            description = query['description']
            del query['description']

        query = Query(name, description, objects_dict[name])
        result.append(query)

    return result
