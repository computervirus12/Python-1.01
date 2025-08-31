import tkinter as tk
from tkinter import scrolledtext, messagebox, Canvas
from datetime import datetime
import threading
import time

# Boot screen
def show_boot_screen(root):
    boot = tk.Toplevel(root)
    boot.attributes('-fullscreen', True)
    boot.configure(bg='blue')

    tk.Label(boot, text="Python", font=("Arial", 80), fg="white", bg="blue").pack(pady=150)
    tk.Label(boot, text="This Python OS was made in 2025", font=("Arial", 16), fg="white", bg="blue").pack(side="bottom")

    def close_boot():
        boot.destroy()
        show_main_screen(root)

    boot.after(3000, close_boot)

# Notepad app
def open_notepad():
    win = tk.Toplevel()
    win.title("Notepad")
    win.geometry("600x400")
    text = scrolledtext.ScrolledText(win, wrap=tk.WORD)
    text.pack(expand=True, fill='both')

# WordPad app
def open_wordpad():
    win = tk.Toplevel()
    win.title("WordPad")
    win.geometry("600x400")
    text = tk.Text(win, wrap=tk.WORD, font=("Times New Roman", 14))
    text.pack(expand=True, fill='both')

# Clock app
def open_clock():
    win = tk.Toplevel()
    win.title("Clock")
    win.geometry("300x100")
    label = tk.Label(win, font=("Arial", 30))
    label.pack()

    def update_time():
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            label.config(text=now)
            time.sleep(1)

    threading.Thread(target=update_time, daemon=True).start()

# Paint app
def open_paint():
    win = tk.Toplevel()
    win.title("Paint")
    win.geometry("600x400")
    canvas = Canvas(win, bg="white")
    canvas.pack(fill="both", expand=True)

    def draw(event):
        x, y = event.x, event.y
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")

    canvas.bind("<B1-Motion>", draw)

# About Python app
def open_about():
    messagebox.showinfo("About Python", "Python 1.01 OS\nCreated in 2012–2025\nAll rights reversed.")

# Shutdown function
def shutdown_os():
    if messagebox.askokcancel("Shutdown", "Are you sure you want to shut down Python 1.01 OS?"):
        root.quit()

# Main OS screen
def show_main_screen(root):
    main = tk.Toplevel(root)
    main.attributes('-fullscreen', True)
    main.configure(bg="yellow")

    tk.Label(main, text="Python 1.01 OS", font=("Arial", 40), fg="black", bg="yellow").pack(pady=20)

    btn_frame = tk.Frame(main, bg="yellow")
    btn_frame.pack(pady=10)

    apps = [
        ("📝 Notepad", open_notepad),
        ("🕒 Clock", open_clock),
        ("📄 WordPad", open_wordpad),
        ("🎨 Paint", open_paint),
        ("ℹ️ About Python", open_about),
        ("🔴 Shutdown", shutdown_os),
    ]

    for name, func in apps:
        btn = tk.Button(btn_frame, text=name, font=("Arial", 20), width=20, command=func)
        btn.pack(pady=5)

    # Scrollable system files section
    sys_frame = tk.Frame(main, bg="yellow")
    sys_frame.pack(pady=20, fill="both", expand=True)

    canvas = tk.Canvas(sys_frame, bg="yellow")
    scrollbar = tk.Scrollbar(sys_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="yellow")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text="System Files", font=("Arial", 18), fg="black", bg="yellow").pack(pady=10)

    system_files = [f"📁 system_file_{i}.sys" for i in range(1, 31)]
    for file in system_files:
        tk.Label(scroll_frame, text=file, font=("Arial", 14), fg="gray", bg="yellow").pack(anchor="w", padx=20)

# Start the OS
root = tk.Tk()
root.withdraw()
show_boot_screen(root)
root.mainloop()