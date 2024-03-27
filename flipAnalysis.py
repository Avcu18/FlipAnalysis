from bs4 import BeautifulSoup
import requests

# funktioniert nur für flip.gg
url = 'https://flip.gg/wheel'

# Webseite abrufen
response = requests.get(url)
print(response.text)
#  check status 200
if response.status_code == 200:
    print('successful response!')
    soup = BeautifulSoup(response.text, 'html.parser')
   
    oberes_div = soup.find('div', class_='tss-visq3v-right MuiBox-root mui-0')
    print(oberes_div)
    if oberes_div:
        print('oberes <div>-Element gefunden.')
        innere_divs = oberes_div.find_all('div', class_='tss-1kk5vra-root MuiBox-root mui-y6ur6a')
        farben = []

   
        for div in divs:
  
            style = div.get('style')
        
        
            if style and 'background' in style:
                value = style.split('background:')[-1].split(';')[0].strip()
                farben.append(value)

        
            print(farben)
        else:
            print('Übergeordnetes <div>-Element wurde nicht gefunden.')
else:
    print(f'Fehler beim Abrufen der Webseite: Status Code {response.status_code}')