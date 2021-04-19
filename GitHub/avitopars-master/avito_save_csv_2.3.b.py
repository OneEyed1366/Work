import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):                               #функция с именем 'get_html' принимает аргумент 'url'
	r = requests.get(url)                        # переменная 'r ' включает в себя не структурированный текст из 'url' c помощью метода 'get'
	return r.text                                # и ф-ция возыращает нам переменную 'r' c методом 'text'

def get_total_pages(html):
	soup = BeautifulSoup(html, 'html5lib')           #функция генерирующая количество (общее) для парсинга страницы

	# total = soup.find('div', class_='js-pages pagination-pagination-2j5na')
	# print(total)
	# total = list(total)
	# total_pages = total[-10]
	# print(total)
	total_pages = 100
	return int(total_pages)

def write_csv(data):
	with open('avito.csv', 'a', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],
						data['price'],
						data['url'],
						data['hour']))

def get_page_data(html):
	soup = BeautifulSoup(html, 'html5lib')
	ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item_table')
	for ad in ads:
		try:
			title = ad.find('a', class_='snippet-link').get('title')
			
		except:
			title = 'none'
		try:
			url = 'https://www.avito.ru' + ad.find('a', class_='snippet-link').get('href')
		except:
			url = 'none'
		try:
			price = ad.find('div', class_='snippet-price-row').text.strip()
		except:
			price = 'none'
			
		try:
			hour = ad.find('div', class_='snippet-date-row').text
		except:
			hour = 'none'
			
		data = {'title' : title,
				'price' : price,
				'url' : url,
				'hour' : hour}
		write_csv(data)

def main():
	url = 'https://www.avito.ru'
	base_url = 'https://www.avito.ru/rossosh?q='  # решить с городами может быть словарь? можно организовать меню выбора с цифрами
	page_part = 'p='
	
	quest = input('Привет! Итак, что нужно найти?	')
	
	

	total_pages = get_total_pages(get_html(url))
	
	for i in range(1, total_pages):
		url_gen = base_url + quest + '&' + page_part + str(i) # | переменная генерирующая различные url в цикле, для дальнейшей с ними работой
		html = get_html(url_gen)                # \__________В ЭТОМ БЛОКЕ можно добавить возможность вводить вручную через функцию 'input()' 
		get_page_data(html)                     # /
		
		








if __name__ == '__main__':
	main()
