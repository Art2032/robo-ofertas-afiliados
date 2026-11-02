import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
ARQUIVO = ROOT / "data" / "produtos.json"
DESCONTO_MINIMO = 20
LOJAS_PERMITIDAS = {"Shopee", "Mercado Livre"}


def url_https_valida(valor):
    try:
        partes = urlparse(valor)
        return partes.scheme == "https" and bool(partes.netloc)
    except (TypeError, ValueError):
        return False


def validar(produto):
    erros = []
    for campo in ("loja", "id", "nome", "url_afiliado", "imagem_url"):
        if not produto.get(campo):
            erros.append(f"campo obrigatório ausente: {campo}")

    if produto.get("loja") not in LOJAS_PERMITIDAS:
        erros.append("loja não permitida")

    if not url_https_valida(produto.get("url_afiliado", "")):
        erros.append("link de afiliado precisa ser HTTPS válido")

    if not url_https_valida(produto.get("imagem_url", "")):
        erros.append("imagem precisa ter URL HTTPS válida")

    try:
        atual = float(produto["preco_atual"])
        anterior = float(produto["preco_anterior"])
        desconto = float(produto["desconto_percentual"])
        if atual <= 0 or anterior <= 0 or atual > anterior:
            erros.append("preços inválidos")
        if desconto < DESCONTO_MINIMO:
            erros.append(f"desconto abaixo de {DESCONTO_MINIMO}%")
    except (KeyError, TypeError, ValueError):
        erros.append("preços ou desconto ausentes/inválidos")

    return erros


def main():
    if not ARQUIVO.exists():
        raise SystemExit(f"Arquivo não encontrado: {ARQUIVO}")

    produtos = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    if not isinstance(produtos, list):
        raise SystemExit("O arquivo deve conter uma lista JSON.")

    vistos = set()
    aceitos = 0

    for produto in produtos:
        erros = validar(produto)
        identificador = (produto.get("loja"), produto.get("id"))

        if identificador in vistos:
            erros.append("produto duplicado nesta execução")
        vistos.add(identificador)

        if erros:
            print(f"REJEITADO: {produto.get('nome', 'sem nome')} — {'; '.join(erros)}")
            continue

        aceitos += 1
        print(
            f"VALIDADO: {produto['nome']} | {produto['loja']} | "
            f"R$ {float(produto['preco_atual']):.2f} | "
            f"desconto cadastrado: {float(produto['desconto_percentual']):.1f}% | "
            f"{produto['url_afiliado']}"
        )

    print(f"\nConcluído: {aceitos} produto(s) validado(s).")
    print("Atenção: preços/descontos são dados cadastrados; não foram conferidos na loja.")
    print("Esta versão ainda não coleta ofertas nem publica nas redes sociais.")


if __name__ == "__main__":
    main()
