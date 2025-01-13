# config/database_config.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ferreira@))1",
            database="imoveis_db"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        raise Exception(f"Erro ao conectar ao MySQL: {e}")

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS imoveis_db")
    cursor.execute("USE imoveis_db")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS imoveis (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tipo_operacao VARCHAR(50) NOT NULL,
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
    """)
    conn.commit()
    cursor.close()
    conn.close()
