def are_parentheses_balanced(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return "NO"
        else:
            stack.append(char)

    if not stack:
        return "YES"
    else:
        return "NO"

sequence = input()
print(are_parentheses_balanced(sequence))
