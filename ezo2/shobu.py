"""module custom contenant diverse fonctions."""


def slug_generator(string=str()):
    """fonction permettant de générer un slug à partire d'une chaîne de caractère."""
    for i in ":/?§!%¨^$£µ*@+=.,'_;":
        string = string.replace(i, "")
    slug = string.replace(" ", "-")
    return slug
