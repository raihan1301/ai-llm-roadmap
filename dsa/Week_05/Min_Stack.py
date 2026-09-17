"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.


Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
At most 3 *10^4 calls will be made to push, pop, top, and getMin.
"""

class MinStack:

    def __init__(self):
        self.stack  = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        """
        now we know we have to find getmin also so we will check here if the push value is min in the list or not
        """

        if not self.min_stack:
            self.min_stack.append(val)
            """
            if min stack is empty this will be the smallest value
            """
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
        we need to find the latest push in the list not the max value
        """
        return self.stack[-1]

    def getMin(self) -> int:
      
        """
        min_value = min(self.stack )
        must run in O(1), so calling min(self.stack ) is too slow because it scans the whole stack each time.

        remember we already know which one is min from push function so,
        """
        return self.min_stack[-1]

"""
push 1
stack     = [1]
min_stack = [1]

push 2
stack     = [1, 2]
min_stack = [1, 1]

push 0
stack     = [1, 2, 0]
min_stack = [1, 1, 0]

After pop()
stack     = [1, 2]
min_stack = [1, 1]
top()    → 2
getMin() → 1
"""

def main():

    input1 = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

    minstack = MinStack()

    for index,word in enumerate(input1):
        if word == "push":
            minstack.push(input1[index+1])
        if word == "pop":
            minstack.pop()
        if word == "top":
            minstack.top()
        if word == "getMin":
            minstack.getMin()

main() 

"""
We create two stacks: stack stores the actual values, while min_stack stores the minimum value seen at each position. 
When we push a new number, we also push the smaller value between the new number and the previous minimum into min_stack. 
When we pop, we pop from both stacks so they stay synchronized. 
top() simply returns the last item in the normal stack, and getMin() returns the last item in min_stack, which is always the current minimum.
"""

"""
All required operations are O(1) time: push, pop, top, and getMin. 
Space complexity is O(n) because both stacks can grow with the number of pushed elements.
"""