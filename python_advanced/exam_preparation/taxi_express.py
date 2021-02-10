from collections import deque


# 2. Sum the clients (each client is represented with minutes needed to reach his destination):
def total_mins_for_all_clients(client_list):
    return sum(client_list)


# 3. Try to do the course with the current client:
def take_a_course(client, taxi):
    if client <= taxi:
        return True
    return False


# 1. Read the customers and the taxis:
clients = deque([int(x) for x in input().split(', ')])
taxis = deque([int(x) for x in input().split(', ')])

total_mins = total_mins_for_all_clients(clients)

while taxis and clients:
    current_client = clients.popleft()
    current_taxi = taxis.pop()
    if take_a_course(current_client, current_taxi):
        continue
    else:
        clients.appendleft(current_client)

if not clients:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_mins} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in clients])}")
