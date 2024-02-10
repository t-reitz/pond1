from tkinter import Tk, Label, Button, Frame, StringVar, Entry
import random

# Define root no nível superior do script para ser acessível globalmente.
root = Tk()

def func_generate_number(min_val, max_val):
    """
    Gera um número inteiro aleatório dentro do intervalo especificado.
    """
    return random.randint(min_val, max_val)

def update_label_with_random_number():
    """
    Atualiza o label com um número aleatório gerado pela função func_generate_number,
    utilizando os valores mínimo e máximo fornecidos pelos inputs.
    """
    try:
        min_val = int(min_val_var.get())
        max_val = int(max_val_var.get())
        # Certifica-se de que o valor mínimo é menor que o máximo
        if min_val < max_val:
            random_number = func_generate_number(min_val, max_val)
            random_number_var.set(f"Número gerado: {random_number}")
        else:
            random_number_var.set("Min deve ser menor que Max.")
    except ValueError:
        random_number_var.set("Por favor, insira valores numéricos válidos.")

def exit_app():
    """
    Fecha a aplicação.
    """
    root.destroy()

def create_gui_elements(frame):
    """
    Cria e posiciona todos os elementos da interface gráfica do usuário (GUI) no frame fornecido.
    """
    Label(frame, text="Gerar Número Aleatório:").grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Cria os labels para os inputs de mínimo e máximo.
    Label(frame, text="MIN").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    Entry(frame, textvariable=min_val_var, width=5).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    
    Label(frame, text="MAX").grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    Entry(frame, textvariable=max_val_var, width=5).grid(row=2, column=2, padx=5, pady=5, sticky="ew")
    
    Label(frame, textvariable=random_number_var).grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    
    # Posiciona o botão abaixo dos inputs e do label de número gerado.
    Button(frame, text="Gerar Número!", command=update_label_with_random_number).grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky="ew")

    Button(frame, text="SAIR", command=exit_app).grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky="ew")


def main():
    global random_number_var, min_val_var, max_val_var
    root.title("Gerador de Número Aleatório")
    root.geometry("420x280")
    root.resizable(0, 0)

    random_number_var = StringVar(value="Número gerado aparecerá aqui")
    min_val_var = StringVar(value="1")
    max_val_var = StringVar(value="100")

    frame = Frame(root)
    frame.pack(pady=20)

    create_gui_elements(frame)

    version_label = Label(root, text="v1.3.0", anchor="e")
    version_label.pack(side="bottom", fill="x", padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
