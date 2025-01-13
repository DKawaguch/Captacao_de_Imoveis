CREATE TABLE imoveis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_operacao VARCHAR(50) NOT NULL,           -- Locação ou Venda
    endereco VARCHAR(255) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf VARCHAR(2) NOT NULL,                      -- Unidade Federativa
    area_total FLOAT DEFAULT 0.0,                -- Área Total em m²
    area_util FLOAT DEFAULT 0.0,                 -- Área Útil em m²
    area_construida FLOAT DEFAULT 0.0,           -- Área Construída em m²
    valor FLOAT DEFAULT 0.0,                     -- Valor (R$) - Locação ou Venda
    iptu FLOAT DEFAULT 0.0,                      -- Valor do IPTU (R$)
    condominio FLOAT DEFAULT 0.0,                -- Condomínio Mensal (R$)
    tipo_imovel VARCHAR(50) NOT NULL,            -- Tipo de Imóvel
    caracteristicas TEXT,                        -- Características do Imóvel (lista concatenada)
    nome_proprietario VARCHAR(100) NOT NULL,
    telefone_proprietario VARCHAR(20) NOT NULL,
    email_proprietario VARCHAR(100),
    observacoes TEXT                             -- Observações adicionais
);