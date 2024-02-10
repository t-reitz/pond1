from tkinter import Tk, Label, Button, Frame, StringVar
import threading 
from datetime import datetime, timedelta
from datetime import date
import os

# # Function to set the default dates for the date picker
# def set_default_dates():
#     today = datetime.now()
#     weekday = today.weekday()
#     last_sunday = today - timedelta(days=(weekday + 1))
#     last_monday = last_sunday - timedelta(days=6)
#     return last_monday.date(), last_sunday.date()

# # Function to run the scripts
# def run_scripts(start_date, end_date, loading_label):
#     # Running SQL query
#     loading_label.config(text="SQL Query...")
#     df = fechamentoComissao.sql_get_df()

#     # Call the main function from fechamentoComissao
#     loading_label.config(text="Calculando Comissão...")
#     output_dir, df_com_comissoes = fechamentoComissao.main(df, comissao_path, start_date, end_date)

#     # Call the main function from gerarPDF
#     loading_label.config(text="Gerando PDFs...")
#     gerarPDF.main(output_dir, start_date, end_date)

#     # Agrupar corbans por promotor em um dicionario
#     loading_label.config(text="Organizando Pastas...")
#     promotor_dict = fechamentoComissao.corbans_com_promotor(df_com_comissoes)

#     # Usar dicionario para criar pastas dos promotores
#     fechamentoComissao.organizar_pastas_promotor(output_dir, promotor_dict)

#     print("Scripts executed successfully.")
    
#     # Show "Done!" text after scripts executed
#     loading_label.config(text="Arquivos Gerados!")

# Function to run the scripts in a separate thread
# def run_scripts_threaded(date_start_entry, date_end_entry, loading_label):
#     start_date = date_start_entry.get_date()
#     end_date = date_end_entry.get_date()

#     # Assuming start_date and end_date are passed as datetime.date objects, convert them to datetime
#     start_date = datetime.combine(start_date, datetime.min.time())
#     end_date = datetime.combine(end_date, datetime.max.time())

#     # Datas do período de comissao formatadas para criar output_dir
#     min_date = start_date.strftime('%d %b')
#     max_date = end_date.strftime('%d %b')

#     # Cria a pasta de output
#     output_dir = os.path.join(output_path, f'Comissões {min_date} - {max_date}')
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     thread = threading.Thread(target=lambda: run_scripts(start_date, end_date, loading_label))
#     thread.start()

def func_generate_number():
    return 1

# Função para criar e posicionar todos os elementos da GUI
def create_gui_elements(frame):
    # Configura as colunas para expandir e centralizar os elementos
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    
    # Configura a última linha para expandir, empurrando o botão para baixo
    frame.grid_rowconfigure(4, weight=1)  # Ajuste o número da linha conforme necessário

    # Criação dos elementos com o grid alinhado ao centro
    Label(frame, text="Gerar Número aleatório:").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    Label(frame, text="Período Início:").grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    # Ajusta o botão para ficar na parte inferior, mantendo-o no centro
    Button(frame, text="Gerar Número!", command=lambda: func_generate_number()).grid(row=3, column=1, padx=10, pady=10, sticky="ew")


# Main function to set up the Tkinter window
def main():
    root = Tk()
    root.title("Random Number Generator")
    root.geometry("420x280")
    root.resizable(0, 0)

    frame = Frame(root)
    frame.pack(pady=20)

    create_gui_elements(frame)

    version_label = Label(root, text="v1.0.0", anchor="e")
    version_label.pack(side="bottom", fill="x", padx=10, pady=5)

    root.mainloop()

# Run the main function if the script is executed
if __name__ == "__main__":
    main()