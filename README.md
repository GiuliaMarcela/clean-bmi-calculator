# Calculadora de IMC em Python

Este projeto é uma calculadora de Índice de Massa Corporal (IMC) desenvolvida em Python
como requisito parcial para a obtenção da média semestral na disciplina de Linguagem de Programação.

## Descrição do Projeto

O Índice de Massa Corporal (IMC) é uma medida comum usada para avaliar a saúde de uma pessoa com
base
em seu peso e altura. Essa calculadora permite que o usuário insira seu peso (em quilogramas/libras)
e sua altura (em metros/polegadas) e calcula o IMC correspondente. Além disso, o programa fornece
uma descrição do IMC, indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso ou
com obesidade.

## Pré-requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Python 3.x

### Instalação

1. Clone este repositório em seu ambiente de desenvolvimento
2. Navegue para a pasta do projeto
3. Crie um ambiente virtual com o venv

```shell
python -m venv venv
```

4. Ative-o

> **OBS**: Os caminhos abaixo foram escritos baseados na arquitetura de um sistema windows.

```shell
### Windows
# Powershell
.\venv\Scripts\Activate.ps1

# Command Prompt
.\venv\Scripts\activate.bat

# Shell
.\venv\Scripts\activate
```

4. Instale as dependências usando o pip

```shell
pip install -r .\requirements.txt
```

## Uso

Para executar a calculadora de IMC, siga as etapas abaixo:

1. Navegue até o diretório do projeto (caso ainda não esteja)
2. Execute o programa

```shell
# Para exibir a mensagem de ajuda da calculadora
python main.py --help

# Para realizar o cálculo - (Unidade de medida métrica)
# Altura em metros
# Peso em quilogramas
python main.py calculate --height 64 --weight 1.64
python main.py calculate --height 64 --weight 164

# Para realizar o cálculo - (Unidade de medida imperial)
# Altura em polegadas
# Peso em libras
python main.py calculate --unit imperial --height 70 --weight 200
python main.py calculate --unit imperial --height 72 --weight 150
```

## Testes

O projeto inclui alguns testes unitários para garantir que a calculadora de IMC funcione corretamente.
Para executar os testes, siga as etapas a seguir:

Assumindo que você já está com o ambiente virtual ativo e dentro da pasta do projeto
- Execute o comando:

```shell
pytest
```

Os testes devem ser executados e você receberá o feedback com o resultado dos testes.

# Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório, criar um branch
e enviar um pull request com suas melhorias.

# Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
