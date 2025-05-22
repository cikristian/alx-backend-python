def stream_users():
    # Simulated user data (e.g., dictionaries, but can be just names or ages too)
    users = [
        {"id": 1, "name": "Alice", "age": 24},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 22},
        {"id": 4, "name": "Diana", "age": 27},
        {"id": 5, "name": "Eve", "age": 35},
        {"id": 6, "name": "Frank", "age": 29},
        {"id": 7, "name": "Grace", "age": 26}
    ]

    for user in users:
        yield user
