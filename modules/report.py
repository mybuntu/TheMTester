# The GUIless Mac Tester   
## Jules David
from fpdf import FPDF
from datetime import datetime

# Regler le problème d'encodage UTF-8
def sanitize_text(text):
    # Remplace les caractères non compatibles avec 'latin-1' par des "?" et les supprime ensuite.
    sanitized_text = text.encode('latin-1', 'replace').decode('latin-1')
    return sanitized_text.replace("?", "")

# Format et génération du fichier PDF
def generate_pdf(output_file, pdf_path, terminal_output):
    try:
        pdf = FPDF()
        pdf.add_page()
        # Titre et date
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, "Test PlaceDuMac", ln=True, align="C")
        pdf.set_font("Arial", 'B', 12)
        current_date = datetime.now().strftime("%d %B %Y")
        pdf.cell(200, 10, current_date, ln=True, align="C")
        pdf.ln(10)

        # Ajout du contenu du fichier texte `resultats.txt`
        pdf.set_font("Arial", '', 10)
        with open(output_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = sanitize_text(line.strip())                
                # Mettez en gras les sections en supprimant les "==="
                if "===" in line:
                    pdf.set_font("Arial", 'B', 12)
                    line = line.replace("===", "").strip()  # Supprime les "==="
                    pdf.cell(0, 6, line, ln=True)
                    pdf.set_font("Arial", '', 10)  # Repasse en normal pour le contenu suivant
                else:
                    pdf.multi_cell(0, 4, line)
        # Enregistrer le PDF au chemin spécifié
        pdf.output(pdf_path)
        print("Le PDF a été généré avec succès !")

    except Exception as e:
        print(f"Erreur lors de la génération du PDF : {e}")
