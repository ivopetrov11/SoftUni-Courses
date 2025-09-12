# part of lists as stacks and queues lecture

# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

user_input = input()
index_stack = []

for index in range(len(user_input)):
    if user_input[index] == "(":
        index_stack.append(index)
    elif user_input[index] == ")":
        close_parentheses = index
        open_parentheses = index_stack.pop()
        print(user_input[open_parentheses:close_parentheses+1])
