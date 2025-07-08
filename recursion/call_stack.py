def sauda(nome):
    print(f"Olá, {nome}!")
    sauda2(nome)
    print("Preparando para dizer tchau!")
    tchau(nome)

def sauda2(nome):
    print(f"Como vai {nome}?")

def tchau(nome):
    print(f"Tchau {nome}!")

sauda("Stack")