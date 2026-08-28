
import streamlit as st

st.set_page_config(page_title="Calculadora de IMC", page_icon="⚖️")

st.title("⚖️ Calculadora de IMC")

peso = st.number_input("Digite seu peso (em kg):", min_value=0.0, format="%.2f")
altura = st.number_input("Digite sua altura (em metros ou cm):", min_value=0.0, format="%.2f")

if st.button("Calcular IMC"):
    # Se digitar a altura em centímetros (ex: 157), converte para metros (1.57)
    if altura > 3:
        altura = altura / 100

    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.subheader(f"Seu IMC é: **{imc:.2f}**")
        
        if imc < 18.5:
            st.warning("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 25:
            st.success("Classificação: Peso ideal (parabéns!)")
        elif 25 <= imc < 30:
            st.warning("Classificação: Levemente acima do peso")
        elif 30 <= imc < 35:
            st.error("Classificação: Obesidade Grau I")
        elif 35 <= imc < 40:
            st.error("Classificação: Obesidade Grau II (severa)")
        else:
            st.error("Classificação: Obesidade Grau III (mórbida)")
    else:
        st.error("Por favor, insira valores válidos.")
