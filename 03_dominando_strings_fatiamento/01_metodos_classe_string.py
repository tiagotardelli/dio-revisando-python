def metodos_string():
    curso = "python"
    print(curso.upper(), " ", curso.lower(), " ", curso.title())

    curso = "  Python "
    print(curso.strip(), " ", curso.lstrip(), curso.rstrip())

    curso = "Python"
    print(curso.center(10, '#'), ".".join(curso), curso + "$$", curso * 2)


metodos_string()