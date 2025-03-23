"""
Wikiversity Pageview Analyzer
Assignment 10 - Regular Expressions & Log File Analysis
Python Version: 3.7.3

This script processes Wikimedia pageview log files (Sample Data 1 & 2).
It performs the following tasks:
1. Filters for 'en.v' domain records only.
2. Creates a dictionary of page_title -> total count_views.
3. Displays top 100 pages sorted by view count (and alphabetically if tied).
4. Parses page_titles to extract learning project names.
5. Creates and displays a dictionary of learning project -> total count_views.

All logic is modularized into separate functions for readability and reusability.
"""

import os
import re
from collections import defaultdict
from typing import Dict, List, Tuple

def parse_log_line(line: str) -> Tuple[str, str, int]:
    """Parses a single log line into domain, title, and count using RegEx."""
    match = re.match(r'^(\S+)\s+(\S+)\s+(\d+)\s+\d+$', line)
    if match:
        domain, title, views = match.groups()
        return domain, title, int(views)
    return '', '', 0

def extract_pageviews_by_title(file_paths: List[str]) -> Dict[str, int]:
    """Returns a dictionary of page_title -> total view count for en.v domain."""
    pageviews = defaultdict(int)
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                domain, title, views = parse_log_line(line)
                if domain == 'en.v':
                    pageviews[title] += views
    return pageviews

def display_top_entries(data: Dict[str, int], top_n: int = 100) -> List[Tuple[str, int]]:
    """Returns the top N entries sorted by value (desc) and key (asc)."""
    return sorted(data.items(), key=lambda x: (-x[1], x[0]))[:top_n]

def extract_learning_projects(pageviews: Dict[str, int]) -> Dict[str, int]:
    """Aggregates pageviews by learning project (base title before any slash)."""
    projects = defaultdict(int)
    for full_title, views in pageviews.items():
        base_title = re.match(r'^([^/]+)', full_title).group(1)
        projects[base_title] += views
    return projects

def main():
    files = ['Sample Data 1.txt', 'Sample Data 2.txt']
    pageview_data = extract_pageviews_by_title(files)
    
    print("Top 100 Individual Pages by Views:\n")
    for title, views in display_top_entries(pageview_data):
        print(f"{title}: {views}")

    project_data = extract_learning_projects(pageview_data)

    print("\nTop 100 Learning Projects by Views:\n")
    for project, views in display_top_entries(project_data):
        print(f"{project}: {views}")

if __name__ == '__main__':
    main()
