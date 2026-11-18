# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic, operações CRUD e respostas de erro.

## 📝 Tasks

### 🛠️ Implementar a listagem de livros

#### Descrição
Instale as dependências, execute o starter code e crie uma rota para listar os livros cadastrados. Use a documentação interativa do FastAPI para testar a rota.

```bash
python -m pip install fastapi uvicorn
python -m uvicorn starter-code:app --reload
```

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a coleção de livros cadastrados.
- Retornar uma lista vazia quando não houver livros.
- Permitir testar a rota pela documentação interativa em `/docs`.

### 🛠️ Criar livros com validação

#### Descrição
Implemente uma rota para adicionar livros ao catálogo. Use o modelo Pydantic fornecido no starter code para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Aceitar `POST /books` com um título e um autor no corpo JSON.
- Atribuir um identificador único ao novo livro e armazená-lo na coleção em memória.
- Retornar o livro criado com o status HTTP `201`.
- Rejeitar dados inválidos ou campos obrigatórios ausentes com o status HTTP `422`.

Exemplo de corpo da requisição:

```json
{
  "title": "The Little Prince",
  "author": "Antoine de Saint-Exupery"
}
```

### 🛠️ Completar as operações CRUD e tratar erros

#### Descrição
Adicione rotas para consultar, atualizar e remover um livro específico. Os dados podem permanecer em memória e não precisam sobreviver ao reinício do servidor.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books/{book_id}` com o livro correspondente.
- Aceitar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Aceitar `DELETE /books/{book_id}` para remover um livro existente e retornar o status HTTP `204` sem corpo.
- Retornar o status HTTP `404` quando uma operação buscar, atualizar ou remover um identificador inexistente.
- Expor todas as rotas e seus modelos na documentação interativa em `/docs`.
