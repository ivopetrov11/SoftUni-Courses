# part of lists as stacks and queues lecture

# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get
# water (each on a separate line) until you receive the command "Start". Add those people to a queue. Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".


from collections import deque

water_dispenser_capacity = int(input())

people = deque()
while (person := input()) != "Start":
    people.append(person)

while (command := input()) != "End":
    if command.isdigit():
        liters_needed = int(command)
        if liters_needed <= water_dispenser_capacity:
            print(f"{people.popleft()} got water")
            water_dispenser_capacity -= liters_needed
        else:
            print(f"{people.popleft()} must wait")
    else:
        refill_command, refill_liters = command.split()
        water_dispenser_capacity += int(refill_liters)

print(f"{water_dispenser_capacity} liters left")