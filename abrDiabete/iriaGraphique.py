import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk
from tkinter import filedialog, messagebox


def load_data(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    X = data[:, :-1]
    y = data[:, -1].astype(int)
    return X, y


def train_model(X_train, y_train, max_depth):
    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(X_train, y_train)
    return model


def test_model(model, X_test):
    return model.predict(X_test)


def calculate_accuracy(y_true, y_pred):
    accuracy = sum(y_true == y_pred) / len(y_true)
    return accuracy


def open_file():
    filepath = filedialog.askopenfilename(title="Ouvrir le fichier", filetypes=[("Fichiers CSV", "*.csv")])
    if filepath:
        try:
            X, y = load_data(filepath)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            max_depth = int(max_depth_entry.get())
            model = train_model(X_train, y_train, max_depth)
            y_pred = test_model(model, X_test)
            accuracy = calculate_accuracy(y_test, y_pred)
            accuracy_label.configure(text=f"Précision: {accuracy:.2f}")
            show_predictions(X_test, y_test, y_pred)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier: {e}")
            
            
def show_predictions(X_test, y_true, y_pred):
    prediction_window = tk.Toplevel(root)
    prediction_window.title("Prédictions")
    prediction_window.geometry("400x300")
    
    for i, (x, y_true, y_pred) in enumerate(zip(X_test, y_true, y_pred)):
        tk.Label(prediction_window, text=f"Exemple {i+1}").pack()
        tk.Label(prediction_window, text=f"Caractéristiques: {x}").pack()
        tk.Label(prediction_window, text=f"Vraie valeur: {y_true}").pack()
        tk.Label(prediction_window, text=f"Prédiction: {y_pred}").pack()
        tk.Label(prediction_window, text="").pack()


# Interface graphique
root = tk.Tk()
root.title("Prédiction de diabète")
root.geometry("400x200")

# Titre
title_label = tk.Label(root, text="Prédiction de diabète", font=("Arial", 16))
title_label.pack(pady=10)

# Bouton Ouvrir
open_button = tk.Button(root, text="Ouvrir le fichier", command=open_file)
open_button.pack()

# Max Depth Entry
max_depth_label = tk.Label(root, text="Profondeur maximale:")
max_depth_label.pack()
max_depth_entry = tk.Entry(root)
max_depth_entry.pack()

# Précision
accuracy_label = tk.Label(root, text="Précision: ")
accuracy_label.pack(pady=10)

root.mainloop()
