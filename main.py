import tkinter as tk


class Rusish:
    def __init__(self, root:tk.Tk):
        self.root = root

        self.seting()
        self.spce()
        
    def seting(self):
        self.root.title("Помошник для ЕГЭ по Русскому")
        
        widh = 1000
        heig = 600

        screen_widh = root.winfo_screenwidth()
        screen_heig = root.winfo_screenheight()

        x = (screen_widh - widh) // 2
        y = (screen_heig - heig) // 2
        self.root.geometry(f"{widh}x{heig}+{x}+{y}")
        
    def space(self):
        self.up_main_screen = tk.Frame(self.root, )

    
if __name__ == "__main__":
    root = tk.Tk()
    rusish = Rusish(root)
    root.mainloop()