# The GUIless Mac Tester   
## by Jules David
import subprocess
import re
import os

# Fonction pour obtenir les informations sur la batterie et les écrire dans un fichier texte
def check_battery_status(output_file):
    try:
        # Exécuter la commande ioreg pour obtenir les capacités
        ioreg_output = subprocess.check_output("ioreg -l -b | grep -i -E 'capacity|CycleCount'", shell=True).decode('utf-8')

        # Extraire les capacités
        max_capacity = int(re.search(r'"MaxCapacity" = (\d+)', ioreg_output).group(1))
        current_capacity = int(re.search(r'"CurrentCapacity" = (\d+)', ioreg_output).group(1))
        design_capacity = int(re.search(r'"DesignCapacity" = (\d+)', ioreg_output).group(1))

        # Extraire le nombre de cycles de charge
        cycle_count_match = re.search(r'"CycleCount" = (\d+)', ioreg_output)
        cycle_count = int(cycle_count_match.group(1)) if cycle_count_match else "Non disponible"

        # Calculer la santé de la batterie en pourcentage
        battery_health_percentage = (max_capacity / design_capacity) * 100

        # Préparer le résultat
        result = (
            f"Capacité actuelle: {current_capacity} mAh\n"
            f"Capacité maximale: {max_capacity} mAh\n"
            f"Capacité de conception (design): {design_capacity} mAh\n"
            f"État de santé de la batterie: {battery_health_percentage:.2f}%\n"
            f"Nombre de cycles de charge: {cycle_count}\n\n"
        )

        # Écrire les résultats dans le fichier texte
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write("=== ETAT DE LA BATTERIE ===\n")
            file.write(result)
            file.write("\n")
        print(f"Les informations sur la batterie ont été exportées dans {output_file} avec succès.")

    except Exception as e:
        print(f"Erreur lors de la récupération des informations de la batterie : {e}")
