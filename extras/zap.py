import webbrowser
import pyautogui
import time


n = 5519999508640
telefone = 5519998120926
link = f"http://web.whatsapp.com/send?phone={telefone}"
webbrowser.open(link)
time.sleep(8)

pyautogui.typewrite("oi, essa mensagem foi enviada por programacao")
pyautogui.press("enter")

time.sleep(2)
