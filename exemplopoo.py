# Classe base
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível.")

    def devolver(self):
        self.disponivel = True
        print(f"O livro '{self.titulo}' foi devolvido.")


# Subclasse com herança e polimorfismo
class LivroDidatico(Livro):
    def __init__(self, titulo, autor, ano, disciplina):
        super().__init__(titulo, autor, ano)
        self.disciplina = disciplina

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro didático '{self.titulo}' da disciplina {self.disciplina} foi emprestado por 7 dias.")
        else:
            print(f"O livro didático '{self.titulo}' não está disponível.")


# --- Exemplo de execução ---
if __name__ == "__main__":
    # Criando objetos
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro3 = LivroDidatico("Introdução à Programação", "José Augusto", 2023, "Computação")
    
    # Mostrando empréstimos
    print("\n--- Empréstimos ---")
    livro1.emprestar()   # Livro comum
    livro3.emprestar()   # Livro didático (comportamento polimórfico)

    # Tentando emprestar de novo
    print("\n--- Tentando novo empréstimo ---")
    livro1.emprestar()   # Já emprestado
    livro3.emprestar()   # Já emprestado

    # Devolvendo
    print("\n--- Devoluções ---")
    livro1.devolver()
    livro3.devolver()

    # Agora é possível emprestar novamente
    print("\n--- Novo Empréstimo Após Devolução ---")
    livro1.emprestar()
    livro3.emprestar()
