"""module custom contenant diverse fonctions."""


def slug_generator(slug=str()):
    """fonction permettant de générer un slug à partire d'une chaîne de caractère."""
    for i in ":/?§!%¨^$£µ*@+=.,'_;":
        slug = slug.replace(i, "")
    slug = slug.replace(" ", "-")
    return slug
