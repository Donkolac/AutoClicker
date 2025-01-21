from tkinter import *
from tkinter import ttk
import AutoClicker
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button, Controller

from AutoClicker import mouse

# 1)Пространство

# 1.1)Название и разрешение
window = Tk()
window.title("Dk Auto Clicker")
window.iconbitmap('mouse.ico')
window.geometry('565x400')
window.minsize(width=565, height=400)
window.maxsize(width=565, height=400)


# 1.2)Рамки/контейнеры

# 1.2.1)Рамка времени
timeFrame = ttk.LabelFrame(window, height=100, relief='solid', text="Интервал")
timeFrame.place(x=10, y=5, width=545)
# Распределение пространства рамки между виджетами ->
timeFrame.grid_rowconfigure(0, weight=1)
timeFrame.grid_columnconfigure(0, weight=1)
timeFrame.grid_columnconfigure(1, weight=1)
timeFrame.grid_columnconfigure(2, weight=1)
timeFrame.grid_columnconfigure(3, weight=1)
timeFrame.grid_columnconfigure(4, weight=1)
timeFrame.grid_columnconfigure(5, weight=1)
timeFrame.grid_columnconfigure(6, weight=1)
timeFrame.grid_columnconfigure(7, weight=1)

# 1.2.2)Рамка выбора клавиши
keyEnterFrame = ttk.LabelFrame(window, height=150, relief='solid', text="Выбранная клавиша")
keyEnterFrame.place(x=10, y=110, width=150)
# Распределение пространства рамки между виджетами ->
keyEnterFrame.grid_columnconfigure(0, weight=1)
keyEnterFrame.grid_rowconfigure(0, weight=1)
keyEnterFrame.grid_rowconfigure(1, weight=1)

# 1.2.3)Рамка выбора кнопки активации
keyActivationFrame = ttk.Frame(window, width=275, height=120)
keyActivationFrame.place(anchor="e", relx=0.5, y=330)

# 1.2.3)Рамка для флажков
checksFrame = ttk.LabelFrame(window, width=385, height=150, relief='solid', text="Настройки использования")
checksFrame.place(x=169, y=110)
checksFrame.grid_propagate(False)
# Распределение пространства рамки между виджетами ->
checksFrame.grid_rowconfigure(0, weight=1)
checksFrame.grid_rowconfigure(1, weight=1)
checksFrame.grid_columnconfigure(0, weight=1)
checksFrame.grid_columnconfigure(1, weight=1)


# 2)Данные

# 2.1)Словари

# 2.1.1)Словарь клавиш
keyDict = {
    "Shift_L": "Shift",
    "Shift_R": "R Shift",
    "Control_L": "Ctrl",
    "Control_R": "R Ctrl",
    "Return": "Enter",
    "Alt_L": "Alt",
    "Alt_R": "R Alt",
    "Prior": "PgUp",
    "Next": "PgDn",
    "space": "Space",
    "Caps_Lock": "Caps Lock",
    "minus": "-",
    "equal": "=",
    "bracketright": "]",
    "bracketleft": "[",
    "comma": ",",
    "period": ".",
    "slash": "/",
    "grave": "`",
    "??": "",
    "Escape": "",
    "Win_L": "",
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
    'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
    'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
    'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
    'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
    'z': 'Z'
}

# 2.1.2)Словарь клавиш мыши
mouseDict = {
    "ЛКМ": Button.left,
    "ПКМ": Button.right,
    "СКМ": Button.middle,
    "Ничего": None
}

# 2.1.3)Словарь для клавиш pynput
pynputKeyDict = {
    "Shift_L": Key.shift,           # Левый Shift
    "Shift_R": Key.shift_r,         # Правый Shift
    "Control_L": Key.ctrl,          # Левый Ctrl
    "Control_R": Key.ctrl_r,        # Правый Ctrl
    "Return": Key.enter,            # Enter
    "Alt_L": Key.alt,               # Левый Alt
    "Alt_R": Key.alt_r,             # Правый Alt
    "Prior": Key.page_up,           # PgUp
    "Next": Key.page_down,          # PgDn
    "space": Key.space,             # Space
    "Caps_Lock": Key.caps_lock,     # Caps Lock
    "minus": KeyCode.from_char('-'),  # "-"
    "equal": KeyCode.from_char('='),  # "="
    "bracketright": KeyCode.from_char(']'),  # "]"
    "bracketleft": KeyCode.from_char('['),  # "["
    "comma": KeyCode.from_char(','),  # ","
    "period": KeyCode.from_char('.'),  # "."
    "slash": KeyCode.from_char('/'),  # "/"
    "grave": KeyCode.from_char('`'), # "`"
    'a': KeyCode.from_char('a'),    # Символ "a"
    'b': KeyCode.from_char('b'),    # Символ "b"
    'c': KeyCode.from_char('c'),    # Символ "c"
    'd': KeyCode.from_char('d'),    # Символ "d"
    'e': KeyCode.from_char('e'),    # Символ "e"
    'f': KeyCode.from_char('f'),    # Символ "f"
    'g': KeyCode.from_char('g'),    # Символ "g"
    'h': KeyCode.from_char('h'),    # Символ "h"
    'i': KeyCode.from_char('i'),    # Символ "i"
    'j': KeyCode.from_char('j'),    # Символ "j"
    'k': KeyCode.from_char('k'),    # Символ "k"
    'l': KeyCode.from_char('l'),    # Символ "l"
    'm': KeyCode.from_char('m'),    # Символ "m"
    'n': KeyCode.from_char('n'),    # Символ "n"
    'o': KeyCode.from_char('o'),    # Символ "o"
    'p': KeyCode.from_char('p'),    # Символ "p"
    'q': KeyCode.from_char('q'),    # Символ "q"
    'r': KeyCode.from_char('r'),    # Символ "r"
    's': KeyCode.from_char('s'),    # Символ "s"
    't': KeyCode.from_char('t'),    # Символ "t"
    'u': KeyCode.from_char('u'),    # Символ "u"
    'v': KeyCode.from_char('v'),    # Символ "v"
    'w': KeyCode.from_char('w'),    # Символ "w"
    'x': KeyCode.from_char('x'),    # Символ "x"
    'y': KeyCode.from_char('y'),    # Символ "y"
    'z': KeyCode.from_char('z'),    # Символ "z"
    "F1": Key.f1,  # F1
    "F2": Key.f2,  # F2
    "F3": Key.f3,  # F3
    "F4": Key.f4,  # F4
    "F5": Key.f5,  # F5
    "F6": Key.f6,  # F6
    "F7": Key.f7,  # F7
    "F8": Key.f8,  # F8
    "F9": Key.f9,  # F9
    "F10": Key.f10,  # F10
    "F11": Key.f11,  # F11
    "F12": Key.f12,  # F12
}

# 2.1.4)Словарь для клавиш pynput(для нажатия)
pynputClickKeyDict = {
    "Shift_L": Key.shift,           # Левый Shift
    "Shift_R": Key.shift_r,         # Правый Shift
    "Control_L": Key.ctrl,          # Левый Ctrl
    "Control_R": Key.ctrl_r,        # Правый Ctrl
    "Return": Key.enter,            # Enter
    "Alt_L": Key.alt,               # Левый Alt
    "Alt_R": Key.alt_r,             # Правый Alt
    "Prior": Key.page_up,           # PgUp
    "Next": Key.page_down,          # PgDn
    "space": Key.space,             # Space
    "Caps_Lock": Key.caps_lock,     # Caps Lock
    "minus": KeyCode.from_char('-'),  # "-"
    "equal": KeyCode.from_char('='),  # "="
    "bracketright": KeyCode.from_char(']'),  # "]"
    "bracketleft": KeyCode.from_char('['),  # "["
    "comma": KeyCode.from_char(','),  # ","
    "period": KeyCode.from_char('.'),  # "."
    "slash": KeyCode.from_char('/'),  # "/"
    "grave": KeyCode.from_char('`'), # "`"
    "F1": Key.f1,  # F1
    "F2": Key.f2,  # F2
    "F3": Key.f3,  # F3
    "F4": Key.f4,  # F4
    "F5": Key.f5,  # F5
    "F6": Key.f6,  # F6
    "F7": Key.f7,  # F7
    "F8": Key.f8,  # F8
    "F9": Key.f9,  # F9
    "F10": Key.f10,  # F10
    "F11": Key.f11,  # F11
    "F12": Key.f12,  # F12
}


# 2.2)Списки

mouseButtonsList = ["ЛКМ", "ПКМ", "СКМ", "Ничего"]# 2.2.1)Список кнопок мыши


# 3)Классы

# 3.1) Отображает на кнопке нажатую клавишу при фокусировке на ней
class KeySelect:
    def __init__(self, button):
        self.button = button

        # Привязывает событие нажатия клавиши на клавиатуре
        self.button.bind("<KeyPress>", self.on_key_press)
        # Привязывает событие нажатия клавиши на клавиатуре(Для кнопки активации)
        if self.button == keyActivation:  self.button.bind("<KeyPress>", self.on_key_press_activate)

    def on_key_press(self, event):
        # По нажатию клавиши сопоставляет ее со словарем и меняет текст кнопки
        global key
        key = event.keysym
        if key in keyDict:
            keyText = keyDict[key]
            if keyDict[key] == "":
                AutoClicker.changeKeyButton(None)
            else:
                if key in pynputClickKeyDict:
                    AutoClicker.changeKeyButton(pynputClickKeyDict[key])
                else:
                    AutoClicker.changeKeyButton(key)

        else:
            keyText = key
            if key in pynputClickKeyDict:
                AutoClicker.changeKeyButton(pynputClickKeyDict[key])
            else:
                AutoClicker.changeKeyButton(key)

        self.button.config(text=keyText)
        window.focus_set()

    def on_key_press_activate(self, event):
        # По нажатию клавиши сопоставляет ее со словарем и меняет текст кнопки(Для кнопки активации)
        global keyActivate
        keyActivate = event.keysym
        if keyActivate in keyDict:
            keyText = keyDict[keyActivate]
        else:
            keyText = keyActivate

        if keyActivate in pynputKeyDict:
            AutoClicker.changeToggleButton(pynputKeyDict[keyActivate])
        else:
            AutoClicker.changeToggleButton(None)

        if keyText == "":
            self.button.config(text="Кнопка активации: Нет")
        else:
            self.button.config(text=("Кнопка активации: " + keyText))
        window.focus_set()


# 4)Функции

def escFocus(event):
    # 4.1)Снимает фокус с поля или кнопки\фокусируется на окне при нажатии Escape
    window.focus_set()
window.bind('<Escape>', escFocus)

def mouseFocus(event):
    # 4.2)Снимает фокус с виджета, если нажать на окно
    widget = event.widget
    focusedWidget = window.focus_get()
    if widget != focusedWidget:
        window.focus_set()
window.bind("<Button-1>", mouseFocus)

def key_enter_valid(new_value):
    # 4.3)Проверяет поле ввода на наличие не более 3 символов, являющихся числом
    if new_value.isdigit():
        return 0 <= len(new_value) <= 3
    else:
        return new_value == ""
keyEnterValidation = window.register(key_enter_valid)

def updates():
    # 4.4) Обновляет значения в файле Autoclicker.py
    hoursInt = (float(hoursEnter.get()) * 60.0 * 60.0)
    minInt = (float(minutsEnter.get()) * 60.0)
    secsInt = float(secsEnter.get())
    msecsInt = (float(msecsEnter.get()) * 0.01)
    newInt = hoursInt + minInt + secsInt + msecsInt
    AutoClicker.changeInterval(newInt)
    AutoClicker.mouseClicking(mouseCheckVar.get())
    AutoClicker.changeHold(holdingCheckVar.get())
    AutoClicker.keyClicking(keyEnterCheckVar.get())
timeFrame.bind("<FocusOut>", lambda event: updates())

def mouseChange(event):
    # 4.5)Обновляет повторяемую клавишу мыши
    changedMouseButton = mouseBux.get()
    newMouseButton = mouseDict[changedMouseButton]
    AutoClicker.mouseButtonChange(newMouseButton)

def close():
    # 4.6) Останавливает работу кликера
    AutoClicker.stopProgramm()
    window.destroy()
window.protocol("WM_DELETE_WINDOW", close)


# 5)Текст

# 5.1)Подписи полей ввода времени
hoursLabel = Label(timeFrame, text='Часы')
hoursLabel.grid(row=0, column=0, pady=30)
minutsLabel = Label(timeFrame, text='Минуты')
minutsLabel.grid(row=0, column=2)
secsLabel = Label(timeFrame, text='Секунды')
secsLabel.grid(row=0, column=4)
msecsLabel = Label(timeFrame, text='Миллисекунды')
msecsLabel.grid(row=0, column=6)

# 5.2)Выбранная клавиша
keyEnterLabel = Label(keyEnterFrame, text='Клавиша')
keyEnterLabel.place(anchor="center", relx=0.5, y=25)

# 5.3)Кнопка мыши
mouseButtonLabel = Label(keyEnterFrame, text="Кнопка мыши")
mouseButtonLabel.place(anchor="center", relx=0.5, y=85)


# 6)Поля ввода

# 6.1)Время
hoursEnter = ttk.Entry(timeFrame, width=4, justify="right", validate='key',
                       validatecommand=(keyEnterValidation, '%P'), font=(16))
hoursEnter.grid(row=0, column=1)
hoursEnter.insert(0, '0')
minutsEnter = ttk.Entry(timeFrame, width=4, justify="right", validate='key',
                        validatecommand=(keyEnterValidation, '%P'), font=(16))
minutsEnter.grid(row=0, column=3)
minutsEnter.insert(0, '0')
secsEnter = ttk.Entry(timeFrame, width=4, justify="right", validate='key',
                      validatecommand=(keyEnterValidation, '%P'), font=(16))
secsEnter.grid(row=0, column=5)
secsEnter.insert(0, '0')
msecsEnter = ttk.Entry(timeFrame, width=4, justify="right", validate='key',
                       validatecommand=(keyEnterValidation, '%P'), font=(16))
msecsEnter.grid(row=0, column=7)
msecsEnter.insert(0, '10')


# 7)Кнопки

# 7.1)Выбор клавиши
keyEnter = ttk.Button(keyEnterFrame, text='')
keyEnter.place(anchor='center', x=75, y=50)
keyEnter.bind('<FocusIn>', lambda key_select: KeySelect(keyEnter))

# 7.2)Выбор кнопки активации
keyActivation = ttk.Button(keyActivationFrame, text='Кнопка активации: Нет', padding=(60,50))
keyActivation.place(x=0,y=0, relwidth=1, relheight=1)
keyActivation.bind('<FocusIn>', lambda key_select: KeySelect(keyActivation))


# 8)Комбобоксы

# 8.1)Выбор кнопки мыши
mouseBux = ttk.Combobox(keyEnterFrame, values=mouseButtonsList, state='readonly', width=10)
mouseBux.current(0)
mouseBux.bind("<<ComboboxSelected>>", escFocus)
mouseBux.bind("<FocusIn>", mouseChange)
mouseBux.place(anchor='center', x=75, y=110)


# 9)Флажки

# 9.1)Переменные флажков
mouseCheckVar = BooleanVar(value=True)
holdingCheckVar = BooleanVar(value=False)
keyEnterCheckVar = BooleanVar(value=False)

# 9.2)Флажок выбора кнопки мыши
mouseCheck = ttk.Checkbutton(checksFrame, text="Использовать мышь", variable=mouseCheckVar, command=updates)
mouseCheck.grid(row=0, column=0, pady=15, padx=15)
mouseCheck.state(["!alternate"])
# 9.3)Флажок кнопки клавиатуры
keyEnterCheck = ttk.Checkbutton(checksFrame, text="Использовать клавиатуру", variable=keyEnterCheckVar, command=updates)
keyEnterCheck.grid(row=0, column=1, pady=15, padx=15)
keyEnterCheck.state(["!alternate"])
# 9.4)Флажок удерживания
holdingCheck = ttk.Checkbutton(checksFrame, text="Удерживать                 ", variable=holdingCheckVar, command=updates)
holdingCheck.grid(row=1, column=0, pady=15, padx=15)
holdingCheck.state(["!alternate"])


window.mainloop()