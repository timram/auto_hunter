# Доаставать мыла магазов из статей, блогов и тд при помощи апи от https://hunter.io
# Usage
- Скопировать репозиторий
- Установка зависимостей: pip install -r dependecies
- Запуск: python hunter.py -u https://domain_example.com -o example -p parser -k your_api_key
# Result
В итоге в папке files появится файл example.csv - таблица с двумя колонками: shop_url, mails
# Parser
parser - это питоновский модуль, в котором должна быть описана функция getAnchors, которая в качестве параметра принимает объект BeautifulSoup(распаршенный html указанного урла) и возвращать список элементов с необходимым href атрибутом.
Пример:
~/auto_hunter/parser.py:
```python
def getAnchors(soup):
	return soup.find("div", class_="article__content").find_all("a")
```
