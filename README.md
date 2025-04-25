# 🏥 Sistema de Cadastro Básico de Pacientes Utilizando Tkinter
## 📋 Visão Geral
Interface gráfica simples para cadastro de informações básicas de pacientes, desenvolvida com Python e Tkinter.

## ✨ Funcionalidades

✔️ **Formulário de cadastro** com campos para:
- Dados pessoais (Nome, RG, CPF, CNS)
- Informações de contato
- Unidade de saúde vinculada

✔️ **Histórico de saúde** com registro de:
- Diabetes (sim/não)
- Hipertensão (sim/não)
- Outros problemas de saúde (campo livre)

✔️ **Visualização imediata** dos dados cadastrados em pop-up

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Biblioteca Tkinter (interface gráfica)
- Sistema de arquivos local para assets

## ⚙️ Como Funciona

1. **Preenchimento do formulário**:
   - Todos os campos são do tipo Text ou Entry
   - Dados são capturados ao clicar no botão "Salvar"

2. **Processamento dos dados**:
   - A função `obter_dados()` coleta todas as informações
   - Organiza em um dicionário Python
   - Formata para exibição amigável

3. **Exibição dos resultados**:
   - Mostra os dados em uma messagebox do Tkinter
   - Apresenta em formato chave-valor

## 🔍 Detalhes Técnicos

- **Interface**:
  - Layout com sidebar azul
  - Campos posicionados precisamente com coordenadas
  - Design limpo e funcional
    🖼️ Screenshots do Sistema
<div align="center"> <h3>📌 Tela de Cadastro</h3> <img src="area-cadastro-vazio.png" alt="Tela principal do sistema" width="600"> <h3>📝 Formulário Preenchido</h3> <img src="area-cadastro-completo.png" alt="Formulário preenchido com dados" width="600"> <h3>✅ Pop-up com os Dados do Paciente</h3> <img src="resultado.png" alt="Pop-up mostrando dados cadastrados" width="400"> </div>
