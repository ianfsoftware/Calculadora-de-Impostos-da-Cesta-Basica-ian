"""
Semana 3 — Reescrevendo com programação funcional
"""

from collections import namedtuple

ALIQUOTA_PADRAO = 0.25
ALIQUOTAS = {"cesta_basica": 0.0, "reduzido": 0.10, "padrao": 0.25}

Item = namedtuple("Item", ["nome", "preco", "categoria", "quantidade"], defaults=[1])


def aliquota(categoria):
    """Retorna a alíquota da categoria. ValueError se ela não existir."""
    if categoria not in ALIQUOTAS:
        raise ValueError(f"Categoria inválida: {categoria}")
    return ALIQUOTAS[categoria]


def imposto_item(item):
    """Imposto do item: o imposto unitário é arredondado antes de multiplicar."""
    return round(round(item.preco * aliquota(item.categoria), 2) * item.quantidade, 2)


def total_impostos(itens):
    """Soma dos impostos de todos os itens."""
    return round(sum(map(imposto_item, itens)), 2)


def total_compra(itens):
    """Soma de preço x quantidade mais os impostos."""
    subtotal = sum(map(lambda i: i.preco * i.quantidade, itens))
    return round(subtotal + total_impostos(itens), 2)

def filtrar_por_categoria(itens, categoria):
    """Lista nova apenas com os itens da categoria."""
    return list(filter(lambda i: i.categoria == categoria, itens))


def ordenar_por_preco(itens, decrescente=False):
    """Lista nova ordenada pelo preço unitário."""
    return sorted(itens, key=lambda i: i.preco, reverse=decrescente)


def economia_total(itens):
    """Quanto se pagaria a mais se todos os itens tivessem a alíquota padrão."""
    imposto_padrao = sum(
        map(lambda i: round(i.preco * ALIQUOTA_PADRAO, 2) * i.quantidade, itens)
    )
    return round(imposto_padrao - total_impostos(itens), 2)


if __name__ == "__main__":
    itens = [
        Item("Feijão 1kg", 8.00, "cesta_basica", 2),
        Item("Chocolate", 10.00, "padrao"),
    ]
    print(total_impostos(itens))  # 2.5
    print(total_compra(itens))    # 28.5
    print(economia_total(itens))  # 4.0