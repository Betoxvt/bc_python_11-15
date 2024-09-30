from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI(
    debug=True
)  # Inicializa a API com debug para testes (não colocar na produção)
fake = Faker()

file_name = "data/products.csv"
df = pd.read_csv(file_name)
df["indice"] = range(
    1, len(df) + 1
)  # Cria uma coluna nova (indice) enumerando de 1 até o fim para ser utilizada depois
df.set_index("indice", inplace=True)

lojapadraoonline = 11


# Métodos chamando decorators para criar rotas (os endereços da página)
# Mostra a frase 'Coca-Cola me patrocina!'
@app.get("/")
async def hello_world():
    return "Coca-Cola me patrocina!"


# Método que gera dados fictícios de uma compra utilizando o faker
@app.get("/gerar_compra")
async def gerar_compra():  # Função está sobre a rota, em modo assíncrono, ela não bloqueia o código, não para/quebra a API.
    index = random.randint(
        1, len(df) - 1
    )  # Aqui ele escolhe um número aleatório de acordo com o número de linhas contendo dados no df
    tuple = df.iloc[index]  # Aqui ele pega a linha que saiu no random
    # Completa o exemplo de dados com dados faker para a compra (com mais dados que o necessário, para fazer uma filtragem mais a frente)
    return [
        {
            "client": fake.name(),  # nome fake
            "creditcard": fake.credit_card_provider(),  # bandeira de crédito fake
            "product": tuple["Product Name"],  # vem do arquivo de dados exemplo
            "ean": int(tuple["EAN"]),  # vem do exemplo
            "price": round(
                float(tuple["Price"]) * 1.2, 2
            ),  # vem do exemplo, e arredonda
            "clientPosition": fake.location_on_land(),  # localidade fake
            "store": lojapadraoonline,  # definido arbitrariamente acima
            "dateTime": fake.iso8601(),  # data fake no formato definido
        }
    ]


# Pega o número inserido na rota e a partir dele executa as ações
@app.get("/gerar_compras/{numero_registro}")  # o número é inserido na rota
async def gerar_compra(
    numero_registro: int,
):  # esse número é um argumento utilizado no parâmetro que serve de número de linhas

    if numero_registro < 1:
        return {"error": "O número deve ser maior que 1"}

    respostas = []  # abre o vetor que armazena cada linha criada
    for _ in range(numero_registro):  # aqui ele faz o loop para cada linha
        try:
            index = random.randint(1, len(df) - 1)
            tuple = df.iloc[index]
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": tuple["Product Name"],
                "ean": int(tuple["EAN"]),
                "price": round(float(tuple["Price"]) * 1.2, 2),
                "clientPosition": fake.location_on_land(),
                "store": lojapadraoonline,
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)  # armazena a linha no vetor de respostas
        except IndexError as e:
            print(f"Erro de índice: {e}")
        except ValueError as e:
            print(f"Erro inesperado: {e}")
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": "error",
                "ean": 0,
                "price": 0.0,
                "clientPosition": fake.location_on_land(),
                "store": lojapadraoonline,
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)
        except Exception as e:
            print(f"Erro inesperado: {e}")
    return respostas
