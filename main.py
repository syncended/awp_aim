from ctypes import windll
from time import sleep
from aim import Aim

aim = Aim()
while True:
    #6 - номер доп. кнопки, замените на нужную
    if windll.user32.GetKeyState(6) != 0 and windll.user32.GetKeyState(6) != 1 and aim.stop:
        print('started')
        aim = Aim()
        aim.start()
    #6 - номер доп. кнопки, замените на нужную
    elif windll.user32.GetKeyState(6) != 0 and windll.user32.GetKeyState(6) != 1:
        print('stoped')
        aim._stop()
    sleep(0.1)
