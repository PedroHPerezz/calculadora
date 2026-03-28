# 🧮 Calculadora em Python

Este projeto é uma calculadora interativa em Python com suporte a:

* Operações matemáticas básicas
* Operações avançadas (raiz, potência, porcentagem)
* Histórico de cálculos
* Conversões entre sistemas numéricos (binário, octal, decimal e hexadecimal)

---

## 📌 Funcionalidades

### ➕ 1. Cálculos Matemáticos

Permite realizar operações como:

* Adição (`+`)
* Subtração (`-`)
* Multiplicação (`*`)
* Divisão (`/`)
* Raiz (`r`)
* Porcentagem (`%`)
* Potência (`**`)

O usuário pode continuar operando com o resultado anterior.

---

### 📜 2. Histórico

* Armazena todas as operações realizadas
* Exibe o histórico em linhas separadas
* Exemplo:

```
[5 + 3 = 8]
[8 * 2 = 16]
```

---

### 🧹 3. Limpar Histórico

* Remove todos os cálculos armazenados

---

### 🔢 4. Conversões Numéricas

Suporte para conversão entre:

| De          | Para        |
| ----------- | ----------- |
| Decimal     | Binário     |
| Binário     | Decimal     |
| Decimal     | Octal       |
| Octal       | Decimal     |
| Decimal     | Hexadecimal |
| Hexadecimal | Decimal     |
| Hexadecimal | Binário     |
| Binário     | Hexadecimal |
| Hexadecimal | Octal       |
| Octal       | Hexadecimal |

---

### ❌ 5. Encerrar Programa

Finaliza a execução da calculadora

---

## 🛠️ Estrutura do Projeto

```
📁 projeto/
│
├── main.py          # Código principal (este arquivo)
├── calculos.py      # Funções matemáticas (importadas)
└── README.md        # Documentação
```

---

## 📦 Dependências

Nenhuma biblioteca externa é necessária.
O projeto utiliza apenas recursos nativos do Python.

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado
2. Execute o arquivo principal:

```bash
python main.py
```

---

## 💡 Exemplo de Uso

```
Selecione a ação:
1 - Calcular
2 - Histórico
3 - Limpar
4 - Finalizar
5 - Calcular binário
```

---

## ⚠️ Tratamento de Erros

O programa trata entradas inválidas usando `try/except`, garantindo que:

* Apenas números válidos sejam aceitos
* O programa não quebre com entradas incorretas

---

## 🚀 Melhorias Futuras

* Interface gráfica (GUI)
* Salvamento do histórico em arquivo
* Suporte a mais operações matemáticas
* Melhor formatação do histórico

---

## 👨‍💻 Autor

Projeto desenvolvido para prática de lógica de programação em Python.
