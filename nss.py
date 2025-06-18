class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = (titulo)
        self.autor = (autor)
        self.ano = (ano)
    def eh_antigo(self):
      return self.ano < 2000

livro1 = Livro("One Piece", "Eiichiro Oda", 1997)

print(f"{livro1.titulo} é antigo?", livro1.eh_antigo()) 