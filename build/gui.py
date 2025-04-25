from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mayma\OneDrive\Área de Trabalho\aulaspython\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def obter_dados():
    # Obtendo valores dos campos de entrada
    nome = entry_1.get("1.0", "end-1c")
    rg = entry_2.get("1.0", "end-1c")
    cpf = entry_3.get("1.0", "end-1c")
    cns = entry_4.get("1.0", "end-1c")
    contato = entry_5.get("1.0", "end-1c")
    unidade_saude = entry_6.get("1.0", "end-1c")
    diabetes = entry_7.get("1.0", "end-1c")
    outros_problemas = entry_8.get()
    hipertensao = entry_9.get("1.0", "end-1c")
    
    # Criando um dicionário com os dados
    dados_paciente = {
        "Nome": nome,
        "RG": rg,
        "CPF": cpf,
        "CNS": cns,
        "Contato": contato,
        "Unidade de Saúde": unidade_saude,
        "Diabetes": diabetes,
        "Hipertensão": hipertensao,
        "Outros Problemas": outros_problemas
    }
    
    # Convertendo para string formatada
    dados_formatados = "\n".join([f"{chave}: {valor}" for chave, valor in dados_paciente.items()])
    messagebox.showinfo("Dados do Paciente", dados_formatados)
    
    return dados_paciente


window = Tk()
window.geometry("889x608")
window.configure(bg = "#FFFFFF")
window.title("Sistema de Cadastro de Pacientes")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 608,
    width = 889,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    279.0,
    608.0,
    fill="#3498DB",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    145.0,
    304.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    612.0,
    100.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=514.0,
    y=90.0,
    width=196.0,
    height=18.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    612.0,
    139.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=514.0,
    y=129.0,
    width=196.0,
    height=18.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    612.0,
    178.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=514.0,
    y=168.0,
    width=196.0,
    height=18.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    612.0,
    217.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=514.0,
    y=207.0,
    width=196.0,
    height=18.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    611.0,
    256.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=513.0,
    y=246.0,
    width=196.0,
    height=18.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    611.0,
    295.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=513.0,
    y=285.0,
    width=196.0,
    height=18.0
)

canvas.create_text(
    386.0,
    91.0,
    anchor="nw",
    text="NOME",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    386.0,
    130.0,
    anchor="nw",
    text="RG",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    386.0,
    169.0,
    anchor="nw",
    text="CPF",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    386.0,
    208.0,
    anchor="nw",
    text="CNS",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    385.0,
    247.0,
    anchor="nw",
    text="CONTATO",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    322.0,
    287.0,
    anchor="nw",
    text="UNIDADE DE SAÚDE",
    fill="#000000",
    font=("InstrumentSans Bold", 15 * -1)
)

canvas.create_text(
    375.0,
    18.0,
    anchor="nw",
    text="CADASTRO DO PACIENTE",
    fill="#3498DB",
    font=("InstrumentSans Bold", 32 * -1)
)

canvas.create_text(
    488.0,
    400.0,
    anchor="nw",
    text="PROBLEMAS DE SAÚDE",
    fill="#499ED7",
    font=("InstrumentSans SemiBold", 15 * -1)
)

canvas.create_rectangle(
    421.0,
    387.0,
    724.0,
    390.0,
    fill="#499ED7",
    outline="")

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    494.0,
    441.0,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=468.0,
    y=431.0,
    width=52.0,
    height=18.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    655.5,
    514.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=561.0,
    y=478.0,
    width=189.0,
    height=71.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    724.0,
    441.0,
    image=entry_image_9
)
entry_9 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=698.0,
    y=431.0,
    width=52.0,
    height=18.0
)

canvas.create_text(
    364.0,
    433.0,
    anchor="nw",
    text="TEM DIABETES?",
    fill="#000000",
    font=("InstrumentSans Bold", 10 * -1)
)

canvas.create_text(
    358.0,
    478.0,
    anchor="nw",
    text="OUTROS PROBLEMAS? SE SIM QUAIS?",
    fill="#000000",
    font=("InstrumentSans Bold", 10 * -1)
)

canvas.create_text(
    580.0,
    436.0,
    anchor="nw",
    text="TEM HIPERTENSÃO?",
    fill="#000000",
    font=("InstrumentSans Bold", 10 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=obter_dados,
    relief="flat"
)
button_1.place(
    x=520.0,
    y=565.0,
    width=120.0,
    height=24.56692886352539
)

window.resizable(False, False)
window.mainloop()