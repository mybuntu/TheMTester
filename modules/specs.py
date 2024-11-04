# The GUIless Mac Tester   
## Jules David
import subprocess
import re
from pathlib import Path

# Récuperation des specs (CPU, GPU, RAM & DISKS)
def get_processor_info():
    """Récupère les informations du processeur."""
    try:
        processor_info = subprocess.check_output("sysctl -n machdep.cpu.brand_string", shell=True).decode().strip()
        result = f"Processeur: {processor_info}\n"
        return result
    except subprocess.CalledProcessError:
        return "Impossible de récupérer les informations du processeur.\n"

def get_ram_info():
    """Récupère la quantité de RAM."""
    try:
        ram_bytes = int(subprocess.check_output("sysctl -n hw.memsize", shell=True).decode().strip())
        ram_gb = ram_bytes / (1024 ** 3)  # Conversion en GB
        result = f"RAM: {ram_gb:.2f} GB\n"
        return result
    except subprocess.CalledProcessError:
        return "Impossible de récupérer les informations de la RAM.\n"

def get_gpu_info():
    """Récupère les informations des GPU intégrés et dédiés."""
    try:
        gpu_info = subprocess.check_output("system_profiler SPDisplaysDataType", shell=True).decode('utf-8')
        integrated_gpu = re.search(r"Chipset Model: (.+)", gpu_info)
        dedicated_gpu = re.findall(r"Chipset Model: (.+)", gpu_info)

        result = ""
        if integrated_gpu:
            result += f"GPU Intégré: {integrated_gpu.group(1).strip()}\n"
        if len(dedicated_gpu) > 1:
            result += f"GPU Dédié: {dedicated_gpu[1].strip()}\n"
        elif len(dedicated_gpu) == 1:
            result += "Aucun GPU dédié trouvé.\n"

        return result
    except subprocess.CalledProcessError:
        return "Impossible de récupérer les informations du GPU.\n"

def get_disk_info():
    """Récupère les informations des disques (type, capacité, état de santé)."""
    try:
        disk_info = subprocess.check_output("system_profiler SPStorageDataType", shell=True).decode('utf-8')
        disk_entries = re.findall(r"Device Name:\s*(.+?)\n.*?Medium Type:\s*(.+?)\n.*?Capacity:\s*(.+?)\n.*?S\.M\.A\.R\.T\. Status:\s*(.+?)\n", disk_info, re.DOTALL)
        
        results = []
        if disk_entries:
            for entry in disk_entries:
                results.extend([
                    f"Disque: {entry[0].strip()}",
                    f"Type: {entry[1].strip()}",
                    f"Capacité: {entry[2].strip()}",
                    f"Santé: {entry[3].strip()}\n"
                ])
        else:
            results.append("Aucun disque trouvé.\n")
        
        return "\n".join(results)
    except subprocess.CalledProcessError:
        return "Impossible de récupérer les informations du disque.\n"

def export_system_specs(output_file):
    # Rassemble toutes les spécifications système et les écrit dans le fichier resultats.txt.
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("=== SPÉCIFICATIONS DU SYSTÈME ===\n")
        file.write(get_processor_info())
        file.write(get_ram_info())
        file.write(get_gpu_info())
        file.write(get_disk_info())
        file.write("\n")

    print("Les spécifications du système ont été exportées dans resultats.txt avec succès.")
