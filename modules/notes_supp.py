# The GUIless Mac Tester   
## by Jules David
import tkinter as tk
from tkinter import simpledialog, messagebox

def add_notes(output_file):
    # Créer la fenêtre de dialogue pour les notes
    notes = simpledialog.askstring("Notes supplémentaires", "Ajouter des notes supplémentaires sur la machine")
    
    # Vérifier si des notes ont été saisies
    if notes:
        # Enregistrer les notes dans le fichier `resultats.txt`
        with open(output_file, "a", encoding="utf-8") as file:
            file.write("\n=== Notes supplémentaires : ===\n")
            file.write(f"{notes}\n")
        messagebox.showinfo("Notes", "Les notes supplémentaires ont été ajoutées.")
    else:
        messagebox.showinfo("Notes", "Aucune note n'a été ajoutée.")

