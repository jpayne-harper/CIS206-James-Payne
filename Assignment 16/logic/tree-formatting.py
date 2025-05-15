import json
import os
from collections import defaultdict, deque

# File path to JSON family tree
JSON_FILE = '/Users/jimmypayne/Desktop/Harper/CIS 206/Assignment 16/family_tree.json'


    
def load_family_data():
    """Load current family data or return an empty template."""
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"family": []}


def build_family_graph():
    """
    Build a graph representing parent-child relationships.
    Returns:
        - people: dict mapping full_name to person data
        - children_map: dict mapping parent full_name to list of their children
    """
    data = load_family_data()
    people = data["family"]
    peopleListed = {}
    parentsListed = []
    children_map = defaultdict(list)

    for person in people:
        full_name = person["full_name"]
        peopleListed[full_name] = person
        
        father = person.get("father", "").strip()
        mother = person.get("mother", "").strip()

        if father:
            children_map[father].append(full_name)
            parentsListed.append(father)
        if mother:
            children_map[mother].append(full_name)
            parentsListed.append(mother)

    peopleList = peopleListed.keys()
    oldest_generation = parentsListed - peopleList
    
    print(oldest_generation)
    print(peopleListed)
    return peopleListed, children_map


def find_roots(people, children_map):
    """
    Find people with no parents listed in the dataset —
    The missing members of the dataset are the oldest generation.
    Returns a list of full_names.
    """
    all_people = set(people.keys())
    child_set = set()

    for children in children_map.values():
        child_set.update(children)
        

    root_candidates = all_people - child_set
    return list(root_candidates)


def organize_generations():
    """
    Organize the family tree into generations.
    Returns a list of lists, where each inner list is a generation.
    """
    people, children_map = build_family_graph()
    roots = find_roots(people, children_map)

    print(roots)

    generations = []
    visited = set()
    queue = deque()

    # Start with roots
    for root in roots:
        queue.append((root, 0))  # (person_name, generation_level)

    while queue:
        person, level = queue.popleft()

        if person in visited:
            continue
        visited.add(person)

        # Extend generations list if needed
        while len(generations) <= level:
            generations.append([])

        generations[level].append(people[person])

        # Add children to queue for next generation
        for child in children_map.get(person, []):
            queue.append((child, level + 1))

    return generations


if __name__ == "__main__":
    generations = organize_generations()
    for i, gen in enumerate(generations):
        print(f"Generation {i+1}:")
        for person in gen:
            print(f" - {person['full_name']}")
