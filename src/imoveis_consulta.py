import streamlit as st
from mysql.connector import Error
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import data_connection

# Function to fetch filtered properties
def fetch_filtered_properties(filters):
    try:
        conn = data_connection.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM imoveis WHERE 1=1"
        params = []

        # Filtros principais
        if filters['operacao']:
            query += " AND operacao = %s"
            params.append(filters['operacao'])

        if filters['endereco']:
            query += " AND endereco LIKE %s"
            params.append(f"%{filters['endereco']}%")

        if filters['uf']:
            query += " AND uf = %s"
            params.append(filters['uf'])

        if filters['bairro']:
            query += " AND bairro LIKE %s"
            params.append(f"%{filters['bairro']}%")

        if filters['cidade']:
            query += " AND cidade LIKE %s"
            params.append(f"%{filters['cidade']}%")

        if filters['nome_condominio']:
            query += " AND nome_condominio LIKE %s"
            params.append(f"%{filters['nome_condominio']}%")

        if filters['area_total']:
            query += " AND area_total BETWEEN %s AND %s"
            params.extend(list(filters['area_total']))

        if filters['area_util']:
            query += " AND area_util BETWEEN %s AND %s"
            params.extend(list(filters['area_util']))

        if filters['area_construida']:
            query += " AND area_construida BETWEEN %s AND %s"
            params.extend(list(filters['area_construida']))

        if filters['quitado']:
            query += " AND quitado = %s"
            params.append(filters['quitado'])

        if filters['financiamento_qtd_parcelas']:
            query += " AND financiamento_qtd_parcelas = %s"
            params.append(filters['financiamento_qtd_parcelas'])

        if filters['financiamento_valor_parcela']:
            query += " AND financiamento_valor_parcela = %s"
            params.append(filters['financiamento_valor_parcela'])

        if filters['fiador']:
            query += " AND fiador = %s"
            params.append(filters['fiador'])

        if filters['seguro_fianca']:
            query += " AND seguro_fianca = %s"
            params.append(filters['seguro_fianca'])

        if filters['adiantamento_alugueis']:
            query += " AND adiantamento_alugueis = %s"
            params.append(filters['adiantamento_alugueis'])

        if filters['valor']:
            query += " AND valor BETWEEN %s AND %s"
            params.extend(list(filters['valor']))

        if filters['iptu'] and len(filters['iptu']) == 2:
            query += " AND iptu BETWEEN %s AND %s"
            params.extend(filters['iptu'])

        if filters['condominio'] and len(filters['condominio']) == 2:
            query += " AND condominio BETWEEN %s AND %s"
            params.extend(filters['condominio'])

        # Características do imóvel (valores numéricos)
        for feature in ['dormitorio', 'cozinha', 'lavabo', 'banheiros', 'area_servico', 'piscina',
                        'sauna', 'suites', 'despensa', 'sala_estar', 'lavanderia', 'hidromassagem',
                        'quintal', 'salao_festas', 'churrasqueira', 'closet', 'armarios', 'lareira',
                        'dep_empregada', 'aquecedor', 'playground', 'salao_jogos', 'garagem', 'sacada',
                        'copa', 'sala_jantar', 'wc_empregada', 'gas_encanado', 'quadra', 'academia']:
            if filters.get(feature) != 0:  # Considera valores numéricos, inclusive 0
                query += f" AND {feature} = %s"
                params.append(filters[feature])

        if filters['observacoes']:
            query += " AND observacoes LIKE %s"
            params.append(f"%{filters['observacoes']}%")

        # Executa a consulta
        #print("Query:", query)
        #print("Parameters:", params)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        st.error(f"Erro ao consultar o banco de dados: {e}")
        return []
    finally:
        if conn.is_connected():
            conn.close()

# Function to display property details
def display_property_details(property):
    st.subheader("Detalhes do Imóvel")

    # Localização
    st.markdown("### Localização")
    loc_cols = st.columns(3)
    with loc_cols[0]:
        st.text_input("Endereço", value=property.get('endereco', ''), disabled=True)
    with loc_cols[1]:
        st.text_input("Cidade", value=property.get('cidade', ''), disabled=True)
    with loc_cols[2]:
        st.text_input("UF", value=property.get('uf', ''), disabled=True)

    bairro = st.text_input("Bairro", value=property.get('bairro', ''), disabled=True)

    area_cols = st.columns(3)
    with area_cols[0]:
        st.text_input("Área Total (m²)", value=property.get('area_total', ''), disabled=True)
    with area_cols[1]:
        st.text_input("Área Útil (m²)", value=property.get('area_util', ''), disabled=True)
    with area_cols[2]:
        st.text_input("Área Construída (m²)", value=property.get('area_construida', ''), disabled=True)

    # Campos específicos para Locação ou Venda
    if property.get('operacao') == "Locação":
        locacao_cols = st.columns(3)
        with locacao_cols[0]:
            st.text_input("Fiador", value=property.get('fiador', ''), disabled=True)
        with locacao_cols[1]:
            st.text_input("Seguro Fiança", value=property.get('seguro_fianca', ''), disabled=True)
        with locacao_cols[2]:
            st.text_input("Adiantamento de Aluguéis", value=property.get('adiantamento_alugueis', ''), disabled=True)
    elif property.get('operacao') == "Venda":
        venda_cols = st.columns(3)
        with venda_cols[0]:
            st.text_input("Quitado", value=property.get('quitado', ''), disabled=True)
        with venda_cols[1]:
            st.text_input("Quantidade de Parcelas", value=property.get('financiamento_qtd_parcelas', ''), disabled=True)
        with venda_cols[2]:
            st.text_input("Valor da Parcela", value=property.get('financiamento_valor_parcela', ''), disabled=True)

    # Valores
    st.markdown("### Valores")
    valor_cols = st.columns(3)
    with valor_cols[0]:
        st.text_input("Valor", value=property.get('valor', ''), disabled=True)
    with valor_cols[1]:
        st.text_input("IPTU", value=property.get('iptu', ''), disabled=True)
    with valor_cols[2]:
        st.text_input("Condomínio", value=property.get('condominio', ''), disabled=True)

    # Tipo de Imóvel
    st.markdown("### Tipo de Imóvel")
    tipo_imovel = st.text_input("Tipo de Imóvel", value=property.get('tipo_imovel', ''), disabled=True)

    # Características do Imóvel
    st.markdown("### Características do Imóvel")
    caracteristicas = [
        'dormitorio', 'suites', 'closet', 'sacada', 'cozinha', 'despensa', 'armarios', 'copa', 'sala_estar',
        'lareira', 'sala_jantar', 'lavabo', 'lavanderia', 'dep_empregada', 'wc_empregada', 'banheiros',
        'hidromassagem', 'aquecedor', 'gas_encanado', 'area_servico', 'quintal', 'playground', 'quadra',
        'piscina', 'salao_festas', 'salao_jogos', 'academia', 'churrasqueira', 'garagem'
        ]

    # Organize characteristics into 4 columns
    cols = st.columns(4)
    for i, feature in enumerate(caracteristicas):
        with cols[i % 4]:
            # Display the numeric value of the feature
            st.text_input(
                label=feature.replace('_', ' ').title(),
                value=property.get(feature, 0),  # Default to 0 if the feature is not present
                disabled=True
            )
    # Dados do Proprietário
    st.markdown("### Dados do Proprietário")
    prop_cols = st.columns(3)
    with prop_cols[0]:
        st.text_input("Nome do Proprietário", value=property.get('nome_proprietario', ''), disabled=True)
    with prop_cols[1]:
        st.text_input("Endereço do Proprietário", value=property.get('endereco_proprietario', ''), disabled=True)
    with prop_cols[2]:
        st.text_input("Cidade do Proprietário", value=property.get('cidade_proprietario', ''), disabled=True)

    prop_cols2 = st.columns(3)
    with prop_cols2[0]:
        st.text_input("Bairro do Proprietário", value=property.get('bairro_proprietario', ''), disabled=True)
    with prop_cols2[1]:
        st.text_input("Telefone do Proprietário", value=property.get('telefone_proprietario', ''), disabled=True)
    with prop_cols2[2]:
        st.text_input("Celular do Proprietário", value=property.get('celular_proprietario', ''), disabled=True)

    # Observações
    st.markdown("### Observações")
    observacoes = st.text_area("Observações", value=property.get('observacoes', ''), disabled=True)