def letters_count(n):
    content = n[1:-1]
    if not content:
        return 0
    letters = content.split(', ')
    unique_letters = set(letters)
    return len(unique_letters)
  
n = input().strip()
print(letters_count(n))