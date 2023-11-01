import argparse
import requests
import json


def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Prend les données dans le terminal lors du lancement de l'application et les traduits en arguments boursiers"
    )

    parser.add_argument(
        '-h', '--help',
        action='store_true',
        help="obtenir de l'aide",
    )

    parser.add_argument(
        '-d', '--debut',
        dest='debut',
        help='date de début',
    )

    parser.add_argument(
        '-f', '--fin',
        dest='fin',
        help='date de fin',
    )

    parser.add_argument(
        '-v', '--valeur',
        dest='valeur',
        choices=['fermeture', 'ouverture', 'min', 'max', 'volume'],
        default='fermeture',
        help='valeur de arg'
    )

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()

def produire_historique(titre, debut, fin, valeur):


    return ()

if __name__ == "__main__":
    analyser_commande()