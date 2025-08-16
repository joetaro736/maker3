import streamlit as st

st.title('Ciberbullying')
st.image('imagem.png')
st.sidebar.header('Joe, Gustavo, Nicollas, Vinicius e Guilherme')

st.sidebar.title("""Ciberbullying
                 6°B""")
st.sidebar.image('download.png')

tab1, tab2 = st.tabs(['aonde acontece', 'como acontece'])
with tab1:
    st.subheader("""O cyberbullying acontece em ambientes virtuais como redes sociais, aplicativos de mensagem, plataformas de jogos e celulares. É um tipo de agressão que utiliza a internet para intimidar, assustar ou envergonhar.
""")
with tab2:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Fóruns Online', 'Criação de Perfil Falso', 'Redes Sociais', 'Jogos Online', 'E-mails'])
    with tab1:
        st.subheader("""Publicação de comentários maldosos ou difamatórios. """)
    with tab2:
        st.subheader("""Se passar por outra pessoa e enviar mensagens agressivas em seu nome.""")
    with tab3:
        st.subheader("""Publicação de mensagens, fotos ou vídeos humilhantes ou ofensivos. """)
    with tab4:
        st.subheader("""Intimidação, zoação ou assédio dentro dos jogos""")
    with tab5:
        st.subheader(""" Envio de mensagens ofensivas ou informações falsas. """)