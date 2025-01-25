import logging
from mysql.connector import Error
import streamlit as st

from . import data_connection

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Formulário de entrada de dados
def cadastro_imovel(operacao):
    st.header(f"Cadastro de {operacao}")

    # Localização
    st.subheader("Localização")
    loc_cols = st.columns(2)

    with loc_cols[0]:
        endereco = st.text_input("Endereço")
        uf = st.selectbox("UF do Imóvel", ["", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
    with loc_cols[1]:
        bairro = st.text_input("Bairro")
        cidade = st.text_input("Cidade")
    
    nome_condominio = st.text_input("Nome do Condomínio")
    
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
    tipo_imovel = st.selectbox("Tipo de Imóvel", ["", "Casa", "Apartamento", "Sobrado", "Cobertura", "Chácara", "Sítio", "Fazenda", "Terreno", "Galpão", "Loja", "Sala", "Prédio", "Outro"])

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
        uf_proprietario = st.selectbox("UF do Proprietário", ["", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
        email_proprietario = st.text_input("Email do Proprietário")

    # Observações
    st.subheader("Observações")
    observacoes = st.text_area("Observações")
    
# Botão para salvar os dados
def save_data(data):
    try:
        conn = data_connection.get_connection()
        cursor = conn.cursor()
        
        # Construção dinâmica do SQL
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO imoveis ({columns}) VALUES ({placeholders})"
        
        # Debugging: Exibir colunas e valores
        #print("SQL gerado:", sql)
        #print("Valores fornecidos:", tuple(data.values()))
        
        # Executar o SQL
        cursor.execute(sql, tuple(data.values()))
        conn.commit()
        st.success("Dados salvos com sucesso!")
    except Error as e:
        st.error(f"Erro ao salvar dados: {e}")
        logging.error(f"Erro ao salvar dados: {e}")
    finally:
        if conn.is_connected():
            conn.close()