import os, feedparser

if os.sys.platform == 'ios':
    os.chdir(
        os.path.join(
            '/private',
            'var',
            'mobile',
            'Library',
            'Mobile Documents',
            'iCloud~is~workflow~my~workflows',
            'Documents'
            )
        )
    
elif os.sys.platform == 'win32':
    os.chdir(
        os.path.join( 
            'C:\\',
            'Users',
            'proka',
            'iCloudDrive',
            'iCloud~is~workflow~my~workflows'
            )
        )

with open(
	os.path.join(
		'Данные для работы',
		'Социалочка',
		'Список RSS каналов.txt'
		), 'r+') as f:
			urls = str(f.read()).rsplit()

with open(
	os.path.join(
		'Данные для работы',
		'Социалочка',
		'Новости-уже было.txt'
		), 'a+') as f:
			f.close()

def parse():
	with open(
		os.path.join(
			'Данные для работы',
			'Социалочка',
			'Новости.txt'
			), 'w+') as f:
				for url in urls:
					for news_number in range(3):
						news = feedparser.parse(url)
						title = news.entries[news_number].title
						link = news.entries[news_number].link
						desc = news.entries[news_number].description
						
						with open(
							os.path.join(
								'Данные для работы',
								'Социалочка',
								'Новости-уже было.txt'
								), 'r+') as news_history:
									if title not in news_history.read():
										f.write(
											'{0}\\n\\n\"{2}\"\\n\\nСсылка на новость: {1}\n'.format(
												title, 
												link,
												desc
												)
											)

										news_history.write('{}\n'.format(title))
parse()
