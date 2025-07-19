import random
import customtkinter as ctk
import tkinter as tk

def gerar_pis():
    pis = [random.randint(1, 9) for _ in range(11)]
    pis[0] = 1
    pis[1] = random.randint(0, 9)
    pis[2] = random.randint(0, 9)
    return ''.join(map(str, pis))

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    for i in range(9, 11):
        soma = sum([(10 - j) * cpf[j] for j in range(i)])
        digito = (soma * 10) % 11
        cpf.append(digito if digito < 10 else 0)
    return ''.join(map(str, cpf))

def gerar_cnpj():
    cnpj = [random.randint(0, 9) for _ in range(8)]
    cnpj.extend([random.randint(0, 9) for _ in range(4)])
    for i in range(12, 14):
        soma = sum([((2 + (j % 8)) * cnpj[j]) for j in range(i)])
        digito = (soma * 10) % 11
        cnpj.append(digito if digito < 10 else 0)
    return ''.join(map(str, cnpj))

def validar_pis(pis): return len(pis) == 11 and pis.isdigit()
def validar_cpf(cpf): return len(cpf) == 11 and cpf.isdigit()
def validar_cnpj(cnpj): return len(cnpj) == 14 and cnpj.isdigit()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Validador de Documentos")
        self.geometry("380x420")
        self.resizable(False, False)
        self.tipo_atual = None
        self.build_ui()

    def build_ui(self):
        ctk.CTkLabel(self, text="Validador e Gerador de Documentos", font=("Segoe UI", 22, "bold")).pack(pady=(10, 20))

        self.entry = ctk.CTkEntry(self, width=320, height=45, font=("Segoe UI", 16), justify="center")
        self.entry.insert(0, "Clique em Gerar...")
        self.entry.configure(state="readonly")
        self.entry.pack(pady=(0, 10))

        self.label_status = ctk.CTkLabel(self, text="", font=("Segoe UI", 14))
        self.label_status.pack(pady=(0, 20))

        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack()

        botoes = [
            ("Gerar PIS", self.gerar_pis),
            ("Validar PIS", self.validar_pis),
            ("Gerar CPF", self.gerar_cpf),
            ("Validar CPF", self.validar_cpf),
            ("Gerar CNPJ", self.gerar_cnpj),
            ("Validar CNPJ", self.validar_cnpj),
        ]

        for i, (label, cmd) in enumerate(botoes):
            btn = ctk.CTkButton(
                frame_botoes, text=label, width=140, height=40, corner_radius=8,
                font=("Segoe UI", 14), command=cmd
            )
            btn.grid(row=i // 2, column=i % 2, padx=15, pady=10)

    def atualizar_entrada(self, texto, tipo=None):
        self.entry.configure(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, texto)
        self.entry.configure(state="readonly")
        self.tipo_atual = tipo
        self.label_status.configure(text="")

    def gerar_pis(self):
        self.atualizar_entrada(gerar_pis(), "PIS")

    def gerar_cpf(self):
        self.atualizar_entrada(gerar_cpf(), "CPF")

    def gerar_cnpj(self):
        self.atualizar_entrada(gerar_cnpj(), "CNPJ")

    def validar_pis(self):
        self.validar("PIS", validar_pis)

    def validar_cpf(self):
        self.validar("CPF", validar_cpf)

    def validar_cnpj(self):
        self.validar("CNPJ", validar_cnpj)

    def validar(self, tipo_esperado, funcao_validacao):
        valor = self.entry.get()
        if self.tipo_atual != tipo_esperado:
            self.label_status.configure(text=f"O campo atual não é um {tipo_esperado}", text_color="orange")
            return
        if funcao_validacao(valor):
            self.label_status.configure(text=f"{tipo_esperado} Válido ✅", text_color="green")
        else:
            self.label_status.configure(text=f"{tipo_esperado} Inválido ❌", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()