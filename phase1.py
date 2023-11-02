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
        description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers."
    )

    parser.add_argument(
        'symbole',
        help="Nom d'un symbole boursier",
        )

    parser.add_argument(
        '-d', '--debut',
        dest='debut',
        metavar='DATE',
        help='Date recherchée la plus ancienne (format: AAAA-MM-JJ)',
    )

    parser.add_argument(
        '-f', '--fin',
        dest='fin',
        metavar='DATE',
        help='Date recherchée la plus récente (format: AAAA-MM-JJ)',
    )

    parser.add_argument(
        '-v', '--valeur',
        dest='valeur',
        choices=['fermeture', 'ouverture', 'min', 'max', 'volume'],
        default='fermeture',
        help='La valeur désirée (par défaut: fermeture)'
    )

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()

def produire_historique(titre, debut, fin, valeur):


    return ()

if __name__ == "__main__":
    parser = analyser_commande()
    