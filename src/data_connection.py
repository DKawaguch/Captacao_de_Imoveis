import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Variáveis de conexão ao banco de dados
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'ferreira@))1')
DB_NAME = os.getenv('DB_NAME', 'imoveis_db')

# Função para conectar ao banco de dados
def get_connection():
    try:
        #logging.info("Conectando ao banco de dados...")
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            #logging.info("Conexão estabelecida com sucesso.")
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
            operacao VARCHAR(50) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            uf VARCHAR(2) NOT NULL,
            bairro VARCHAR(100) NOT NULL,
            cidade VARCHAR(100) NOT NULL,
            nome_condominio VARCHAR(255),
            area_total FLOAT,
            area_util FLOAT,
            area_construida FLOAT,
            quitado VARCHAR(20),
            financiamento_qtd_parcelas INT,
            financiamento_valor_parcela FLOAT,
            fiador VARCHAR(255),
            seguro_fianca VARCHAR(255),
            adiantamento_alugueis INT,              
            valor FLOAT,
            iptu FLOAT,
            condominio FLOAT,
            tipo_imovel VARCHAR(50) NOT NULL,
            dormitorio INT,cozinha INT,lavabo INT,banheiros INT,area_servico INT,piscina INT,sauna INT,suites INT,
            despensa INT,sala_estar INT,lavanderia INT,hidromassagem INT,quintal INT,salao_festas INT,churrasqueira INT,
            closet INT,armarios INT,lareira INT,dep_empregada INT,aquecedor INT,playground INT,salao_jogos INT,
            garagem INT,sacada INT,copa INT,sala_jantar INT,wc_empregada INT,gas_encanado INT,quadra INT,academia INT,
            nome_proprietario VARCHAR(255),
            endereco_proprietario VARCHAR(255),
            bairro_proprietario VARCHAR(100),
            telefone_proprietario VARCHAR(50),
            cidade_proprietario VARCHAR(100),
            celular_proprietario VARCHAR(50),
            uf_proprietario VARCHAR(2),
            email_proprietario VARCHAR(100),
            observacoes TEXT
            );
        ''')
        conn.commit()
        #logging.info("Banco de dados inicializado com sucesso.")
    except Error as e:
        logging.error(f"Erro ao inicializar banco de dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()