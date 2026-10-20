import streamlit as st
import json
import os

# Ficheiro para guardar os dados
arquivo = 'minhas_horas.json'

def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(lista):
    with open(arquivo, 'w') as f:
        json.dump(lista, f)

# Carrega a lista de atividades
atividades = carregar_dados()

# Título da tua página Web
st.title("🏆 Volunteer Hours Tracker")

# 1. Secção para adicionar nova atividade usando um formulário
st.subheader("Add New Activity")
with st.form("form_nova_atividade"):
    nome = st.text_input("Organization / Location (e.g., Library, Food Bank)")
    data = st.text_input("Date (e.g., 10/16/2026)")
    horas = st.number_input("Hours Completed", min_value=0.0, step=0.5)
    
    # Botão de submeter o formulário
    submit = st.form_submit_button("Save Hours")
    
    if submit:
        if nome and data and horas > 0:
            atividades.append({"nome": nome, "data": data, "horas": horas})
            salvar_dados(atividades)
            st.success("✅ Activity saved successfully!")
            st.rerun() # Atualiza a página para mostrar os novos dados
        else:
            st.error("❌ Please fill out all fields correctly.")

# 2. Secção para mostrar o total de horas
total_horas = sum(item["horas"] for item in atividades)
st.metric(label="Total Hours Accumulated", value=f"{total_horas} hours")

# 3. Secção para listar e apagar atividades
st.subheader("Your Activities")

if not atividades:
    st.info("No activities logged yet.")
else:
    # Cria uma lista bonita em colunas
    for i, atv in enumerate(atividades):
        col1, col2, col3, col4 = st.columns([2, 3, 2, 2])
        
        col1.write(f"📅 **{atv['data']}**")
        col2.write(f"🏢 {atv['nome']}")
        col3.write(f"⏱️ {atv['horas']} hours")
        
        # Cria um botão de apagar para cada linha
        if col4.button("🗑️ Delete", key=f"apagar_{i}"):
            atividades.pop(i)
            salvar_dados(atividades)
            st.rerun()


