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


# 3. Користувач вводить з клавіатури рядок, слово для пошуку,
# слово для заміни. Зробіть у рядку заміну одного слова на інше.
# Отриманий рядок на екрані.

# try:
#     text = str(input("Input text: "))
#     search = str(input("Enter a search word: "))
#     replacement = str(input("Enter a replacement word: "))
#     newText = text.replace(search, replacement)
#     print(f"New text: {newText}")
# except Exception as Error:
#     print(f"ExceptionError: {Error}")

# 4. Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами
# (вважаючи, що індексація починається з 0, тому символи виводяться з першого).

# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.

try:
    text = "I love my home!"
    print(f"1.\t{text[2]}")
    print(f"2.\t{text[-2]}")
    print(f"3.\t{text[0:5]}")
    print(f"4.\t{text[:-2]}")
    print(f"5.\t{text[::2]}")
    print(f"6.\t{text[1::2]}")
    print(f"7.\t{text[::-1]}")
    print(f"8.\t{text[-1::-2]}")
    print(f"9.\t{len(text)}")
except Exception as Error:
    print(f"ExceptionError: {Error}")