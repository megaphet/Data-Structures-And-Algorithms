from collections import deque

# Airtel queue
airtel_queue = deque(["Eric", "Diane", "Kevin", "Amina", "John", "Teta"])

# Serve first two customers
first_served = airtel_queue.popleft()
second_served = airtel_queue.popleft()

print(f"1st served: {first_served}")
print(f"2nd served: {second_served}")