# Дополните приведенный код, используя списочное выражение, так чтобы получить список всех чисел-палиндромов от
# 100 до 1000 (включительно).
# Примечание. Результирующий список должен состоять из целых чисел.

palindromes = [_ for _ in range(100, 1001) if str(_) == str(_)[::-1]]
print(palindromes)