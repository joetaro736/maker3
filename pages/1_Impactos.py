import streamlit as st
st.sidebar.header('Joe, Gustavo, Nicollas, Vinicius e Guilherme')

st.sidebar.title("""Ciberbullying
                 6°B""")
st.sidebar.image('download.png')
st.title('Impactos do Ciberbullying')

tab1, tab2, tab3, tab4 = st.tabs(['Saúde mental', 'Comportamento', 'Relações', 'Saúde física'])

with tab1:
    st.subheader('Depressão, ansiedade, baixa autoestima, isolamento social, problemas de sono.')
with tab2:
    st.subheader('Mudanças de humor, irritabilidade, retraimento, perda de interesse em atividades')
with tab3:
    st.subheader('Dificuldade em construir e manter relacionamentos, medo de interagir com outras pessoas.')
with tab4:
    st.subheader('Problemas como dores de cabeça, dores no estômago, fadiga. ')

with st.container():
    st.title('Como Combater o Cyberbullying')
    tab1, tab2, tab3, tab4 = st.tabs(['Educação', 'Prevenção', 'Denúncia', 'Legislação'])
    with tab1:
        st.subheader('Aumentar a conscientização sobre o problema, tanto em escolas como em casa.')
    with tab2:
        st.subheader('Estabelecer regras de uso seguro das tecnologias, ensinar a reconhecer os sinais de cyberbullying e a buscar ajuda. ')
    with tab3:
        st.subheader('Informar as plataformas online sobre o cyberbullying, buscar apoio de familiares, amigos e profissionais de saúde. ')
    with tab4:
        st.subheader('A lei que inclui o cyberbullying no Código Penal é um passo importante para o combate ao problema, mas é fundamental que haja um trabalho conjunto de todos para garantir que as vítimas sejam protegidas.')
        