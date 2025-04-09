import random

def init_minefield(width: int, height: int) -> list:
    """
    Initialise le champ de mines avec une largeur et une hauteur données.

    :param width: Largeur du champ.
    :param height: Hauteur du champ.
    :return: Champ de mines initialisé.
    """
    if not 5 <= width <= 20:
        raise ValueError('Taille erronée !!!')
    if not 5 <= height <= 20:
        raise ValueError('Hauteur erronée !!!')

    return [[0 for _ in range(width)] for _ in range(height)]

def place_mine(empty_field:list[list[int]], nbr_mines: int, position_init=(21, 21)) -> list:
    """
    Place un nombre spécifié de mines sur le champ.

    :param position_init:
    :param empty_field: Champ vide initialisé.
    :param nbr_mines: Nombre de mines à placer.
    :return: Champ avec les mines placées.
    """
    height = len(empty_field)
    width = len(empty_field[0])
    i = 0

    if nbr_mines > height * width // 3:
        raise ValueError('Taille erronée !!!')

    while i < nbr_mines:
        row = random.randint(0, height - 1)  # Plage correcte pour la hauteur
        col = random.randint(0, width - 1)   # Plage correcte pour la largeur
        if position_init == (row, col):
            continue
        if empty_field[row][col] == 0:
            empty_field[row][col] = 9  # Utilise 9 pour représenter une mine
            i += 1

    return empty_field



