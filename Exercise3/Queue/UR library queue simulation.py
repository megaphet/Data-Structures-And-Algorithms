print("\nThis simple program uses a queue structure to simulate a queue at the UR library and prints the student at the front after the first one has been served.\n")
from collections import deque

# Initial queue
library_queue = deque()

# 3 students join
library_queue.append("Alice")
library_queue.append("Bob")
library_queue.append("Charlie")

# 1 student is served
served = library_queue.popleft()

# Who is now at the front?
front = library_queue[0]
print(f"Served: {served}")
print(f"Now at front there is: {front}")