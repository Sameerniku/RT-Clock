import tkinter as tk
from datetime import datetime

class RealTimeClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Clock App")
        self.time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.time_label.pack(anchor='center')

        # Update the time every 1000 milliseconds (1 second)
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label['text'] = current_time
        self.time_label.after(1000, self.update_time)  # Schedule the update after 1000 milliseconds (1 second)

if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeClockApp(root)
    root.geometry("400x200")
    root.configure(background='black')

    # My Reference
    reference_label = tk.Label(root, text="Made by Sameer", font=('calibri', 12), background='black', foreground='white')
    reference_label.pack(side='bottom', pady=10)

    root.mainloop()
