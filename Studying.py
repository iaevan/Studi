import tkinter as tk
from win10toast import ToastNotifier

notify = ToastNotifier()

root= tk.Tk()
root.title('Studying')
root.geometry('600x200')
root.iconbitmap('G:\\flex\icon.ico')
root.resizable(False,False)

running = False

hours, minutes, seconds = 0, 0, 0

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

    if minutes != 0 and minutes != 30 and minutes % 10 == 0:
    # if seconds == 5:
        notify.show_toast(
        "Drink", 
        "drink some water, stay hydrated", 
        icon_path="", 
        duration=3, 
        threaded=True
        )

    if minutes != 0 and minutes != 10 and minutes % 30 == 0:
    # if seconds == 10:
        notify.show_toast(
        "Take a break bro!", 
        "Youre studying for 30 min, take a short break", 
        icon_path="", 
        duration=3, 
        threaded=True
        )



stopwatch_label = tk.Label(text='00:00:00', font=('JetBrains Mono', 80))
stopwatch_label.pack()


start_button = tk.Button(text='start', height=5, width=7, font=('JetBrains Mono', 20), command=start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='pause', height=5, width=7, font=('JetBrains Mono', 20), command=pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='reset', height=5, width=7, font=('JetBrains Mono', 20), command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='quit', height=5, width=7, bg= "red", fg="white", font=('JetBrains Mono', 20), command=root.quit)
quit_button.pack(side=tk.RIGHT)
root.mainloop()