"""Imports pour le programme"""
import argparse
import json
import datetime
import requests


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
        description="Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.",
        )

    parser.add_argument(
        'symbole',
        help="Nom d'un symbole boursier",
        type=str,
        nargs = "+",
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

def produire_historique(symbole, debut, fin, valeur):
    """
    Produit l'historique à partir de l'API

    Returns:
        Liste de tuples de dates et des valeurs demandées.
    """

    if debut is not None:
        de = datetime.date(int(debut[0:4]), int(debut[5:7]), int(debut[8:10]))
    
    if fin is not None:
        fi = datetime.date(int(fin[0:4]), int(fin[5:7]), int(fin[8:10]))

    for sym in symbole:
        url = f'https://pax.ulaval.ca/action/{sym}/historique/'

        if fin is None:
            fi = datetime.date.today()

        if debut is None:
            de = fi

        print(f'titre={sym}: valeur={valeur}, début={de.__repr__()}, fin={fi.__repr__()}')

        params = {
            'début': de,
            'fin': fi,
            'valeur': sym,
        }

        réponse = json.loads(requests.get(url, params).text)

        liste_rep = []

        histo = réponse.get('historique')

        for date in histo:
            day = datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10]))
            liste_rep.append(tuple([day, histo.get(date).get(valeur)]))

    liste_rep.sort()

    return liste_rep


if __name__ == "__main__":
    arguments = analyser_commande()

    historique = produire_historique(arguments.symbole, arguments.debut, arguments.fin, arguments.valeur)

    print(historique)
