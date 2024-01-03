import tkinter as tk
import math

# Fonction pour l'ajout de chiffres
def ajout_chiffre(chiffre):
    valeur_actuelle = entry_resultat.get()
    if valeur_actuelle == "0":
        entry_resultat.delete(0, tk.END)
    entry_resultat.insert(tk.END, chiffre)

# Fonction pour effacer
def effacer():
    entry_resultat.delete(0, tk.END)
    entry_resultat.insert(tk.END, "0")

# Fonction pour calculer
def calculer():
    try:
        expression = entry_resultat.get()
        resultat = eval(expression)
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(resultat))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

# Fonctions pour les opérations mathématiques
def sin():
    try:
        value = float(entry_resultat.get())
        result = math.sin(math.radians(value))
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def cos():
    try:
        value = float(entry_resultat.get())
        result = math.cos(math.radians(value))
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def tan():
    try:
        value = float(entry_resultat.get())
        result = math.tan(math.radians(value))
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

# Fonctions pour les nouvelles fonctionnalités
def carre():
    try:
        value = float(entry_resultat.get())
        result = value ** 2
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def racine_carree():
    try:
        value = float(entry_resultat.get())
        result = math.sqrt(value)
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def inversion_signe():
    try:
        value = float(entry_resultat.get())
        result = -value
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def pourcentage():
    try:
        value = float(entry_resultat.get())
        result = value / 100
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

def exponentiation():
    try:
        value = float(entry_resultat.get())
        result = value ** 2  # Modifier cette ligne pour obtenir l'exponentiation souhaitée
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, str(result))
    except Exception as e:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(tk.END, "Erreur")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Frame pour les éléments de la calculatrice
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Entrée pour afficher le résultat
entry_resultat = tk.Entry(frame, font=('Arial', 20), bd=10, justify='right', relief=tk.SOLID)
entry_resultat.insert(tk.END, "0")
entry_resultat.grid(row=0, column=0, columnspan=6, sticky="nsew")

# Liste des étiquettes et des commandes pour les boutons
boutons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('.', 4, 2),('+', 4, 3),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4), ('%', 3, 5),
    ('x²', 1, 5), ('√', 2, 5), ('+/-', 4, 4), ('=', 4, 5)
]

# Création des boutons avec les étiquettes et les commandes associées
for label, row, col in boutons:
    command = None
    
    if label == 'C':
        command = effacer
    elif label == '=':
        command = calculer
    elif label == 'sin':
        command = sin
    elif label == 'cos':
        command = cos
    elif label == 'tan':
        command = tan
    elif label == 'x²':
        command = carre
    elif label == '√':
        command = racine_carree
    elif label == '+/-':
        command = inversion_signe
    elif label == '%':
        command = pourcentage
    elif label == '.':
        command = lambda lbl=label: ajout_chiffre(lbl)  # Fonction pour ajouter une virgule sans parenthèses
    
    else:
        command = lambda lbl=label: ajout_chiffre(lbl)
    
    tk.Button(frame, text=label, width=5, height=2, command=command).grid(row=row, column=col)

root.mainloop()