import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import streamlit as st

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Variáveis de conexão ao banco de dados
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'ferreira@))1')
DB_NAME = os.getenv('DB_NAME', 'imoveis_db')

# Função para conectar ao banco de dados
def get_connection():
    try:
        logging.info("Conectando ao banco de dados...")
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            logging.info("Conexão estabelecida com sucesso.")
            return conn
    except Error as e:
        logging.error(f"Erro ao conectar ao banco de dados: {e}")
        raise Exception(f"Erro ao conectar ao banco de dados: {e}")

# Função para inicializar o banco de dados
def initialize_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS imoveis_db")
        cursor.execute("USE imoveis_db")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS imoveis (
                id INT AUTO_INCREMENT PRIMARY KEY,
                tipo_operacao VARCHAR(50) NOT NULL,
                fiador VARCHAR(20) DEFAULT 'Não se aplica',
                seguro_fianca VARCHAR(20) DEFAULT 'Não se aplica',
                adiantamento_alugueis INT DEFAULT 0,
                quitado VARCHAR(20) DEFAULT 'Não se aplica',
                financiamento_qtd_parcelas INT DEFAULT 0,
                financiamento_valor_parcela FLOAT DEFAULT 0.0,
                endereco VARCHAR(255) NOT NULL,
                bairro VARCHAR(100) NOT NULL,
                cidade VARCHAR(100) NOT NULL,
                uf VARCHAR(2) NOT NULL,
                area_total FLOAT DEFAULT 0.0,
                area_util FLOAT DEFAULT 0.0,
                area_construida FLOAT DEFAULT 0.0,
                valor FLOAT DEFAULT 0.0,
                iptu FLOAT DEFAULT 0.0,
                condominio FLOAT DEFAULT 0.0,
                tipo_imovel VARCHAR(50) NOT NULL,
                caracteristicas TEXT,
                nome_proprietario VARCHAR(100) NOT NULL,
                telefone_proprietario VARCHAR(20) NOT NULL,
                email_proprietario VARCHAR(100),
                observacoes TEXT
            );
        ''')
        conn.commit()
        logging.info("Banco de dados inicializado com sucesso.")
    except Error as e:
        logging.error(f"Erro ao inicializar banco de dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()

# Inicializar o banco de dados
initialize_database()

# Ecolha de operação
st.title("Cadastro de Imóveis")
operacao = st.selectbox("Escolha a operação", ["Venda", "Locação"])

# Formulário de entrada de dados
def form_imovel(operacao):
    st.header(f"Cadastro de {operacao}")

    # Localização
    st.subheader("Localização")
    loc_cols = st.columns(2)

    with loc_cols[0]:
        endereco = st.text_input("Endereço")
        uf = st.text_input("UF")
    with loc_cols[1]:
        bairro = st.text_input("Bairro")
        cidade = st.text_input("Cidade")
    
    # Áreas
    area_cols = st.columns(3)

    with area_cols[0]:
        area_total = st.number_input("Área Total", min_value=0.0, step=0.01)
    with area_cols[1]:
        area_util = st.number_input("Área Útil", min_value=0.0, step=0.01)
    with area_cols[2]:
        area_construida = st.number_input("Área Construída", min_value=0.0, step=0.01)

    # Campos específicos
    if operacao == "Venda":
        venda_cols = st.columns(3)

        with venda_cols[0]:
            quitado = st.selectbox("Quitado", ["Sim", "Não"])
        with venda_cols[1]:
            financiamento_qtd_parcelas = st.number_input("Quantidade de Parcelas", min_value=0, step=1)
        with venda_cols[2]:
            financiamento_valor_parcela = st.number_input("Valor da Parcela", min_value=0.0, step=0.01)

    else:
        locacao_cols = st.columns(3)

        with locacao_cols[0]:
            fiador = st.text_input("Fiador")
        with locacao_cols[1]:
            seguro_fianca = st.text_input("Seguro Fiança")
        with locacao_cols[2]:
            adiantamento_alugueis = st.number_input("Adiantamento de Aluguéis", min_value=0, step=1)

    # Valores
    valor_cols = st.columns(3)

    with valor_cols[0]:
        valor = st.number_input("Valor", min_value=0.0, step=0.01)
    with valor_cols[1]:
        iptu = st.number_input("IPTU", min_value=0.0, step=0.01)
    with valor_cols[2]:
        condominio = st.number_input("Condomínio", min_value=0.0, step=0.01)

    # Imóvel
    st.subheader("Características")
    tipo_imovel = st.text_input("Tipo de Imóvel")

    cat_cols = st.columns(4)

    with cat_cols[0]:
        dormitorio = st.number_input("Dormitórios", min_value=0, step=1)
        cozinha = st.number_input("Cozinhas", min_value=0, step=1)
        lavabo = st.number_input("Lavabos", min_value=0, step=1)
        banheiros = st.number_input("Banheiros", min_value=0, step=1)
        area_servico = st.number_input("Área de Serviço", min_value=0, step=1)
        piscina = st.number_input("Piscina", min_value=0, step=1)
        sauna = st.number_input("Sauna", min_value=0, step=1)
        suites = st.number_input("Suítes", min_value=0, step=1)
    with cat_cols[1]:
        despensa = st.number_input("Despensa", min_value=0, step=1)
        sala_estar = st.number_input("Sala de Estar", min_value=0, step=1)
        lavanderia = st.number_input("Lavanderia", min_value=0, step=1)
        hidromassagem = st.number_input("Hidromassagem", min_value=0, step=1)
        quintal = st.number_input("Quintal", min_value=0, step=1)
        salao_festas = st.number_input("Salão de Festas", min_value=0, step=1)
        churrasqueira = st.number_input("Churrasqueira", min_value=0, step=1)

    with cat_cols[2]:
        closet = st.number_input("Closet", min_value=0, step=1)
        armarios = st.number_input("Armários", min_value=0, step=1)
        lareira = st.number_input("Lareira", min_value=0, step=1)
        dep_empregada = st.number_input("Dep. de Empregada", min_value=0, step=1)
        aquecedor = st.number_input("Aquecedor", min_value=0, step=1)
        playground = st.number_input("Playground", min_value=0, step=1)
        salao_jogos = st.number_input("Salão de Jogos", min_value=0, step=1)

    with cat_cols[3]:
        garagem = st.number_input("Garagens", min_value=0, step=1)
        sacada = st.number_input("Sacada", min_value=0, step=1)
        copa = st.number_input("Copa", min_value=0, step=1)
        sala_jantar = st.number_input("Sala de Jantar", min_value=0, step=1)
        wc_empregada = st.number_input("WC Empregada", min_value=0, step=1)
        gas_encanado = st.number_input("Gás Encanado", min_value=0, step=1)
        quadra = st.number_input("Quadra", min_value=0, step=1)
        academia = st.number_input("Academia", min_value=0, step=1)

    # Proprietário
    st.subheader("Proprietário")

    nome_proprietario = st.text_input("Nome do Proprietário")
    endereco_proprietario = st.text_input("Endereço do Proprietário")

    prop_cols = st.columns(3)

    with prop_cols[0]:
        bairro_proprietario = st.text_input("Bairro do Proprietário")
        telefone_proprietario = st.text_input("Telefone do Proprietário")
    with prop_cols[1]:
        cidade_proprietario = st.text_input("Cidade do Proprietário")
        celular_proprietario = st.text_input("Celular do Proprietário")
    with prop_cols[2]:
        uf_proprietario = st.text_input("UF do Proprietário")
        email_proprietario = st.text_input("Email do Proprietário")

    # Observações
    st.subheader("Observações")
    observacoes = st.text_area("Observações")

    # Botão para salvar os dados
    if st.button("Salvar"):
        save_data()

# Botão para salvar os dados
def save_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO imoveis (
                tipo_operacao, 
                fiador,
                seguro_fianca,
                adiantamento_alugueis,
                quitado,
                financiamento_qtd_parcelas,
                financiamento_valor_parcela,
                endereco, 
                bairro, 
                cidade, 
                uf, 
                area_total, 
                area_util, 
                area_construida,
                valor, 
                iptu, 
                condominio, 
                tipo_imovel, 
                caracteristicas, 
                nome_proprietario,
                telefone_proprietario, 
                email_proprietario, 
                observacoes
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            tipo_operacao, fiador, seguro_fianca, adiantamento_alugueis, quitado,
            financiamento_qtd_parcelas, financiamento_valor_parcela, endereco, bairro,
            cidade, uf, area_total, area_util, area_construida, valor, iptu, condominio,
            tipo_imovel, caracteristicas, nome_proprietario, telefone_proprietario,
            email_proprietario, observacoes
        ))
        conn.commit()
        st.success("Dados salvos com sucesso!")
    except Error as e:
        st.error(f"Erro ao salvar dados: {e}")
        logging.error(f"Erro ao salvar dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()

# Executar o formulário
form_imovel(operacao)