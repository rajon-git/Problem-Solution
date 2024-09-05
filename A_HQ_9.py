def find_execute_or_not(program):
    if 'H' in program or 'Q' in program or '9' in program:
        return 'YES'
    return 'NO'

program = input().strip()
result = find_execute_or_not(program)
print(result)