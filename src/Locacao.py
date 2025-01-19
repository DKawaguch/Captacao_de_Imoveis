from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, 
    QComboBox, QPlainTextEdit, QSpinBox, QCheckBox, QGridLayout
)

class Locacao(QWidget):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Locação")
        layout = QVBoxLayout(self)

        # Campos Exclusivos de Locação
        
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
            "Edicula": QCheckBox("Edicula")
        }

        row = 0
        for i, (key, checkbox) in enumerate(self.caracteristicas_checkboxes.items()):
            self.caracteristicas_layout.addWidget(checkbox, row, i % 7)
            if i % 7 == 1:
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

    def collect_data(self):
        return{

            "tipo_operacao": "Locação",
            "fiador": self.com_fiador_combo.currentText(),
            "seguro_fianca": self.seguro_fianca_combo.currentText(),
            "adiantamento_alugueis": self.adiantamento_alugueis_input.value(),
            "quitado": "Não",
            "financiamento_qtd_parcelas": 0,
            "financiamento_valor_parcela": 0.0,
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