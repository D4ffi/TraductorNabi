import google.generativeai as genai
from tkinter import *

API_KEY = "AIzaSyBjEYLrBSBODY-NPmac7yeZmZdp3nSSmmY"

genai.configure(
    api_key=API_KEY
)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Formato de la UI
FONDO = "#E6D6CA"
FONDO_OSCURO = "#FFEEE0"
COLOR_TEXTO = "#003A35"
FUENTE = ("Arial", 12)
FUENTE_NEGRITA = ("Arial", 12, "bold")


# Codigo
class Traductor:
    def __init__(self):
        self.ventana = Tk()
        self._configurar_ventana_principal()

    def run(self):
        self.ventana.mainloop()

    def _configurar_ventana_principal(self):
        self.ventana.title("Traductor")
        self.ventana.resizable(width=False, height=False)
        self.ventana.configure(width=400, height=550, bg=FONDO_OSCURO)

        # Etiqueta principal
        etiqueta_principal = Label(self.ventana, bg=FONDO_OSCURO, fg=COLOR_TEXTO, text="Traductor", font=FUENTE_NEGRITA,
                                   pady=10)
        etiqueta_principal.place(relwidth=1)

        # Divisor
        linea = Label(self.ventana, width=450, bg=FONDO)
        linea.place(relwidth=1, rely=0.07, relheight=0.012)

        # Widget de texto
        self.widget_texto = Text(self.ventana, width=20, height=2, bg=FONDO_OSCURO, fg=COLOR_TEXTO, font=FUENTE, padx=5,
                                 pady=5)
        self.widget_texto.place(relheight=0.745, relwidth=1, rely=0.08)
        self.widget_texto.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.widget_texto)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.widget_texto.yview)

        # Etiqueta inferior
        etiqueta_inferior = Label(self.ventana, bg=FONDO, height=80)
        etiqueta_inferior.place(relwidth=1, rely=0.825)

        # Caja de entrada de mensaje
        self.entrada_msg = Entry(etiqueta_inferior, bg=FONDO_OSCURO, fg=COLOR_TEXTO, font=FUENTE)
        self.entrada_msg.place(relwidth=0.64, relheight=0.05, rely=0.008, relx=0.011)  # Ajusta estos valores
        self.entrada_msg.focus()

        # Boton de enviar
        boton_enviar = Button(etiqueta_inferior, text="Enviar", font=FUENTE, width=20, bg=FONDO,
                      command=lambda: self._enviar_mensaje(None))
        boton_enviar.place(relx=0.77, rely=0.008, relheight=0.05, relwidth=0.22)  # Ajusta estos valores

        self.ventana.bind("<Return>", self._enviar_mensaje)

    def _enviar_mensaje(self, e):
        mensaje = self.entrada_msg.get()
        self.entrada_msg.delete(0, END)
        self._insertar_mensaje(mensaje, "Tu")

        respuesta = chat.send_message(mensaje)
        self._insertar_mensaje(respuesta.text, "Gemini")

    def _insertar_mensaje(self, mensaje, remitente):
        if not mensaje:
            return

        self.widget_texto.configure(state=NORMAL)
        self.widget_texto.insert(END, f"{remitente}: {mensaje}\n")
        self.widget_texto.configure(state=DISABLED)

        self.widget_texto.see(END)


traductor = Traductor()

if __name__ == "__main__":
    traductor.run()
