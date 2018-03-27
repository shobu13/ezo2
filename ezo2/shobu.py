def slugGenerator(slug=str()):
    for i in ":/?§!%¨^$£µ*@+=.,'_;":
        slug=slug.replace(i,"")
    slug=slug.replace(" ","-")
    return slug