# Bootcamp Python para dados - Programação Orientada a Objetos (POO)

# Aula 11 - Introdução a POO

## Básico
É um paradigma da programação.
* Quando a função está dentro de uma classe, se chama método.
* `__init__` é um método (fuynção) que inicia sempre que a classe é chamada. Roda automaticamente quando se chama a classe.
* `self` cada um só fala com si próprio, sem os métodos falarem um com o outro. Com as propriedades exclusivas dessa classe. Dentro dessa classe.
* Classes criam instâncias e ficam na memória

## Herança
* Os métodos são herdados de uma classe incial. Você tipo cria uma classe que fica dentro de outra classe. A classe "filha" chama a classe "mãe".
* super() dá o direito dentro dessa classe acessar o método da classe "mãe"

## Encapsulamento
Criar uma classe na qual eu não de a obrigação ao desenvolvedor de cuidar das das conexões ou dos atributos.

# Aula 12 - Introdução às Classes em Python
As classes se tornam mais interessantes de usar quando há uma maior complexidade do código.

Não é sobre facilidade, é sobre desenvolvimento. Facilita para os outros que vão utilizar o código.

`self` serve para deixar os parâmetros já carregados em uma classe. Cada instância fica separada.

Recursividade: Quando sua classe chama ela mesma

# Aula 13 e 14 - Herança e Polimorfismo

### Desafio: Minha empresa recebe arquivos nos formatos .csv e .txt em duas pastas distintas, e preciso consolidá-los em um único dataframe.

Qual seria a melhor abordagem para realizar essa tarefa?

paths:          |   format:

data/csv_files  |   id,name

data/txt_files  |   id  name

data/json_files |   {"id":foo, "name":"bar"}

### Estrutura do projeto

    `src/__main__.py` invocação dos métodos, instanciação das classes

    `src/lib/classes/*.py` arquivos das classes, __init__, AbstractDataSource, CsvSource, FilesSources, TxtSource

### AbstractDataSource.py:
Receber dados de fontes genéricas. Garante que todos os desenvolvedores que usarem essa classe tem que escrever estes métodos.

Classe que herda as caracteristicas da classe nativa do python ABC.

* Classes abstratas: from abc import ABC, abstractmethod
ABC > PEP 3119 > garantir a função tenha todos os requerimentos para classe abstrata
* abstractmethod > decorator que valida se o método é abstrato e obriga a próxima classe (herdeiros) a ter os métodos da classe anterior.

### FilesSources.py:
"O chefe só restringiu a métodos de arquivos"

Um método para implementar o que há de comum entre diversos tipos de arquivos.

* Método só para arquivos, cria os arquivos anteriores e aplica o metodo start()
* Método genérico que cria path quando não há. A partir daqui pode fazer um polimorfismo, pegar o método que já existe e muda-lo para a classe herdeira para que se encaixe no contexto secundário.
* Lê a pasta para detectar arquivos atuais, se os arquivos não estão na variável de arquivos anteriores, ela adiciona na lista de novos arquivos e atualiza a arquivos anteriores. Se não há nada novo nada ocorre.

### CsvSource.py

Herda os comportamentos do FilesSources.py que herda do AbstractDataSource.py

* Reescreve os métodos (da classe anterior) de genérico para definir o arquivo como sendo csv.
* Para incluir os novos arquivos encontrados ele também verifica se terminam com '.csv'

### TxtSource.py

Igual a do CSV, só que troca CSV por TXT.

* Poderia ter feito uma função dinâmica que recebe o tipo de arquivo, mas foi escrito assim para mostrar o polimorfismo

### JsonSource.py

Mesmo jeito...

## Falta implementar

### CsvSourceS3.py

Herda da classe CsvSource.py busca arquivos na AWS S3.

### TxtSourceS3.py

Herda da classe TxtSource.py mas busca arquivos na AWS S3.

### JsonSourceS3.py

Herda da classe JsonSource.py mas busca arquivos na AWS S3.

### aws/s3.py

Classe para fonte com origem em cloud AWS s3.

s3 -> trigger -> ec2 ou lambda ou ecs

# Aula 15 - Finalizando POO com uma API teste

Aplicar classes para fazer abstrações com intenção de esconder, ou seja, encapsular os serviços (funções e métodos). Permite no futuro a mudança de serviços utilizando as mesmas classes. Assim o código pode ficar robusto, durar muito tempo e ser flexível/dinâmico

## FastAPI > Criar a API
REST API: Mudanças de plataforma ou tecnologia na aplicação do servidor não afetam a aplicação do cliente.

1. Transforma funções em API
2. Métodos HTTP:

        .get    = SELECT -> recebe algum dado
        .post   = INSERT -> envia dados para o servidor
        .put    = UPDATE -> faz alteração de dados
        .delete = DELETE -> deleta dados
3. Cria docs da API
4. Pode mandar a rota pro Postman (API Platform) para ter mais controle e melhora a leitura, também gera o código de request.

## Faker > Gera dados de teste (números, nomes, atributos, cód. de barra...)
