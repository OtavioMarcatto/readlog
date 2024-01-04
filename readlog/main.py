import tkinter as tk
from tkinter import filedialog
from pymavlink import mavutil
from datetime import datetime

def process_file():
    filename = filedialog.askopenfilename(filetypes=[("Log files", "*.log", ".bin"), ("All files", "*.*")])
    if not filename:
        print("Nenhum arquivo selecionado.")
        return
    print("Processing log %s" % filename)
    mlog = mavutil.mavlink_connection(filename)
    data = {}

    while True:
        m = mlog.recv_match(type="")
        if m is None:
            print("Nenhuma mensagem restante.")
            break
        m_type = m.get_type()
        data[m.TimeUS] = {
            "Volt": m.Volt,
            "Curr": m.Curr,
        }
        print(f"Processed message type: {m_type}")  # Debug: imprimir tipo de mensagem

    print(f"Data: {data}")  # Debug: imprimir o dicionário de dados

    result_label.config(text=str(data))
    result_label.config(text=str(data))
    root.update_idletasks()  # Forçar atualização da interface gráfica



# Criar janela principal
root = tk.Tk()
root.title("Processar Log MAVLink")

# Botão para selecionar arquivo
select_button = tk.Button(root, text="Selecionar arquivo", command=process_file)
select_button.pack(pady=20)

# Label para exibir resultados
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=20)

# Iniciar loop principal da GUI
root.mainloop()
