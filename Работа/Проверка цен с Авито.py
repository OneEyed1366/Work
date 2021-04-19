import re, bs4, dialogs, urllib3, certifi, clipboard, shortcuts

#Получаем ссылку, заходим по адресу и получаем значение "цена" из контейнера
def base_data(link):
    soup_data = bs4.BeautifulSoup(
        urllib3.PoolManager(
            ca_certs=certifi.where()).request(
                'GET', link).data, 'html5lib').text
    
    print(
        re.findall(
            r'[0-9]{6,10}', re.findall(
                'dataLayer.+', soup_data)[0])[1])
                
def link_check():
    if re.findall(r'https\:\/\/www\.avito\.ru.+', clipboard.get()):
        base_data(clipboard.get())
    else:
        dialogs.hud_alert('Здесь ничего нет! 🥺')
        
link_check()
