import streamlit as st

# 1. Títulos de la interfaz web
st.title("📱 Calculador de Propinas")
st.write("Solo coloca el costo de la comida, el número de personas y el porcentaje de propina. ¡Nada de símbolos ni letras!")


precio = st.number_input("Ingrese el costo de la comida ($):", min_value=0.0, step=1.0)
cuanto_propina = st.number_input("Ingrese el porcentaje de propina (%):", min_value=0.0, step=1.0)
personas = st.number_input("Ingrese el número de personas que van a colaborar:", min_value=0, step=1)

# 3. Matemática del total
propina = precio * (cuanto_propina / 100)
total = precio + propina

# 4. Lógica de decisiones interactiva
if personas == 1:
    st.warning(f"Irga, pagando tú solo, estás luqueado: **${total:.2f}**")

elif personas > 1:
    # Mostramos la pregunta de dividir solo si hay más de una persona
    dividir = st.radio("¿Desea dividir la cuenta entre las personas en partes iguales?", ["Sí", "No"])
    
    if dividir == "Sí":
        total_por_persona = total / personas
        st.info(f"El total general a pagar es: **${total:.2f}**")
        st.success(f"Cada uno tiene que soltarse: **${total_por_persona:.2f}** lucas")
        
    elif dividir == "No":
        aporte_del_resto = st.number_input("Ingrese cuánto va a aportar el resto de las personas en total ($):", min_value=0.0, step=1.0)
        pago_usuario = total - aporte_del_resto
        
        st.info(f"El total general a pagar es: **${total:.2f}**")
        if pago_usuario >= 0:
            st.success(f"te toca bajarte con: **${pago_usuario:.2f}** lucas")
        else:
            st.error("¡tu eres cuco mano si ya entre todos estan pagando de mas ay vale .")

else:
    # Caso para cuando el usuario pone 0 personas
    st.error("Tú eres gafo, ¿cómo que 0 personas?")
