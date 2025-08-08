import tkinter as tk
from tkinter import messagebox
import random

# Lista de palabras
palabras = ["python", "computadora", "teclado", "monitor", "programa"]

# Elegir una palabra aleatoria
palabra = random.choice(palabras)
letras_adivinadas = []
intentos_restantes = 6

# Función para mostrar el estado de la palabra
def mostrar_palabra():
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

# Función cuando el usuario presiona "Adivinar"
def adivinar():
    global intentos_restantes
    letra = entrada_letra.get().lower()

    if not letra.isalpha() or len(letra) != 1:
        messagebox.showwarning("Entrada inválida", "Por favor ingresa solo una letra.")
        return

    if letra in letras_adivinadas:
        messagebox.showinfo("Ya usada", "Ya habías adivinado esa letra.")
        return

    letras_adivinadas.append(letra)

    if letra in palabra:
        mensaje.set("¡Bien! La letra está en la palabra.")
    else:
        intentos_restantes -= 1
        mensaje.set(f"La letra no está. Te quedan {intentos_restantes} intentos.")

    palabra_mostrada.set(mostrar_palabra())
    entrada_letra.delete(0, tk.END)

    if "_" not in palabra_mostrada.get():
        messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Adivinaste la palabra: {palabra}")
        reiniciar_juego()
    elif intentos_restantes == 0:
        messagebox.showinfo("Perdiste", f"Te quedaste sin intentos. La palabra era: {palabra}")
        reiniciar_juego()

# Reiniciar juego
def reiniciar_juego():
    global palabra, letras_adivinadas, intentos_restantes
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos_restantes = 6
    palabra_mostrada.set(mostrar_palabra())
    mensaje.set("Elige una letra:")

# ----------------- INTERFAZ ----------------- #
ventana = tk.Tk()
ventana.title("Juego del Ahorcado")
ventana.geometry("400x300")

palabra_mostrada = tk.StringVar(value=mostrar_palabra())
mensaje = tk.StringVar(value="Elige una letra:")

tk.Label(ventana, textvariable=palabra_mostrada, font=("Courier", 24)).pack(pady=20)
tk.Label(ventana, textvariable=mensaje).pack()

entrada_letra = tk.Entry(ventana, font=("Arial", 14), width=5, justify="center")
entrada_letra.pack(pady=10)

boton_adivinar = tk.Button(ventana, text="Adivinar", command=adivinar)
boton_adivinar.pack()

ventana.mainloop()
