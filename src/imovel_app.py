import sys
import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QPushButton, 
    QComboBox, 
    QMessageBox, 
    QMainWindow
)

from Venda import Venda
from Locacao import Locacao

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
                quitado VARCHAR(20 ) DEFAULT 'Não se aplica',
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

class ImovelApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro do Imóvel")
        #self.initUI()

        # Layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tipo de Operação
        self.tipo_operacao_label = QLabel("Tipo de Operação:")
        self.tipo_operacao_combo = QComboBox()
        self.tipo_operacao_combo.addItems(["", "Locação", "Venda"])
        self.layout.addWidget(self.tipo_operacao_label)
        self.layout.addWidget(self.tipo_operacao_combo)

        # Placeholder para o formulário dinâmico
        self.form_placeholder = QWidget()
        self.form_layout = QVBoxLayout(self.form_placeholder)
        self.layout.addWidget(self.form_placeholder)

        # Botões
        self.salvar_button = QPushButton("Salvar")
        self.salvar_button.clicked.connect(self.save_data)
        self.layout.addWidget(self.salvar_button)

        #self.setLayout(layout)

        # Conectar a mudança no ComboBox
        self.tipo_operacao_combo.currentIndexChanged.connect(self.show_form)

        # Variável para armazenar o formulário atual
        self.current_form = None

    def show_form(self):
        # Remover o formulário atual, se houver
        if self.current_form:
            self.current_form.setParent(None)
            self.current_form = None

        # Determinar qual formulário exibir
        operation = self.tipo_operacao_combo.currentText()

        if operation == "Venda":
            self.current_form = Venda()
        elif operation == "Locação":
            self.current_form = Locacao()

        # Adicionar o novo formulário ao layout
        if self.current_form:
            self.form_layout.addWidget(self.current_form)

    def save_data(self):
        if self.current_form:
            try:
                data = self.current_form.collect_data()  # Método nos formulários que retorna os dados
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
                ''', tuple(data.values()))
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Error as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {e}")
                logging.error(f"Erro ao salvar dados: {e}")
            finally:
                if conn.is_connected():
                    conn.close()
        else:
            QMessageBox.warning(self, "Aviso", "Nenhum formulário foi selecionado.")

if __name__ == "__main__":
    initialize_database()
    app = QApplication(sys.argv)
    window = ImovelApp()
    window.show()
    sys.exit(app.exec_())