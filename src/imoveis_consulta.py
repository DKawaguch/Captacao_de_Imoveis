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
            query += " AND tipo_operacao = %s"
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
            params.extend(filters['area_total'])

        if filters['area_util']:
            query += " AND area_util BETWEEN %s AND %s"
            params.extend(filters['area_util'])

        if filters['area_construida']:
            query += " AND area_construida BETWEEN %s AND %s"
            params.extend(filters['area_construida'])

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
            params.extend(filters['valor'])

        if filters['iptu']:
            query += " AND iptu = BETWEEN %s AND %s"
            params.append(filters['iptu'])

        if filters['condominio']:
            query += " AND condominio = BETWEEN %s AND %s"
            params.append(filters['condominio'])

        # Características do imóvel (valores numéricos)
        for feature in ['dormitorio', 'cozinha', 'lavabo', 'banheiros', 'area_servico', 'piscina',
                        'sauna', 'suites', 'despensa', 'sala_estar', 'lavanderia', 'hidromassagem',
                        'quintal', 'salao_festas', 'churrasqueira', 'closet', 'armarios', 'lareira',
                        'dep_empregada', 'aquecedor', 'playground', 'salao_jogos', 'garagem', 'sacada',
                        'copa', 'sala_jantar', 'wc_empregada', 'gas_encanado', 'quadra', 'academia']:
            if filters.get(feature) is not None:  # Considera valores numéricos, inclusive 0
                query += f" AND {feature} = %s"
                params.append(filters[feature])

        if filters['observacoes']:
            query += " AND observacoes LIKE %s"
            params.append(f"%{filters['observacoes']}%")

        # Executa a consulta
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
    for key, value in property.items():
        st.text(f"{key}: {value}")