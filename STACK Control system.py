size = 5
top, base = 0, 0
stack = [None for i in range(size)]

# ADD TO STACK
def Push(item):
    global top
    if top < size:
        stack[top] = item
        print(f"+ added {item} to stack")
        top += 1
    else:
        print("\n ! ERROR : stack is full")
    Display(stack)

# REMOVE FROM STACK
def Pop():
    global top
    if top == 0:
        print("\n ! ERROR : stack is empty")
    else:
        top -= 1
        stack[top] = None
        print(f"- removed {stack[top]} from stack")
        Display(stack)
        return stack[top]

# DISPLAY STACK
def Display(Stack):
    print(f"stack contents : {Stack}\n")

# STACK INTERACTION
print("STACK SESSION STARTED  \nTYPE (+value) to add value to stack  \nTYPE (-) to remove value from stack\n\ne.g +5 adds to stack")

for i in range(10):
    inp = input("Enter command : ")
    # validating input
    if inp[0] == '+':
        if inp[1:].isdigit():
            Push(int(inp[1:]))
        else:
            print(" ! ERROR : can only add numbers to stack")
        
    elif inp[0] == '-':
        Pop()
    else: 
        print("invalid command")
print("\n\n! SESSION ENDED")
