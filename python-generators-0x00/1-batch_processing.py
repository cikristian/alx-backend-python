#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    processing.batch_processing(50)
except BrokenPipeError:
    sys.stderr.close()

    def stream_users_in_batches(batch_size):
    # Simulated data source: List of user ages
    user_ages = [18, 22, 30, 40, 24, 26, 19, 60, 25, 45, 20, 29, 32, 21, 27, 55]

    batch = []
    for age in user_ages:
        batch.append(age)
        if len(batch) == batch_size:
            yield batch
            batch = []

    if batch:
        yield batch

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for age in batch:
            if age > 25:
                print(age)
