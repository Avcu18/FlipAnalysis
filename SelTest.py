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
    EC.presence_of_element_located((By.CLASS_NAME, 'tss-1kk5vra-root'))
)

# Hier eine Schleife, um auf das dynamische Laden von Inhalten zu warten und änderungen prüfen
elements = []
last_count = 0
start_time = time.time()
timeout = 10  
background_colors = []
while time.time() - start_time < timeout:
    elements = driver.find_elements(By.CSS_SELECTOR, '.tss-1kk5vra-root, .tss-13lu5i1-root, .tss-1epd446-root, .tss-on00c-root') #byclass kann nur eine klasse suchen, deshalb css selector
    current_count = len(elements)
    if current_count > last_count:
        print(f"Neue Elemente gefunden: {current_count} insgesamt.")
        last_count = current_count
    time.sleep(1)  

# Extrahiert die Hintergrundfarben der Elemente
for element in elements:
    background_color = driver.execute_script(
        "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", #bisschen komplexer => executen script im browser, welcher das erste argument (elemente) nimmt und basierend darauf die property value rein holt 
        element
    )
    background_colors.append(background_color)

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
driver.quit()
