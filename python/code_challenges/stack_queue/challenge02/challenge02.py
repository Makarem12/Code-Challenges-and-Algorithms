# Write here the code challenge solution
def is_valid(s):
    """
    Determine if the input string s containing just the characters
    '(', ')', '{', '}', '[' and ']' is valid.
    
    An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    
    Parameters:
    s (str): The input string containing brackets.
    
    Returns:
    bool: True if the string is valid, False otherwise.
    
   
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        elif char in bracket_map.values():
            stack.append(char)
    
    return not stack

# Test cases
if __name__ == "__main__":
    print(is_valid("()"))         # Output: True
    print(is_valid("()[]{}"))     # Output: True
    print(is_valid("[({}]"))      # Output: False
    print(is_valid("[(hello)()]")) # Output: True
