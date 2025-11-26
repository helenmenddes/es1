# main.py
from models import Produto, Categoria
from dao import ProdutoDAO, CategoriaDAO

def main():
    categoria_dao = CategoriaDAO()
    produto_dao = ProdutoDAO()

    #categorias
    cat1 = Categoria(nome="Suplementos")
    cat2 = Categoria(nome="Roupas")
    cat1 = categoria_dao.create(cat1)
    cat2 = categoria_dao.create(cat2)
    print("Categorias criadas:")
    print(cat1)
    print(cat2)
    print("-" * 40)

    #produtos
    p1 = Produto(nome="Whey Protein", valor=199.90, categoria_id=cat1.id, associacao_tipo="belongs_to")
    p2 = Produto(nome="Camiseta DryFit", valor=79.90, categoria_id=cat2.id, associacao_tipo="belongs_to")
    p3 = Produto(nome="Creatina", valor=89.90, categoria_id=cat1.id, associacao_tipo="belongs_to")

    p1 = produto_dao.create(p1)
    p2 = produto_dao.create(p2)
    p3 = produto_dao.create(p3)

    print("Produtos criados:")
    print(p1)
    print(p2)
    print(p3)
    print("-" * 40)

    #alteracao valor do produto
    updated = produto_dao.update(3, {"valor": 99.90})
    if updated:
        print("Produto id=3 atualizado:")
        print(updated)
    else:
        print("Produto id=3 não encontrado para atualização.")
    print("-" * 40)

    #excluir produto
    deleted = produto_dao.delete(2)
    print(f"Produto id=2 deletion status: {'sucesso' if deleted else 'não encontrado'}")
    print("-" * 40)

    #lista das categorias
    categorias = categoria_dao.list_all()
    print("Todas as categorias:")
    for c in categorias:
        print(c)
    print("-" * 40)

    #lista dos produtos
    produtos = produto_dao.list_all()
    print("Produtos restantes:")
    for p in produtos:
        print(p)
    print("-" * 40)

    #printar categoria
    cat = categoria_dao.get_by_id(1)
    if cat:
        print("Categoria id=1:")
        print(cat)
        print("Produtos relacionados a essa categoria (se carregados):")
        
        produtos_relacionados = [p for p in produtos if p.categoria_id == cat.id]
        for pr in produtos_relacionados:
            print("  -", pr)
    else:
        print("Categoria id=1 não encontrada.")

if __name__ == "__main__":
    main()
