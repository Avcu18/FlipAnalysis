from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# seite angeben, driver initialisieren und seite öffnen
url = 'https://flip.gg/wheel'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# checken ob min. ein element vorhanden ist. 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.tss-1kk5vra-root, .tss-13lu5i1-root, .tss-1epd446-root, .tss-on00c-root')) #hier schauen wir jz nach allen selektoren
)

# tracking durch unique set
element_ids = set()
background_colors = []


#logik geändert, damit es dauerhaft läuft + wir im array immer das neuste element haben 
try:
    while True: 
        new_elements = driver.find_elements(By.CSS_SELECTOR, '.tss-1kk5vra-root, .tss-13lu5i1-root, .tss-1epd446-root, .tss-on00c-root')
       # print(new_elements)
        for element in new_elements:
            if element.id not in element_ids:
                print("Neues Element gefunden.")
                element_ids.add(element.id)
                
                # Extrahiere die Hintergrundfarbe für jedes neue Element
                background_color = driver.execute_script(
                    "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", element #bisschen komplexer => executen script im browser, welcher das erste argument (elemente) nimmt und basierend darauf die property value rein holt 
                )
                background_colors.append(background_color)
                
        time.sleep(1)  

except KeyboardInterrupt:  # skript beenden durch ctrl + c 
    print("Beendet durch Benutzer.")
    


# hintergrund farben to names
farben = []
for color in background_colors:
    if color == 'rgb(69, 141, 191)':
        farben.append("Blau")
    elif color == 'rgb(177, 87, 206)':
        farben.append("Lila")
    elif color == 'rgb(46, 189, 80)':
        farben.append("Grün")
    elif color == 'rgb(253, 212, 41)':
        farben.append("Gelb")

# => array & beenden
print(farben)
print(len(farben))
driver.quit()
