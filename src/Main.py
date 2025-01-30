import streamlit as st
#from mysql.connector import Error
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src import data_connection
from src import imoveis_cadastro, imoveis_consulta

# Load environment variables
load_dotenv()

# Inicializar o banco de dados
data_connection.initialize_database()

# Initialize session state
if 'selected_property' not in st.session_state:
    st.session_state['selected_property'] = None

# Streamlit app
def main():
    st.title("Gerenciamento de Imóveis")

    menu = ["Cadastro", "Consulta"]
    choice = st.sidebar.selectbox("Escolha a opção", menu)

    if choice == "Cadastro":
        #st.header("Cadastro de Imóvel")
        # Form fields for property registration

        operacao = st.selectbox("Escolha a operação", ["", "Venda", "Locação"])

        with st.form("cadastro_form"):
            
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

            submit_button = st.form_submit_button("Salvar")

            if submit_button:

                data = {
                    'operacao': operacao,
                    'endereco': endereco,
                    'uf': uf,
                    'bairro': bairro,
                    'cidade': cidade,
                    'nome_condominio': nome_condominio,
                    'area_total': area_total,
                    'area_util': area_util,
                    'area_construida': area_construida,
                    'quitado': quitado if operacao == 'Venda' else 'Não se aplica',
                    'financiamento_qtd_parcelas': financiamento_qtd_parcelas if operacao == 'Venda' else 0,
                    'financiamento_valor_parcela': financiamento_valor_parcela if operacao == 'Venda' else 0.0,
                    'fiador': fiador if operacao == 'Locação' else 'Não se aplica',
                    'seguro_fianca': seguro_fianca if operacao == 'Locação' else 'Não se aplica',
                    'adiantamento_alugueis': adiantamento_alugueis if operacao == 'Locação' else 0,
                    'valor': valor,
                    'iptu': iptu,
                    'condominio': condominio,
                    'tipo_imovel': tipo_imovel,
                    'dormitorio': dormitorio,'cozinha': cozinha,'lavabo': lavabo,'banheiros': banheiros,'area_servico': area_servico,'piscina': piscina,'sauna': sauna,'suites': suites,
                    'despensa': despensa,'sala_estar': sala_estar,'lavanderia': lavanderia,'hidromassagem': hidromassagem,'quintal': quintal,'salao_festas': salao_festas,'churrasqueira': churrasqueira,
                    'closet': closet,'armarios': armarios,'lareira': lareira,'dep_empregada': dep_empregada,'aquecedor': aquecedor,'playground': playground,'salao_jogos': salao_jogos,
                    'garagem': garagem,'sacada': sacada,'copa': copa,'sala_jantar': sala_jantar,'wc_empregada': wc_empregada,'gas_encanado': gas_encanado,'quadra': quadra,'academia': academia,
                    'nome_proprietario': nome_proprietario,
                    'endereco_proprietario': endereco_proprietario,
                    'bairro_proprietario': bairro_proprietario,
                    'telefone_proprietario': telefone_proprietario,
                    'cidade_proprietario': cidade_proprietario,
                    'celular_proprietario': celular_proprietario,
                    'uf_proprietario': uf_proprietario,
                    'email_proprietario': email_proprietario,
                    'observacoes': observacoes
                    }

                imoveis_cadastro.save_data(data)

    elif choice == "Consulta":
        st.header("Consulta de Imóveis")

        con_operacao = st.selectbox("Escolha a operação", ["Venda", "Locação"])

        with st.form("consulta_form"):

            # Localização
            st.subheader("Localização")
            loc_cols = st.columns(2)

            with loc_cols[0]:
                con_endereco = st.text_input("Endereço")
                con_uf = st.selectbox("UF do Imóvel", ["", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
            with loc_cols[1]:
                con_bairro = st.text_input("Bairro")
                con_cidade = st.text_input("Cidade")
    
            con_nome_condominio = st.text_input("Nome do Condomínio")
    
            # Áreas
            area_cols = st.columns(3)

            with area_cols[0]:
                con_area_total = st.slider("Área Total", min_value=0.0, max_value=100000.0, value=(0.0, 100000.0), step=1.0)
            with area_cols[1]:
                con_area_util = st.slider("Área Útil", min_value=0.0, max_value=100000.0, value=(0.0, 100000.0), step=1.0)
            with area_cols[2]:
                con_area_construida = st.slider("Área Construída", min_value=0.0, max_value=100000.0, value=(0.0, 100000.0), step=1.0)

            # Campos específicos
            if con_operacao == "Venda":
                venda_cols = st.columns(3)

                with venda_cols[0]:
                    con_quitado = st.selectbox("Quitado", ["Sim", "Não"])
                with venda_cols[1]:
                    con_financiamento_qtd_parcelas = st.number_input("Quantidade de Parcelas", min_value=0, step=1)
                with venda_cols[2]:
                    con_financiamento_valor_parcela = st.number_input("Valor da Parcela", min_value=0.0, step=0.01)

            else:
                locacao_cols = st.columns(3)

                with locacao_cols[0]:
                    con_fiador = st.text_input("Fiador")
                with locacao_cols[1]:
                    con_seguro_fianca = st.text_input("Seguro Fiança")
                with locacao_cols[2]:
                    con_adiantamento_alugueis = st.number_input("Adiantamento de Aluguéis", min_value=0, step=1)

            # Valores
            valor_cols = st.columns(3)

            with valor_cols[0]:
                con_valor = st.slider("Valor", min_value=0.0, max_value=10000000.0, value=(0.0, 10000000.0), step=1.0)
            with valor_cols[1]:
                con_iptu = st.slider("IPTU", min_value=0.0, max_value=10000000.0, value=(0.0, 10000000.0), step=1.0)
            with valor_cols[2]:
                con_condominio = st.slider("Condomínio", min_value=0.0, max_value=10000000.0, value=(0.0, 10000000.0), step=1.0)

            # Imóvel
            st.subheader("Características")
            con_tipo_imovel = st.selectbox("Tipo de Imóvel", ["", "Casa", "Apartamento", "Sobrado", "Cobertura", "Chácara", "Sítio", "Fazenda", "Terreno", "Galpão", "Loja", "Sala", "Prédio", "Outro"])

            cat_cols = st.columns(4)

            with cat_cols[0]:
                con_dormitorio = st.number_input("Dormitórios", min_value=0, step=1)
                con_cozinha = st.number_input("Cozinhas", min_value=0, step=1)
                con_lavabo = st.number_input("Lavabos", min_value=0, step=1)
                con_banheiros = st.number_input("Banheiros", min_value=0, step=1)
                con_area_servico = st.number_input("Área de Serviço", min_value=0, step=1)
                con_piscina = st.number_input("Piscina", min_value=0, step=1)
                con_sauna = st.number_input("Sauna", min_value=0, step=1)
                con_suites = st.number_input("Suítes", min_value=0, step=1)
            with cat_cols[1]:
                con_despensa = st.number_input("Despensa", min_value=0, step=1)
                con_sala_estar = st.number_input("Sala de Estar", min_value=0, step=1)
                con_lavanderia = st.number_input("Lavanderia", min_value=0, step=1)
                con_hidromassagem = st.number_input("Hidromassagem", min_value=0, step=1)
                con_quintal = st.number_input("Quintal", min_value=0, step=1)
                con_salao_festas = st.number_input("Salão de Festas", min_value=0, step=1)
                con_churrasqueira = st.number_input("Churrasqueira", min_value=0, step=1)

            with cat_cols[2]:
                con_closet = st.number_input("Closet", min_value=0, step=1)
                con_armarios = st.number_input("Armários", min_value=0, step=1)
                con_lareira = st.number_input("Lareira", min_value=0, step=1)
                con_dep_empregada = st.number_input("Dep. de Empregada", min_value=0, step=1)
                con_aquecedor = st.number_input("Aquecedor", min_value=0, step=1)
                con_playground = st.number_input("Playground", min_value=0, step=1)
                con_salao_jogos = st.number_input("Salão de Jogos", min_value=0, step=1)

            with cat_cols[3]:
                con_garagem = st.number_input("Garagens", min_value=0, step=1)
                con_sacada = st.number_input("Sacada", min_value=0, step=1)
                con_copa = st.number_input("Copa", min_value=0, step=1)
                con_sala_jantar = st.number_input("Sala de Jantar", min_value=0, step=1)
                con_wc_empregada = st.number_input("WC Empregada", min_value=0, step=1)
                con_gas_encanado = st.number_input("Gás Encanado", min_value=0, step=1)
                con_quadra = st.number_input("Quadra", min_value=0, step=1)
                con_academia = st.number_input("Academia", min_value=0, step=1)

            # Observações
            st.subheader("Observações")
            con_observacoes = st.text_area("Observações")

            filter_button = st.form_submit_button("Filtrar")

            if filter_button:
                filters = {
                    'operacao': con_operacao,
                    'endereco': con_endereco,
                    'uf': con_uf,
                    'bairro': con_bairro,
                    'cidade': con_cidade,
                    'nome_condominio': con_nome_condominio,
                    'area_total': con_area_total,
                    'area_util': con_area_util,
                    'area_construida': con_area_construida,
                    'quitado': con_quitado if con_operacao == 'Venda' else 'Não se aplica',
                    'financiamento_qtd_parcelas': con_financiamento_qtd_parcelas if con_operacao == 'Venda' else 0,
                    'financiamento_valor_parcela': con_financiamento_valor_parcela if con_operacao == 'Venda' else 0.0,
                    'fiador': con_fiador if con_operacao == 'Locação' else 'Não se aplica',
                    'seguro_fianca': con_seguro_fianca if con_operacao == 'Locação' else 'Não se aplica',
                    'adiantamento_alugueis': con_adiantamento_alugueis if con_operacao == 'Locação' else 0,
                    'valor': con_valor,
                    'iptu': con_iptu,
                    'condominio': con_condominio,
                    'tipo_imovel': con_tipo_imovel,
                    'dormitorio': con_dormitorio,'cozinha': con_cozinha,'lavabo': con_lavabo,'banheiros': con_banheiros,'area_servico': con_area_servico,'piscina': con_piscina,'sauna': con_sauna,'suites': con_suites,
                    'despensa': con_despensa,'sala_estar': con_sala_estar,'lavanderia': con_lavanderia,'hidromassagem': con_hidromassagem,'quintal': con_quintal,'salao_festas': con_salao_festas,'churrasqueira': con_churrasqueira,
                    'closet': con_closet,'armarios': con_armarios,'lareira': con_lareira,'dep_empregada': con_dep_empregada,'aquecedor': con_aquecedor,'playground': con_playground,'salao_jogos': con_salao_jogos,
                    'garagem': con_garagem,'sacada': con_sacada,'copa': con_copa,'sala_jantar': con_sala_jantar,'wc_empregada': con_wc_empregada,'gas_encanado': con_gas_encanado,'quadra': con_quadra,'academia': con_academia,
                    #'nome_proprietario': nome_proprietario,
                    #'endereco_proprietario': endereco_proprietario,
                    #'bairro_proprietario': bairro_proprietario,
                    #'telefone_proprietario': telefone_proprietario,
                    #'cidade_proprietario': cidade_proprietario,
                    #'celular_proprietario': celular_proprietario,
                    #'uf_proprietario': uf_proprietario,
                    #'email_proprietario': email_proprietario,
                    'observacoes': con_observacoes
                    }

                properties = imoveis_consulta.fetch_filtered_properties(filters)

                if properties:
                    for property in properties:
                        if st.button(f"Ver detalhes - {property['endereco']}"):
                            st.session_state["selected_property"] = property
                else:
                    st.info("Nenhum imóvel encontrado com os filtros selecionados.")

        if st.session_state['selected_property']:
            imoveis_consulta.display_property_details(st.session_state['selected_property'])
if __name__ == "__main__":
    main()
