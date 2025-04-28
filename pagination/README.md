# Pagination

This project focuses on implementing pagination techniques in a Python backend application. 

## Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Tasks

### 0. Simple helper function
- Implement a function `index_range` that takes two integer arguments `page` and `page_size`
- Return a tuple of size two containing a start index and an end index for pagination

### 1. Simple pagination
- Implement a Server class with a method `get_page` that returns the appropriate page of the dataset
- Handle page validation and edge cases

### 2. Hypermedia pagination
- Implement a `get_hyper` method that returns all necessary pagination information
- Include metadata like next/previous pages and total pages

### 3. Deletion-resilient hypermedia pagination
- Implement a deletion-resilient pagination system
- Handle cases where items might be removed between pagination requests 