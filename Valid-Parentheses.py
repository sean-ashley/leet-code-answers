class Solution:
    def isValid(self, s: str) -> bool:
        #setup empty stacks
        stack  = []
        #make dict with open brackets
        brackets = {')':'(',']' : '[' , '}':'{'}
        
        if len(s) == 1:
            return False
        #loop thru string
        for i in s:
            #if its an open bracket, add it to the tack
            if i in brackets.values():
                stack.append(i)
            #if the stack is empty or if its a closing bracket with no open bracket equivalent at the top of the stack, its false
            elif stack == [] or brackets[i] != stack.pop():
                
                return False
        #if we make it thru the string and the stack is empty,  its good!
        return stack == []
