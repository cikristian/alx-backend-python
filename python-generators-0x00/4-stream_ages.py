def stream_user_ages():
    # Example dataset; in a real case this could come from a file, DB, or API stream
    user_ages = [25, 30, 22, 27, 35, 28, 31]
    for age in user_ages:
        yield age

def calculate_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age}")
    else:
        print("No user ages provided.")

calculate_average_age()
