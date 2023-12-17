import tkinter as tk

class MafiaApplicationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Formularz Aplikacyjny do Mafii")

        self.label_name = tk.Label(master, text="Imię:")
        self.entry_name = tk.Entry(master)

        self.label_age = tk.Label(master, text="Wiek:")
        self.entry_age = tk.Entry(master)

        self.label_experience = tk.Label(master, text="Doświadczenie w mafii:")
        self.text_experience = tk.Text(master, height=5, width=30)

        self.button_submit = tk.Button(master, text="Zatwierdź", command=self.submit_form)

        
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name.grid(row=0, column=1)

        self.label_age.grid(row=1, column=0, sticky="e")
        self.entry_age.grid(row=1, column=1)

        self.label_experience.grid(row=2, column=0, sticky="e")
        self.text_experience.grid(row=2, column=1)

        self.button_submit.grid(row=3, column=1, pady=10)

    def submit_form(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        experience = self.text_experience.get("1.0", tk.END)

        
        with open("application_data.txt", "a") as file:
            file.write(f"Imię: {name}\n")
            file.write(f"Wiek: {age}\n")
            file.write(f"Doświadczenie w mafii:\n{experience}\n")
            file.write("=" * 30 + "\n")

        
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.text_experience.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    application_form = MafiaApplicationForm(root)
    root.mainloop()