import requests
import json

#запит до API Breaking Bad Quotes
response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")


if response.status_code == 200:
    data = response.json()
    quote = data[0]["quote"] 
    author = data[0]["author"]

    #виводимо цитату на екран
    print(f'"{quote}" — {author}')

    # Сейв цитати в файл
    with open("quote.txt", "w", encoding="utf-8") as file:
        file.write(f'"{quote}" — {author}')
else:
    print("Помилка отримання цитати")
def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        words = text.split()
        return len(words)
    except FileNotFoundError:
        return "Файл не знайдено."

file_name = "quote.txt"
word_count = count_words(file_name)
print(f"Кількість слів у файлі '{file_name}': {word_count}")
