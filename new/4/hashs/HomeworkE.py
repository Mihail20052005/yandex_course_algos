def count_palindromic_substrings(s):
    n = len(s)
    count = 0

    # Для нечетной длины
    for i in range(n):
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    # Для четной длины
    for i in range(n - 1):
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count

# Чтение входных данных
input_string = input().strip()

# Вызываем функцию и выводим результат
result = count_palindromic_substrings(input_string)
print(result)
