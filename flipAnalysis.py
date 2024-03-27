from bs4 import BeautifulSoup
import requests

# funktioniert nur für flip.gg
url = 'https://flip.gg/wheel'

# Webseite abrufen
response = requests.get(url)

#  check status 200
if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

 
    divs = soup.find_all('div', class_='tss-visq3v-right MuiBox-root mui-0')

    farben = []

   
    for div in divs:
  
        inner_divs = div.find_all('div', attrs={'bg': True})
        
        
        for inner_div in inner_divs:
            farbe = inner_div.get('bg')  # extract bg
            if farbe:  
                farben.append(farbe)

  
    print(farben)
else:
    print(f'Fehler beim Abrufen der Webseite: Status Code {response.status_code}')
