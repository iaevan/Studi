import tkinter as tk
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
import os
from win10toast import ToastNotifier 
import time
from pypresence import Presence
from extra import clientid


notify = ToastNotifier()


running = False

hours, minutes, seconds = 0, 0, 0


global discord
discord = False

try:
    rpc = Presence(clientid)
    rpc.connect()
    rpc.update(details="Currently studying", state="Dont interrupt? pls ♥", large_image="studi", start=time.time(), buttons= [{"label": "Pc Price Tracker Bangladesh", "url": "https://www.pcpricetracker.co"},{"label": "ME", "url": "https://fb.iaevan.co"}])  # Set the presence
    discord = True
except:

    discord = False
    pass





def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

iconimg= resource_path('studi.ico')

font = resource_path('JetBrainsMono.ttf')




FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20

def loadfont(fontpath, private=True, enumerable=False):
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or unicode')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)

fontfile = font
fontfile_asByte= str.encode(fontfile)


loadfont(fontfile_asByte)



def start():
    global running
    if not running:
        update()
        running = True


def pause():
    global running
    if running:

        stopwatch_label.after_cancel(update_time)
        running = False


def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0

    stopwatch_label.config(text='00:00:00')


def update():
    a=0

    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)


    global update_time
    update_time = stopwatch_label.after(1000, update)

    if minutes != 0 and minutes != 30 and minutes % 10 == 0 and seconds == 0:
    # if seconds == 5:
        notify.show_toast(
        "Drink", 
        "drink some water, stay hydrated", 
        icon_path=iconimg, 
        duration=5, 
        threaded=True
        )


    if minutes != 0 and minutes != 10 and minutes % 30 == 0 and seconds == 0:
    # if seconds == 10:
    
        notify.show_toast(
        "Take a break bro!", 
        "Youre studying for 30 min, take a short break", 
        icon_path=iconimg, 
        duration=5, 
        threaded=True
        )
    global discord
    if seconds % 15 == 0 and discord == False:
        try:
            rpc = Presence("942139758350569493")
            rpc.connect()
            rpc.update(details="Currently studying", state="Dont interrupt? pls ♥", large_image="studi", start=time.time(), buttons= [{"label": "Pc Price Tracker Bangladesh", "url": "https://www.pcpricetracker.co"},{"label": "ME", "url": "https://fb.iaevan.co"}])  # Set the presence
            discord = True
        except:
            pass

def on_enter(e):
    e.widget['background'] = '#262626'

def on_leave(e):
    e.widget['background'] = "#191919"  

def on_enter_exit(e):
    e.widget['background'] = '#3f0000'

def on_leave_exit(e):
    e.widget['background'] = "#330000"  







root = tk.Tk()
root.title('Studi')
root.geometry('600x200')
root.configure(bg='#333333')
root.iconbitmap(iconimg)
root.resizable(False,False)

fontJet = "JetBrains Mono Regular"


stopwatch_label = tk.Label(text='00:00:00', font=(fontJet, 80), bg="#333333", fg="#b2b2b2")
stopwatch_label.pack()


start_button = tk.Button(text='start', height=5, width=7, font=(fontJet, 20), command=start, bg="#191919", fg="#b2b2b2", activebackground="#0C0C0C", activeforeground= "#b2b2b2", relief= "flat", borderwidth= 0)
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)
start_button.pack(side=tk.LEFT)


pause_button = tk.Button(text='pause', height=5, width=7, font=(fontJet, 20), command=pause, bg="#191919", fg="#b2b2b2", activebackground="#0C0C0C", activeforeground= "#b2b2b2", relief= "flat", borderwidth= 0)
pause_button.pack(side=tk.LEFT)
pause_button.bind("<Enter>", on_enter)
pause_button.bind("<Leave>", on_leave)

reset_button = tk.Button(text='reset', height=5, width=7, font=(fontJet, 20), command=reset, bg="#191919", fg="#b2b2b2", activebackground="#0C0C0C", activeforeground= "#b2b2b2", relief= "flat", borderwidth= 0)
reset_button.pack(side=tk.LEFT)
reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)

quit_button = tk.Button(text='quit', height=5, width=7, bg= "#330000", fg="#b2b2b2", font=(fontJet, 20),  activebackground="#260000", activeforeground= "#b2b2b2", relief= "flat", borderwidth= 0, command=root.quit)
quit_button.bind("<Enter>", on_enter_exit)
quit_button.bind("<Leave>", on_leave_exit)
quit_button.pack(side=tk.RIGHT)
root.mainloop()
