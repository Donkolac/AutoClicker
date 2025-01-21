import time
import threading
from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller

# 1) Данные

# 1.1) Переменные
mouse = Controller()
Keyboard = KeyboardController()
running = True
clicking = False
interval = 0.1
mouseButton = Button.left
toggleButton = None
ButtonKey = None
keyCheck = False
mouseCheck = True
hold = False
holding = False
trueHolding = False

# 2) Функции

def changeInterval(newInterval):
    """2.1)Обновляет интервал кликов"""
    global interval
    interval = newInterval

def stopProgramm():
    """2.2)Останавливает программу"""
    global running
    running = False

def start():
    """2.3)Запускает кликер"""
    global clicking
    clicking = True

def stop():
    """2.4)Останавливает кликер"""
    global clicking
    clicking = False

def mouseButtonChange(new_mouse_button):
    """2.5)Обновляет клавишу мыши"""
    global mouseButton
    mouseButton = new_mouse_button

def toggleClicking():
    """2.6)Переключает состояние кликера (включить/выключить)"""
    global clicking
    if clicking:
        clicking = False
    else:
        clicking = True

def changeToggleButton(new_toggle_button):
    """2.7)Меняет клавишу переключения состояния кликера"""
    global toggleButton
    toggleButton = new_toggle_button

def clicker():
    """2.8)Кликает, пока переменная clicking = True"""
    while running:
        if clicking:
            if mouseCheck:
                    mouse.click(mouseButton)
            if keyCheck:
                    Keyboard.press(ButtonKey)
                    Keyboard.release(ButtonKey)
        time.sleep(interval)


def activate(key):
    """2.9)Обработчик нажатия клавиш"""
    if key == toggleButton:
        activateType()


def keyboardListener():
    """2.10)Запуск слушателя клавиатуры"""
    with keyboard.Listener(on_press=activate) as listener:
            listener.join()

def mouseClicking(currentMouseCheck):
    """2.11)Обновление значения флажка использования мыши"""
    global mouseCheck
    mouseCheck = currentMouseCheck

def toggleHolding():
    """2.12)Удержание клавиши"""
    if running:
        global holding
        if hold:
            if mouseCheck:
                if holding:
                    mouse.release(mouseButton)
                    holding = False
                else:
                    mouse.press(mouseButton)
                    holding = True
            if keyCheck:
                if holding:
                    Keyboard.release(ButtonKey)
                    holding = False
                else:
                    Keyboard.press(ButtonKey)
                    holding = True

def changeHold(new_change_hold):
    """2.13)Обновляет значение флажка удержания"""
    global hold
    hold = new_change_hold

def changeKeyButton(new_key_button):
    """2.14)Обновляет значение повторяемой клавиши"""
    global ButtonKey
    ButtonKey = new_key_button
    print(ButtonKey)

def keyClicking(current_keycheck):
    """2.15)Обновляет значение флажка клавиатуры"""
    global keyCheck
    keyCheck = current_keycheck
    print(keyCheck)

def activateType():
    """2.16)Проверяет режим работы автокликера"""
    if hold:
        toggleHolding()
    else:
        toggleClicking()


# 3) Потоки

# 3.1)Поток для кликера
clickerThread = threading.Thread(target=clicker)
clickerThread.daemon = True
clickerThread.start()

# 3.2)Поток для слушателя нажатий
listenerThread = threading.Thread(target=keyboardListener)
listenerThread.daemon = True
listenerThread.start()