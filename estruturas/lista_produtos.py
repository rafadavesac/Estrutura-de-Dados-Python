class NoProduto:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None


class ListaEncadeadaProdutos:
    def __init__(self):
        self.inicio = None

    def inserir_produto(self, produto):
        novo_no = NoProduto(produto)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def listar_produtos(self):
        lista = []
        atual = self.inicio

        while atual is not None:
            lista.append(atual.produto)
            atual = atual.proximo

        return lista

    def buscar_por_id(self, id_produto):
        atual = self.inicio

        while atual is not None:
            if atual.produto.id_produto == id_produto:
                return atual.produto
            atual = atual.proximo

        return None

    def buscar_por_nome(self, nome):
        encontrados = []
        atual = self.inicio

        nome = nome.strip().lower()

        while atual is not None:
            if nome in atual.produto.nome.lower():
                encontrados.append(atual.produto)
            atual = atual.proximo

        return encontrados

    def id_ja_existe(self, id_produto):
        atual = self.inicio

        while atual is not None:
            if atual.produto.id_produto == id_produto:
                return True
            atual = atual.proximo

        return False

    def nome_ja_existe(self, nome):
        atual = self.inicio
        nome = nome.strip().lower()

        while atual is not None:
            if atual.produto.nome.strip().lower() == nome:
                return True
            atual = atual.proximo

        return False

    def lista_vazia(self):
        return self.inicio is None

    def contar_produtos(self):
        contador = 0
        atual = self.inicio

        while atual is not None:
            contador += 1
            atual = atual.proximo

        return contador

    def remover_ultimo(self):
        if self.inicio is None:
            return None

        if self.inicio.proximo is None:
            produto_removido = self.inicio.produto
            self.inicio = None
            return produto_removido

        atual = self.inicio
        while atual.proximo.proximo is not None:
            atual = atual.proximo

        produto_removido = atual.proximo.produto
        atual.proximo = None
        return produto_removido

    def calcular_valor_total_estoque(self):
        total = 0
        atual = self.inicio

        while atual is not None:
            total += atual.produto.quantidade * atual.produto.preco
            atual = atual.proximo

        return total