from tkinter import Tk, Label, Button, Frame
import random

def func_generate_number():
    """
    Gera um número inteiro aleatório entre 1 e 100.

    Retorna:
        int: Um número aleatório entre 1 e 100.
    """
    return random.randint(1, 100)

def create_gui_elements(frame):
    """
    Cria e posiciona todos os elementos da interface gráfica do usuário (GUI) no frame fornecido.

    Parâmetros:
        frame (Frame): O frame no qual os elementos da GUI serão colocados.
    """
    # Configura as colunas para que se expandam e centralizem os elementos, garantindo uma distribuição equilibrada do espaço.
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    
    # Configura a última linha para expandir, movendo o botão para a parte inferior do frame.
    frame.grid_rowconfigure(4, weight=1)  # Ajusta conforme a necessidade de disposição dos elementos.

    # Cria e posiciona os elementos da GUI, utilizando o método grid para alinhamento e distribuição.
    Label(frame, text="Gerar Número Aleatório:").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    Button(frame, text="Gerar Número!", command=lambda: func_generate_number()).grid(row=3, column=1, padx=10, pady=10, sticky="ew")


def main():
    """
    Função principal para configurar a janela do Tkinter e inicializar a aplicação.
    """
    root = Tk()
    root.title("Gerador de Número Aleatório")
    root.geometry("420x280")  # Define o tamanho inicial da janela.
    root.resizable(0, 0)  # Desabilita o redimensionamento da janela.

    frame = Frame(root)
    frame.pack(pady=20)  # Adiciona um padding vertical para o frame.

    create_gui_elements(frame)  # Chama a função para criar os elementos da GUI no frame.

    # Adiciona um label para a versão da aplicação, posicionado na parte inferior.
    version_label = Label(root, text="v1.0.0", anchor="e")
    version_label.pack(side="bottom", fill="x", padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
