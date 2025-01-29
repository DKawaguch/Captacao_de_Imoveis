# Captação de Imóveis

Esta aplicação foi desenvolvida para facilitar o gerenciamento de imóveis, permitindo o cadastro e a consulta de informações em uma base de dados de maneira prática e intuitiva.

## Objetivo do Projeto

Automatizar o processo de cadastro e consulta de imóveis, fornecendo uma interface de fácil uso para entrada e busca de informações relevantes sobre propriedades imobiliárias.

## Funcionalidades

- **Cadastro de Imóveis**:
  - Informações detalhadas sobre localização, características e valores do imóvel.
  - Dados do proprietário.
- **Consulta de Imóveis**:
  - Busca utilizando múltiplos filtros, como endereço, tipo de operação (venda ou aluguel), características do imóvel e valores.
  - Visualização dos detalhes dos imóveis cadastrados.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Frameworks e Bibliotecas**:
  - Streamlit (Interface de usuário)
  - MySQL Connector (Conexão com o banco de dados)
  - dotenv (Carregamento de variáveis de ambiente)
- **Banco de Dados**: MySQL

## Estrutura do Projeto

```plaintext
config/
├── settings.py           # Configurações de usuário para o SQL
database/
├── imoveis_db.sql        # Schema para armazenamento da base de dados
logs/
├── imovel_app.logs       # logs do app
src/
├── imoveis_cadastro.py   # Funções para cadastro de imóveis
├── imoveis_consulta.py   # Funções para consulta de imóveis
├── data_connection.py    # Conexão e inicialização do banco de dados
├── Main.py               # Interação principal com o usuário e junção das funções
├── wrapper.py               # Iniciação do projeto
.env
requirements.txt
```

## Como Configurar e Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/DKawaguch/Captacao_de_Imoveis.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente no arquivo `.env`:
   ```plaintext
   DB_HOST=seu_host
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=imoveis_db
   ```
4. Inicialize o banco de dados:
   ```bash
   python -c "from src.data_connection import initialize_database; initialize_database()"
   ```
5. Execute a aplicação Streamlit:
   ```bash
   streamlit run src/imoveis_cadastro.py
   ```

## Como Utilizar

- **Cadastro de Imóveis**:
  1. Preencha os campos do formulário com as informações do imóvel.
  2. Clique no botão de salvar para armazenar os dados no banco.
- **Consulta de Imóveis**:
  1. Insira os filtros desejados na interface de consulta.
  2. Visualize os resultados filtrados e os detalhes dos imóveis.

## Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção de bug:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Descrição da alteração"
   ```
4. Faça um push para sua branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Contato

Para dúvidas ou sugestões:

- Autor: DKawaguch
- Email: dkawaguchi@hotmail.com
