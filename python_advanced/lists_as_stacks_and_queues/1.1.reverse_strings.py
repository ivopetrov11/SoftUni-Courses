# part of lists as stacks and queues lecture

# Write a program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

user_input_stack = list(input())
while user_input_stack:
    print(user_input_stack.pop(), end='')