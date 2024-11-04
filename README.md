# The GUI Mac Tester   
## by Jules David

Structure:
---------
```plaintext
TheMacTester/
├── requirements.txt        # Dependances (libraies pythons)
|
├── Tester.py               # Script de tests Graphique
├── modules/                # Dossier pour les modules
│   ├── info.py             # Module pour la prise d'informations système
│   ├── specs.py            # Module pour les tests matériels
│   ├── battery_test.py     # Module pour les tests concernant la batterie
│   └── hardware_test.py    # Module pour les tests matériels
│   └── user_test.py        # Module pour générer les tests utilisateurs
│   └── notes_supp.py       # Module pour noter des éléments supplémentaires 
│   └── report.py           # Module pour générer le rapport PDF
├── resources/              # Dossier pour les fichiers de ressources (si besoin)
│   └── model_years.txt     # Fichier contenant les modèles et les années
```

# Utilisation :
Dans le repertoire TheMacTester \
Utilisation (Installation manuelle) :\
Pour un environnement virtuel (facultatif)
```plaintext
    python3 -m venv venv 
    source venv/bin/activate 
    (Dependances)
    pip3 install --upgrade pip
    pip3 install -r requirements.txt 
    python3 Tester.py
->Pour désactiver l'environnement virtuel:
    deactivate
    rm -rf venv
```

# Explication : 
Le script Tester.py propose plusieurs choix de tests.
Chaque module est une fonction mais le but était de rendre le programme de base plus modulable. 
Dans le dossier resoures, vous trouverez un repertoire des mac par modèles et années (incomplète pour l'instant). 
Chaque modules renvoie un resultat dans le fichier ~/Desktop/$NOM_DU_DOSSIER_/resultats.txt. \
Le module report.py permet de generer un pdf qui se basera sur le fichier resultats.txt pour rendre un fichier pdf plus lisible. 
Ignorer les modules "impression" & "upload" qui pour l'instant n'ont pas été testé.

# Pour la version Tester.py
Les tests nécessitant des entrées de l'utilisateur se feront depuis le terminal, donc gardez un oeil sur ce dernier afin de voir si le programme nécessite une entrée.

# Les résultats :
En début d'execution, le programme demande un input. Cet input sera la variable $OUTPUT_DIR et il sera automatiquement rangé sur le bureau dans un repertoire "RESULTATS_TESTS" grace à la variable $MAIN_DIR qui se crée directement à l'execution de Tester.py\
(~/Desktop/$MAIN_DIR/$OUTPUT_DIR/FICHIERS_DE_RESULTATS)

Pour les Reconditionnement :
-
Il suffit de taper "Recond" (avec le 'R' Majuscule) et tous les fichiers de sorties seront envoyé dans le dossiers déstinnée aux machines reconditionnées. 