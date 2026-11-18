# 📘 Assignment: Unit Testing with unittest

## 🎯 Objective

Escreva testes automatizados para funções simples em Python usando o módulo `unittest`, que faz parte da biblioteca padrão. Você praticará organizar casos de teste, escolher verificações apropriadas e executar testes pela linha de comando.

## 📝 Tasks

### 🛠️ Escrever o primeiro teste unitário

#### Descrição
Renomeie `starter-code.py` para `calculator.py` e crie `test_calculator.py`. Importe a função `add` e escreva um teste para verificar a soma de dois números.

#### Requisitos
O programa concluído deve:

- Importar `unittest` e a função `add` do módulo `calculator`.
- Definir uma classe de testes que herde de `unittest.TestCase`.
- Definir um método de teste cujo nome comece com `test_`.
- Usar `self.assertEqual()` para confirmar que `add(2, 3)` retorna `5`.

### 🛠️ Testar resultados booleanos

#### Descrição
Adicione testes para a função `is_even`, verificando exemplos de números pares e ímpares.

#### Requisitos
O programa concluído deve:

- Verificar que `is_even(4)` retorna `True`.
- Verificar que `is_even(5)` retorna `False`.
- Usar `self.assertTrue()` e `self.assertFalse()` para expressar essas verificações.

### 🛠️ Verificar casos-limite e executar a suíte

#### Descrição
Teste a conversão de Celsius para Fahrenheit com valores comuns e um caso-limite. Depois, execute todos os testes com o descobridor do `unittest`.

#### Requisitos
O programa concluído deve:

- Verificar que `celsius_to_fahrenheit(0)` retorna `32`.
- Verificar que `celsius_to_fahrenheit(100)` retorna `212` e que `celsius_to_fahrenheit(-40)` retorna `-40`.
- Executar todos os testes com `python -m unittest -v` e obter resultado aprovado.
- Usar apenas a biblioteca padrão do Python, sem instalar dependências externas.
