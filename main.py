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


# Додатково:
# Є певний текст. Реалізуйте наступну функціональність:
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# ■ Порахуйте кількість знаків оклику в тексті.
#
# try:
#     text = '''the marathon took place on Route 5, attracting runners from across the country.
# participants received numbered bibs, making it easier for spectators to track their favorite athletes!!!'''
#
#     print(text.capitalize())
#
#     countDigit = 0
#     for i in text:
#         if i.isdigit():
#             countDigit += 1
#     print(f"Count digit = {countDigit}")
#
#     punctuation = set(".,;:!?")
#     countPunctuation = 0
#     for i in text:
#         if i in punctuation:
#             countPunctuation += 1
#     print(f"Count punctuation = {countPunctuation}")
#
#     print(f"Count = {text.count('!')}")
# except Exception as Error:
#     print(f"ExceptionError: {Error}")