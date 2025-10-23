import tkinter as tk
from tkinter import font

class Rusish:
    def __init__(self, root: tk.Tk, widh:int=1000, heig:int=600):
        self.root = root
        self.widh = widh
        self.heig = heig

        self.seting()
        self.space()
        self.widget()

    def seting(self):
        self.root.title("Помошник для ЕГЭ по Русскому")
        self.root.configure(background="#ECE8B4")
        
        self.geometry()
            
    def geometry(self):
        screen_widh = self.root.winfo_screenwidth()
        screen_heig = self.root.winfo_screenheight()

        x = (screen_widh - self.widh) // 2
        y = (screen_heig - self.heig) // 2
        self.root.geometry(f"{self.widh}x{self.heig}+{x}+{y}")

    def space(self):
        
        self.up_main_screen = tk.Frame(
            self.root,
            background="#ECE8B4",
        )
        self.up_main_screen.pack(
            fill="x"
        )
        
        self.down_main_screen = tk.Frame(
            self.root,
            background="#ECE8B4"
        )
        self.down_main_screen.pack(
            expand=True
        )
        
        self.buttons = tk.Frame(
            self.down_main_screen,
            background="#ECE8B4"
        )
        self.buttons.pack(
            expand=True
        )
    
    def widget(self):        
        
        font_title = font.Font(family="Times New Roman", size=24, weight="bold")
        
        tk.Label(
            self.up_main_screen,
            font=font_title,
            text="Номера в ЕГЭ по Русскому языку",
            background="#ECE8B4",
            pady=40
        ).pack(

        )
        
        tasks = [
            "Задание 1\nВставить в текст",
            "Задание 2\nСредства связи",
            "Задание 3\nЛексика",
            "Задание 4\nОрфоэпия",
            "Задание 5\nПаронимы",
            "Задание 6\nЛексика",
            "Задание 7\nСоответствие",
            "Задание 8\nОрфография",
            "Задание 9\nСуффиксы",
            "Задание 10\nПриставки",
            "Задание 11\nГлаголы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
            "Задание 12\nЧастицы",
        ]
        
        for i, task_text in enumerate(tasks):
            row = i // 6  # 4 кнопки в строке
            col = i % 6
            
            tk.Button(
                self.buttons,
                text=task_text,
                command=lambda x=i+1: self.task_handler(x),
                width=15,
                height=3,
                wraplength=120,  # перенос текста
                background="#B1AF92",
                font=("Arial", 10),
                anchor="n"
            ).grid(
                row=row,
                column=col,
                padx=10,
                pady=10,
                sticky="nsew",
            )
        
    def task_handler(self, task_number):
        print(f"Задание {task_number}")



if __name__ == "__main__":
    root = tk.Tk()
    rusish = Rusish(root)
    root.mainloop()
