print("\nThis simple program uses queue data structure 'airtel_queue' to simulate a queue at Airtel SIM swap service center and prints the customer served second.\n")
from collections import deque

# Airtel queue
airtel_queue = deque(["Eric", "Diane", "Kevin", "Amina", "John", "Teta"])

print(f"People in Airtel queue: {airtel_queue}")

# Serve first two customers
first_served = airtel_queue.popleft()
second_served = airtel_queue.popleft()

print(f"2nd served customer is: {second_served}")
