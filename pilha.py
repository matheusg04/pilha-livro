class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.paginas} páginas)"

class PilhaDeLivros:
    def __init__(self, capacidade_maxima):
        self.pilha = []
        self.capacidade_maxima = capacidade_maxima

    def isEmpty(self):
        return not self.pilha

    def isFull(self):
        return len(self.pilha) == self.capacidade_maxima

    def push(self, livro):
        if not self.isFull():
            self.pilha.append(livro)
        else:
            print("Erro: Pilha de livros está cheia.")

    def pop(self):
        if not self.isEmpty():
            return self.pilha.pop()
        else:
            print("Erro: Pilha de livros está vazia.")
            return None

    def tamanho(self):
        return len(self.pilha)

    def topo(self):
        return self.pilha[-1] if self.pilha else None

    def remover(self):
        if not self.isEmpty():
            print(f"Livro removido: {self.pop()}")
        else:
            print("Erro: Pilha de livros está vazia. Nenhum livro para remover.")

    def imprimir(self):
        if not self.isEmpty():
            print("Conteúdo da Pilha de Livros:")
            for livro in reversed(self.pilha):
                print(livro)
        else:
            print("Pilha de livros está vazia.")



pilha = PilhaDeLivros(capacidade_maxima=5)

pilha.push(Livro("Dom Quixote", "Miguel de Cervantes", 863))
pilha.push(Livro("A Revolução dos Bichos", "George Orwell", 144))
pilha.push(Livro("Cem Anos de Solidão", "Gabriel García Márquez", 417))

print("Livro no topo da pilha:", pilha.topo())
print("Tamanho da pilha:", pilha.tamanho())

pilha.remover()

pilha.imprimir()

while not pilha.isEmpty():
    pilha.remover()

print("A pilha está vazia?", pilha.isEmpty())
