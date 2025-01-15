import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
import logging

# Configuração básica do log
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_connection():
    try:
        logging.info("Tentando conectar ao banco de dados MySQL...")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ferreira@))1",
            database="imoveis_db"
        )
        if conn.is_connected():
            logging.info("Conexão com o banco de dados estabelecida com sucesso.")
            return conn
    except Error as e:
        logging.error(f"Erro ao conectar ao MySQL: {e}")
        raise Exception(f"Erro ao conectar ao MySQL: {e}")
    
def initialize_database():
    logging.info("Inicializando o banco de dados...")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS imoveis_db")
        cursor.execute("USE imoveis_db")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS imoveis (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo_operacao VARCHAR(50) NOT NULL,  -- Locação ou Venda
            endereco VARCHAR(255) NOT NULL,
            bairro VARCHAR(100) NOT NULL,
            cidade VARCHAR(100) NOT NULL,
            uf VARCHAR(2) NOT NULL,             -- Unidade Federativa
            area_total FLOAT DEFAULT 0.0,       -- Área Total em m²
            area_util FLOAT DEFAULT 0.0,        -- Área Útil em m²
            area_construida FLOAT DEFAULT 0.0,  -- Área Construída em m²
            valor FLOAT DEFAULT 0.0,            -- Valor (R$) - Locação ou Venda
            iptu FLOAT DEFAULT 0.0,             -- Valor do IPTU (R$)
            condominio FLOAT DEFAULT 0.0,       -- Condomínio Mensal (R$)
            tipo_imovel VARCHAR(50) NOT NULL,   -- Tipo de Imóvel
            caracteristicas TEXT,               -- Características do Imóvel (lista concatenada)
            nome_proprietario VARCHAR(100) NOT NULL,
            telefone_proprietario VARCHAR(20) NOT NULL,
            email_proprietario VARCHAR(100),
            observacoes TEXT                    -- Observações adicionais
        );
        """)
        conn.commit()
        logging.info("Banco de dados e tabelas inicializados com sucesso.")
    except Error as e:
        logging.error(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()

def salvar_dados(novo_registro):
    logging.info(f"Tentando salvar os seguintes dados no banco: {novo_registro}")
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO imoveis (
            tipo_operacao, endereco, bairro, cidade, uf, area_total, area_util, area_construida,
            valor, iptu, condominio, tipo_imovel, caracteristicas, nome_proprietario,
            telefone_proprietario, email, observacoes
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(novo_registro.values()))
        conn.commit()
        logging.info("Dados salvos com sucesso!")
        st.success("Dados salvos com sucesso!")
        st.write("Registro salvo:")
        st.json(novo_registro)  # Mostra o registro salvo no front-end.
    except Error as e:
        logging.error(f"Erro ao salvar os dados: {e}")
        st.error(f"Erro ao salvar os dados: {e}")
        print(f"Erro: {e}")
    finally:
        if conn.is_connected():
            conn.close()

initialize_database()

# Título
st.title("Cadastro de Imóveis")
'''
# Inicializando o DataFrame local para armazenar dados
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(
        columns=[
            "Tipo", "Endereço", "Bairro", "Cidade", "UF", "Área Total (m²)",
            "Área Útil (m²)", "Área Construída (m²)", "Valor (R$)", "IPTU (R$)",
            "Condomínio Mensal (R$)", "Tipo de Imóvel", "Características",
            "Nome Proprietário", "Telefone", "E-mail", "Observações"
        ]
    )
data = st.session_state["data"]
# Conectando ao banco de dados MySQL e carregando os dados
try:
    conn = get_connection()
    query = "SELECT * FROM imoveis"
    data = pd.read_sql(query, conn)
    st.session_state["data"] = data
    conn.close()
except Error as e:
    st.error(f"Erro ao carregar os dados do banco de dados: {e}")
'''
# Inicializando o estado da sessão
if "tipo_operacao" not in st.session_state:
    st.session_state["tipo_operacao"] = "Locação"
    st.session_state["endereco"] = ""
    st.session_state["bairro"] = ""
    st.session_state["cidade"] = ""
    st.session_state["uf"] = ""
    st.session_state["area_total"] = 0.0
    st.session_state["area_util"] = 0.0
    st.session_state["area_construida"] = 0.0
    st.session_state["valor_locacao"] = 0.0
    st.session_state["valor_venda"] = 0.0
    st.session_state["iptu"] = 0.0
    st.session_state["condominio"] = 0.0
    st.session_state["tipo_imovel"] = "Casa Térrea"
    st.session_state["caracteristicas_imovel"] = []
    st.session_state["nome_proprietario"] = ""
    st.session_state["telefone_proprietario"] = ""
    st.session_state["email_proprietario"] = ""
    st.session_state["observacoes"] = ""

# Função para resetar o formulário
def reset_form():
    st.session_state["tipo_operacao"] = "Locação"
    st.session_state["endereco"] = ""
    st.session_state["bairro"] = ""
    st.session_state["cidade"] = ""
    st.session_state["uf"] = ""
    st.session_state["area_total"] = 0.0
    st.session_state["area_util"] = 0.0
    st.session_state["area_construida"] = 0.0
    st.session_state["valor_locacao"] = 0.0
    st.session_state["valor_venda"] = 0.0
    st.session_state["iptu"] = 0.0
    st.session_state["condominio"] = 0.0
    st.session_state["tipo_imovel"] = "Casa Térrea"
    st.session_state["caracteristicas_imovel"] = []
    st.session_state["nome_proprietario"] = ""
    st.session_state["telefone_proprietario"] = ""
    st.session_state["email_proprietario"] = ""
    st.session_state["observacoes"] = ""

# Escolha entre Locação ou Venda
st.session_state["tipo_operacao"] = st.radio("Escolha a operação:", ["Locação", "Venda"], index=["Locação", "Venda"].index(st.session_state["tipo_operacao"]))

st.subheader("Localização do Imóvel")
st.session_state["endereco"] = st.text_input("Endereço", st.session_state["endereco"])
st.session_state["bairro"] = st.text_input("Bairro", st.session_state["bairro"])
st.session_state["cidade"] = st.text_input("Cidade", st.session_state["cidade"])
ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
st.session_state["uf"] = st.selectbox("UF", ufs, index=ufs.index(st.session_state["uf"]) if st.session_state["uf"] else 0)
st.session_state["area_total"] = st.number_input("Área Total (m²)", min_value=0.0, step=1.0, value=st.session_state["area_total"])
st.session_state["area_util"] = st.number_input("Área Útil (m²)", min_value=0.0, step=1.0, value=st.session_state["area_util"])
st.session_state["area_construida"] = st.number_input("Área Construída (m²)", min_value=0.0, step=1.0, value=st.session_state["area_construida"])

if st.session_state["tipo_operacao"] == "Locação":
    st.session_state["valor_locacao"] = st.number_input("Valor da Locação (R$)", min_value=0.0, step=1.0, value=st.session_state["valor_locacao"])
    st.session_state["iptu"] = st.number_input("Valor do IPTU (R$)", min_value=0.0, step=1.0, value=st.session_state["iptu"])
    st.session_state["condominio"] = st.number_input("Condomínio Mensal (R$)", min_value=0.0, step=1.0, value=st.session_state["condominio"])
else:  # Venda
    st.session_state["valor_venda"] = st.number_input("Valor do Imóvel (R$)", min_value=0.0, step=1.0, value=st.session_state["valor_venda"])
    st.session_state["iptu"] = st.number_input("Valor do IPTU (R$)", min_value=0.0, step=1.0, value=st.session_state["iptu"])
    st.session_state["condominio"] = st.number_input("Condomínio Mensal (R$)", min_value=0.0, step=1.0, value=st.session_state["condominio"])

# Tipo de Imóvel (Escolha única)
st.subheader("Tipo de Imóvel")
tipos = [
    "Casa Térrea", "Sobrado", "Apartamento", "Terreno", "Sítio",
    "Chácara", "Galpão", "Assobradado", "Fazenda", "Indústria"
]
st.session_state["tipo_imovel"] = st.radio("Selecione o tipo de imóvel:", tipos, index=tipos.index(st.session_state["tipo_imovel"]))

# Características do Imóvel
st.subheader("Características do Imóvel")
caracteristicas = [
    "Dormitórios", "Suítes", "Cozinha", "Banheiros", "Área de Serviço",
    "Lavabo", "Garagem", "Piscina", "Hidromassagem", "Churrasqueira",
    "Quintal", "Sacada", "Playground", "Salão de Festas", "Salão de Jogos",
    "Edícula", "WC Empregada", "Lareira", "Armários", "Closet"
]
st.session_state["caracteristicas_imovel"] = st.multiselect("Selecione as características:", caracteristicas, default=st.session_state["caracteristicas_imovel"])

# Dados do Proprietário
st.subheader("Dados do Proprietário")
st.session_state["nome_proprietario"] = st.text_input("Nome do Proprietário", st.session_state["nome_proprietario"])
st.session_state["telefone_proprietario"] = st.text_input("Telefone do Proprietário", st.session_state["telefone_proprietario"])
st.session_state["email_proprietario"] = st.text_input("E-mail do Proprietário", st.session_state["email_proprietario"])

# Observações
st.session_state["observacoes"] = st.text_area("Observações", st.session_state["observacoes"])

# Botão para salvar os dados
if st.button("Salvar"):
    novo_registro = {
        "tipo_operacao": st.session_state["tipo_operacao"],
        "endereco": st.session_state["endereco"],
        "bairro": st.session_state["bairro"],
        "cidade": st.session_state["cidade"],
        "uf": st.session_state["uf"],
        "area_total": st.session_state["area_total"],
        "area_util": st.session_state["area_util"],
        "area_construida": st.session_state["area_construida"],
        "valor": st.session_state["valor_locacao"] if st.session_state["tipo_operacao"] == "Locação" else st.session_state["valor_venda"],
        "iptu": st.session_state["iptu"],
        "condominio": st.session_state["condominio"],
        "tipo_imovel": st.session_state["tipo_imovel"],
        "caracteristicas": ", ".join(st.session_state["caracteristicas_imovel"]),
        "nome_proprietario": st.session_state["nome_proprietario"],
        "telefone_proprietario": st.session_state["telefone_proprietario"],
        "email": st.session_state["email_proprietario"],
        "observacoes": st.session_state["observacoes"]
    }
    
    salvar_dados(novo_registro)
    reset_form()

# Exibindo os dados salvos
#st.subheader("Dados Salvos")
#st.dataframe(data)