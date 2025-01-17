import sys
import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, 
    QComboBox, QPlainTextEdit, QSpinBox, QMessageBox, QCheckBox, QGridLayout
)

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

class ImovelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Imóveis")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Tipo de Operação
        self.tipo_operacao_label = QLabel("Tipo de Operação:")
        self.tipo_operacao_combo = QComboBox()
        self.tipo_operacao_combo.addItems(["", "Locação", "Venda"])
        layout.addWidget(self.tipo_operacao_label)
        layout.addWidget(self.tipo_operacao_combo)

        # Separando diferenças entre locação e venda
        if self.tipo_operacao_combo.currentText() == "Locação":
            self.com_fiador_label = QLabel("Com Fiador:")
            self.com_fiador_combo = QComboBox()
            self.com_fiador_combo.addItems(["", "Sim", "Não"])
            layout.addWidget(self.com_fiador_label)
            layout.addWidget(self.com_fiador_combo)

            self.seguro_fianca_label = QLabel("Seguro Fiança:")
            self.seguro_fianca_combo = QComboBox()
            self.seguro_fianca_combo.addItems(["", "Sim", "Não"])
            layout.addWidget(self.seguro_fianca_label)
            layout.addWidget(self.seguro_fianca_combo)

            self.adiantamento_alugueis_label = QLabel("Adiantamento de Quantos Aluguéis:")
            self.adiantamento_alugueis_input = QSpinBox()
            self.adiantamento_alugueis_input.setRange(0, 12)
            layout.addWidget(self.adiantamento_alugueis_label)
            layout.addWidget(self.adiantamento_alugueis_input)

        elif self.tipo_operacao_combo.currentText() == "Venda":
            self.quitado_label = QLabel("Quitado:")
            self.quitado_combo = QComboBox()
            self.quitado_combo.addItems(["", "Sim", "Não"])
            layout.addWidget(self.quitado_label)
            layout.addWidget(self.quitado_combo)

            self.financiado_label = QLabel("Financiado em Quantas Vezes:")
            self.financiado_input = QSpinBox()
            self.financiado_input.setRange(0, 60)
            layout.addWidget(self.financiado_label)
            layout.addWidget(self.financiado_input)

            self.parcela_label = QLabel("Parcelas de:")
            self.parcela_input = QSpinBox()
            self.parcela_input.setRange(0, 1000000)
            layout.addWidget(self.parcela_label)
            layout.addWidget(self.parcela_input)

        # Endereço e localização
        self.endereco_label = QLabel("Endereço:")
        self.endereco_input = QLineEdit()
        layout.addWidget(self.endereco_label)
        layout.addWidget(self.endereco_input)

        self.bairro_label = QLabel("Bairro:")
        self.bairro_input = QLineEdit()
        layout.addWidget(self.bairro_label)
        layout.addWidget(self.bairro_input)

        self.cidade_label = QLabel("Cidade:")
        self.cidade_input = QLineEdit()
        layout.addWidget(self.cidade_label)
        layout.addWidget(self.cidade_input)

        self.uf_label = QLabel("UF:")
        self.uf_combo = QComboBox()
        self.uf_combo.addItems(["", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
        layout.addWidget(self.uf_label)
        layout.addWidget(self.uf_combo)

        # Áreas
        self.area_total_label = QLabel("Área Total (m²):")
        self.area_total_input = QSpinBox()
        self.area_total_input.setRange(0, 100000)
        layout.addWidget(self.area_total_label)
        layout.addWidget(self.area_total_input)

        self.area_util_label = QLabel("Área Útil (m²):")
        self.area_util_input = QSpinBox()
        self.area_util_input.setRange(0, 100000)
        layout.addWidget(self.area_util_label)
        layout.addWidget(self.area_util_input)

        self.area_construida_label = QLabel("Área Construída (m²):")
        self.area_construida_input = QSpinBox()
        self.area_construida_input.setRange(0, 100000)
        layout.addWidget(self.area_construida_label)
        layout.addWidget(self.area_construida_input)

        # Valor e Proprietário
        self.valor_label = QLabel("Valor (R$):")
        self.valor_input = QSpinBox()
        self.valor_input.setRange(0, 100000000)
        layout.addWidget(self.valor_label)
        layout.addWidget(self.valor_input)

        self.iptu_label = QLabel("IPTU (R$):")
        self.iptu_input = QSpinBox()
        self.iptu_input.setRange(0, 1000000)
        layout.addWidget(self.iptu_label)
        layout.addWidget(self.iptu_input)

        self.condominio_label = QLabel("Condomínio (R$):")
        self.condominio_input = QSpinBox()
        self.condominio_input.setRange(0, 1000000)
        layout.addWidget(self.condominio_label)
        layout.addWidget(self.condominio_input)

        # Tipo de Imóvel
        self.tipo_imovel_label = QLabel("Tipo de Imóvel:")
        self.tipo_imovel_combo = QComboBox()
        self.tipo_imovel_combo.addItems(["", "Casa Térrea", "Sobrado", "Apartamento", "Terreno", "Sítio",
        "Chácara", "Galpão", "Assobradado", "Fazenda", "Indústria"])
        layout.addWidget(self.tipo_imovel_label)
        layout.addWidget(self.tipo_imovel_combo)

        # Características
        self.caracteristicas_label = QLabel("Características:")
        self.caracteristicas_layout = QGridLayout()
        self.caracteristicas_checkboxes = {
            "Dormitórios": QCheckBox("Dormitórios"),
            "Suítes": QCheckBox("Suítes"),
            "Closet": QCheckBox("Closet"),
            "Sacada": QCheckBox("Sacada"),
            "Cozihna": QCheckBox("Cozinha"),
            "Despensa": QCheckBox("Despensa"),
            "Armários": QCheckBox("Armários"),
            "Copa": QCheckBox("Copa"),
            "Sala de Almoço": QCheckBox("Sala de Almoço"),
            "Sala": QCheckBox("Sala"),
            "Lareira": QCheckBox("Lareira"),
            "Sala de Jantar": QCheckBox("Sala de Jantar"),
            "Lavabo": QCheckBox("Lavabo"),
            "Lavanderia": QCheckBox("Lavanderia"),
            "Dependência de Empregada": QCheckBox("Dependência de Empregada"),
            "W.C. de Empregada": QCheckBox("W.C. de Empregada"),
            "Banheiros": QCheckBox("Banheiros"),
            "Hidromassagem": QCheckBox("Hidromassagem"),
            "Aquecedor": QCheckBox("Aquecedor"),
            "Gás Encanado": QCheckBox("Gás Encanado"),
            "Área de Serviço": QCheckBox("Área de Serviço"),
            "Quintal": QCheckBox("Quintal"),
            "Playground": QCheckBox("Playground"),
            "Quadra Poliesportiva": QCheckBox("Quadra Poliesportiva"),
            "Piscina": QCheckBox("Piscina"),
            "Salão de Festas": QCheckBox("Salão de Festas"),	
            "Salão de Jogos": QCheckBox("Salão de Jogos"),
            "Sala de Ginástica": QCheckBox("Sala de Ginástica"),
            "Sauna": QCheckBox("Sauna"),
            "Churrasqueira": QCheckBox("Churrasqueira"),
            "Garagem": QCheckBox("Garagem"),
            "Edicula": QCheckBox("Edicula"),
            "Placa Solar": QCheckBox("Placa Solar"),
            "Chaves": QCheckBox("Chaves"),
        }

        row = 0
        for i, (key, checkbox) in enumerate(self.caracteristicas_checkboxes.items()):
            self.caracteristicas_layout.addWidget(checkbox, row, i % 4)
            if i % 4 == 1:
                row += 1

        layout.addWidget(self.caracteristicas_label)
        layout.addLayout(self.caracteristicas_layout)

        self.nome_proprietario_label = QLabel("Nome do Proprietário:")
        self.nome_proprietario_input = QLineEdit()
        layout.addWidget(self.nome_proprietario_label)
        layout.addWidget(self.nome_proprietario_input)

        self.telefone_proprietario_label = QLabel("Telefone do Proprietário:")
        self.telefone_proprietario_input = QLineEdit()
        layout.addWidget(self.telefone_proprietario_label)
        layout.addWidget(self.telefone_proprietario_input)

        self.email_proprietario_label = QLabel("E-mail do Proprietário:")
        self.email_proprietario_input = QLineEdit()
        layout.addWidget(self.email_proprietario_label)
        layout.addWidget(self.email_proprietario_input)

        # Observações
        self.observacoes_label = QLabel("Observações:")
        self.observacoes_input = QPlainTextEdit()
        layout.addWidget(self.observacoes_label)
        layout.addWidget(self.observacoes_input)

        # Botões
        self.salvar_button = QPushButton("Salvar")
        self.salvar_button.clicked.connect(self.save_data)
        layout.addWidget(self.salvar_button)

        self.setLayout(layout)

    def save_data(self):
        data = {
            "tipo_operacao": self.tipo_operacao_combo.currentText(),
            "endereco": self.endereco_input.text(),
            "bairro": self.bairro_input.text(),
            "cidade": self.cidade_input.text(),
            "uf": self.uf_combo.currentText(),
            "area_total": self.area_total_input.value(),
            "area_util": self.area_util_input.value(),
            "area_construida": self.area_construida_input.value(),
            "valor": self.valor_input.value(),
            "iptu": self.iptu_input.value(),
            "condominio": self.condominio_input.value(),
            "tipo_imovel": self.tipo_imovel_combo.currentText(),
            "caracteristicas": ", ".join([key for key, checkbox in self.caracteristicas_checkboxes.items() if checkbox.isChecked()]),
            "nome_proprietario": self.nome_proprietario_input.text(),
            "telefone_proprietario": self.telefone_proprietario_input.text(),
            "email": self.email_proprietario_input.text(),
            "observacoes": self.observacoes_input.toPlainText()
        }

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO imoveis (
            tipo_operacao, 
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
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', tuple(data.values()))
            conn.commit()
            QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
        except Error as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar dados: {e}")
            logging.error(f"Erro ao salvar dados: {e}")
        finally:
            if conn.is_connected():
                conn.close()

if __name__ == "__main__":
    initialize_database()
    app = QApplication(sys.argv)
    window = ImovelApp()
    window.show()
    sys.exit(app.exec_())