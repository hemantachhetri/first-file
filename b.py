#PROBLEM 1
input_str = "(((("
count_index = 0

for char in input_str:
    if char == "(":
        count = +1
        count_index = count_index +1

    elif char == ")":
        count = -1
        count_index = count_index -1
 
#print ("He is in ",count_index, "floor")

#PROBLEM 2
input_str = "((()))"
stack= []

while char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop()
        

print ('Length of stack:', stack)

    



