# python-data-science-foundations

Repositório referente ao curso gratuito  
**Fundamentos de Linguagem Python Para Análise de Dados e Data Science**  
da **Data Science Academy**.

Este projeto contém exercícios, labs e pequenos projetos desenvolvidos ao longo do curso, com foco em:

- Fundamentos da linguagem Python
- Manipulação de dados
- Programação orientada a objetos
- Automação básica
- Introdução a projetos de Data Science

---

## Conteúdos Abordados

### Fundamentos de Python

- Números
- Variáveis
- Strings
- Listas
- Dicionários
- Tuplas
- Condicionais (`if / else`)
- Laços (`for`, `while`, `range`)
- Métodos
- Funções
- Expressões lambda
- List comprehension

### Manipulação de Dados e Programação Funcional

- Arquivos
- `map`, `reduce`, `filter`
- `zip`
- `enumerate`
- Tratamento de erros e exceções

### Programação Orientada a Objetos

- Classes
- Objetos
- Métodos
- Herança
- Polimorfismo

### Bibliotecas para Data Science

- NumPy
- Pandas
- Matplotlib
- Seaborn

### Análise de Dados e Machine Learning

- SQL
- Statsmodels
- Scikit-learn
- Séries temporais
- Introdução a Deep Learning

---

## Como executar os projetos

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/python-data-science-foundations.git
cd python-data-science-foundations
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instale as dependências necessárias

```bash
pip install openai
```

### 4. Configure a variável de ambiente (para projetos com OpenAI)

No PowerShell:

```ps
setx OPENAI_API_KEY "SUA_CHAVE_AQUI"
```

Depois feche e abra o terminal.

Teste:

```bash
python -c "import os; print(os.getenv('OPENAI_API_KEY'))"
```

### 5. Execute um projeto

Exemplo (chatbot):

```bash
python cap19/projeto-3/chatbot.py
```

Observações

- As chaves de API não devem ser colocadas diretamente no código.
- Utilize sempre variáveis de ambiente.
- Este repositório tem finalidade educacional.
- Projeto criado como parte do aprendizado em Python, Data Science e Machine Learning.
