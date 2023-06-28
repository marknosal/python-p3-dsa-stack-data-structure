def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)

    reversed = ''
    while stack:
        reversed += stack.pop()
    
    print(reversed)

reverse_string('mark')


# def evaluate_keystrokes(string):
#     i = len(string) - 1
#     result = ''
#     skip = 0

#     while i >= 0:
#         if string[i] == '<':
#             skip += 1
#             i -= 1
#         else:
#             if skip > 0:
#                 i -= skip
#                 skip = 0
#             else:
#                 result = string[i] + result
#                 i -= 1
#     return result

def evaluate_keystrokes(string):
    stack = []
    for char in string:
        if char =='<':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)

    result = ''
    while stack:
        result = stack.pop() + result
    
    return result

sd = evaluate_keystrokes('<abcc<deff<')
print(sd)