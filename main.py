# # 1. Користувач вводить рядок з клавіатури.
# # Порахуйте кількість літер, цифр у рядку.
# # Виведіть обидві кількості на екран. (використовувати цикл)
# try:
#     inputLines = str(input("Please, enter a line: "))
#     countLetter = 0
#     countNumber = 0
#     for i in inputLines:
#         if i.isalpha():
#             countLetter += 1
#         if i.isdigit():
#             countNumber += 1
#     print(f"Count letter = {countLetter};\nCount number = {countNumber}.")
# except Exception as Error:
#     print(f"ExceptionError : {Error}")

# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ.
# Отримане число виведіть на екран.

# try:
#     inputLine = str(input("Enter a line: "))
#     inputSearchSymbol = str(input("Enter search symbol: "))
#     print(f"Count search symbol = {inputLine.count(inputSearchSymbol)}")
# except Exception as Error:
#     print(f"ExceptionError : {Error}")
