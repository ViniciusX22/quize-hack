import pyautogui
import pytesseract
from google import google
import os
import io
# Descomente esta linha e altere o caminho para
# o local onde Tesseract está instalado, caso não esteja
# adicionado no PATH do sistema
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

fname = 'results.txt'

print('Localizando imagem na tela...')
imgLocation = pyautogui.locateOnScreen(
    'images/base_image.png', confidence=0.30, grayscale=False)
if imgLocation is not None:
    print('Capturando a tela...')
    img = pyautogui.screenshot('images/screenshot.png', region=imgLocation)
    print('Lendo texto...')
    text = pytesseract.image_to_string(img)
    print('Pesquisando pelo texto...')
    results = google.search(text)
    with io.open(fname, "w+", encoding="utf-8") as f:
        print('Salvando resultados...')
        f.write('Pesquisa feita: "%s"\n\n' % text)
        for result in results:
            f.write("Título: " + result.name)
            f.write("\nDescrição: %s\n\n" % result.description)
    os.system('notepad.exe results.txt')
else:
    print('Falha ao localizar imagem.')
