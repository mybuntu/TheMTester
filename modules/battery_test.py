# The GUIless Mac Tester   
## Jules David
import subprocess
import re
import platform

# Fonction pour obtenir les informations sur la batterie et les écrire dans un fichier texte
def check_battery_status(output_file):
    try:
        # Vérifier l'architecture
        arch = platform.processor()
        if "arm" in arch.lower():
            print("Exécution sur Apple Silicon.")
        else:
            print("Exécution sur Intel.")

        # Exécuter la commande ioreg pour obtenir les capacités
        ioreg_output = subprocess.check_output(
            "ioreg -l -b | grep -i -E 'capacity|CycleCount'", shell=True
        ).decode('utf-8')

        # Extraire les informations
        max_capacity = re.search(r'"AppleRawMaxCapacity" = (\d+)', ioreg_output)
        current_capacity = re.search(r'"AppleRawCurrentCapacity" = (\d+)', ioreg_output)
        design_capacity = re.search(r'"DesignCapacity" = (\d+)', ioreg_output)
        cycle_count = re.search(r'"CycleCount" = (\d+)', ioreg_output)

        # Vérifier la présence des données
        if not max_capacity or not current_capacity or not design_capacity:
            raise ValueError("Impossible de trouver certaines informations sur la batterie.")

        max_capacity = int(max_capacity.group(1))
        current_capacity = int(current_capacity.group(1))
        design_capacity = int(design_capacity.group(1))
        cycle_count = int(cycle_count.group(1)) if cycle_count else "Non disponible"

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
            file.write("=== ÉTAT DE LA BATTERIE ===\n")
            file.write(result)
            file.write("\n")

        print(f"Les informations sur la batterie ont été exportées dans {output_file} avec succès.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande ioreg : {e}")
    except ValueError as ve:
        print(f"Erreur lors de la récupération des informations : {ve}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")