# part of lists as stacks and queues lecture

# Tom is working at the supermarket, and he needs your help to keep track of his clients. Write a program that reads lines of input
# consisting of a customer's name and adds it to the end of a queue until "End" is received. If, in the meantime, you receive the command
# "Paid", you should print each customer in the order they are served (from the first to the last one) and empty the queue.

# When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining.".

from collections import deque

shop_queue = deque()
# print(shop_queue)

while (command := input()) != "End":
    # print(shop_queue.popleft())
    if command == "Paid":
        while shop_queue:
            print(shop_queue.popleft())
    else:
        shop_queue.append(command)

print(f"{len(shop_queue)} people remaining.")



