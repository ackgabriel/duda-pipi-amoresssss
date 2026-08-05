import streamlit as st
from PIL import Image
import os

# ── Configuração da página ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Duda & Pipi 🩷",
    page_icon="🩷",
    layout="wide",
)

# ── CSS Barbie Pink ───────────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Background degradê rosa Barbie */
  [data-testid="stAppViewContainer"] {
      background: linear-gradient(135deg, #ff80c0 0%, #ff1493 30%, #ff69b4 60%, #ffb6d9 100%);
      min-height: 100vh;
  }
  [data-testid="stHeader"] { background: transparent; }
  [data-testid="stSidebar"] { display: none; }

  /* Cartão branco translúcido */
  .card {
      background: rgba(255, 255, 255, 0.88);
      border-radius: 24px;
      padding: 2rem 2.5rem;
      margin: 1.2rem 0;
      box-shadow: 0 8px 32px rgba(255, 20, 147, 0.25);
      border: 2px solid rgba(255, 105, 180, 0.4);
  }

  /* Títulos */
  .titulo-principal {
      font-family: 'Georgia', serif;
      font-size: 3.4rem;
      font-weight: 900;
      color: #c2185b;
      text-align: center;
      text-shadow: 3px 3px 0px #ff80c0, 6px 6px 0px rgba(194,24,91,0.2);
      letter-spacing: 2px;
      margin-bottom: 0.3rem;
  }
  .subtitulo {
      font-size: 1.3rem;
      color: #ad1457;
      text-align: center;
      font-style: italic;
      margin-bottom: 0.5rem;
  }
  .secao-titulo {
      font-family: 'Georgia', serif;
      font-size: 1.9rem;
      font-weight: 700;
      color: #c2185b;
      text-align: center;
      margin-bottom: 1rem;
  }

  /* Mensagem */
  .mensagem {
      font-size: 1.12rem;
      color: #6d1a4a;
      line-height: 1.9;
      text-align: center;
  }

  /* Foto com hover */
  .foto-container img {
      border-radius: 20px;
      border: 4px solid #ff69b4;
      box-shadow: 0 6px 20px rgba(255, 20, 147, 0.35);
      transition: transform 0.3s ease;
      width: 100%;
  }
  .foto-container:hover img { transform: scale(1.03); }

  /* Caption rosa */
  [data-testid="stImage"] > div > div > p {
      color: #c2185b !important;
      font-style: italic;
      font-size: 0.92rem;
      text-align: center;
  }

  /* Coração pulsante */
  @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.15); }
  }
  .coracao { animation: pulse 1.5s infinite; display: inline-block; }

  /* Divisor rosa */
  .divisor {
      text-align: center;
      font-size: 1.6rem;
      margin: 0.5rem 0;
      color: #ff69b4;
      letter-spacing: 8px;
  }

  /* Rodapé */
  .rodape {
      text-align: center;
      color: #fff;
      font-size: 0.95rem;
      text-shadow: 1px 1px 4px rgba(194,24,91,0.5);
      padding: 1rem 0 0.5rem;
  }

  /* Balão de cápsula */
  .capsula {
      display: inline-block;
      background: linear-gradient(90deg, #ff1493, #ff69b4);
      color: white;
      border-radius: 50px;
      padding: 0.35rem 1.2rem;
      font-size: 1rem;
      font-weight: 600;
      margin: 0.3rem;
      box-shadow: 0 3px 10px rgba(255,20,147,0.4);
  }
</style>
""", unsafe_allow_html=True)

# ── CABEÇALHO ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="card">
  <div class="titulo-principal">🩷 Duda & Pipi 🐾</div>
  <div class="subtitulo">Uma homenagem à amizade mais fofa do mundo</div>
  <div class="divisor">🌸 ✨ 🌸 ✨ 🌸</div>
</div>
""", unsafe_allow_html=True)

# ── MENSAGEM CARINHOSA ────────────────────────────────────────────────────────
st.markdown("""
<div class="card">
  <div class="secao-titulo">💌 Para a Duda</div>
  <div class="mensagem">
    Você é daquelas pessoas que ilumina qualquer lugar por onde passa — com seu sorriso,
    sua energia e o seu coração enorme. 🌸<br><br>
    Ter você como amiga é um presente que a vida deu de presente.
    Cada momento ao seu lado (e da nossa Pipi 🐾) é uma memória que fica guardada
    com muito carinho.<br><br>
    Você é incrível, linda, forte e especial — e a Pipi com certeza concorda. 🩷<br><br>
    <strong>Com todo amor do mundo,</strong><br>
    <span class="coracao">💖</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── GALERIA ───────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="secao-titulo">📸 Galeria — Momentos Especiais</div>', unsafe_allow_html=True)

# Informações de cada foto
fotos_info = [
    ("fotos/foto1.jpg", "Duda & Pipi de Chapeuzinho 🧺"),
    ("fotos/foto2.jpg", "A dupla mais estilosa 🐄✨"),
    ("fotos/foto3.jpg", "Pipi na praia 🌊"),
    ("fotos/foto4.jpg", "Melhor abraço do mundo 🤗"),
    ("fotos/foto5.jpg", "Amor no verão 🌞"),
]

# Linha 1: 3 fotos
col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]
for i in range(3):
    path, caption = fotos_info[i]
    if os.path.exists(path):
        with colunas[i]:
            img = Image.open(path)
            st.image(img, caption=caption, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# Linha 2: 2 fotos centralizadas
_, col4, col5, _ = st.columns([0.5, 2, 2, 0.5])
for i, col in enumerate([col4, col5]):
    path, caption = fotos_info[3 + i]
    if os.path.exists(path):
        with col:
            img = Image.open(path)
            st.image(img, caption=caption, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── TAGS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="card" style="text-align:center;">
  <div class="secao-titulo">🏷️ Tudo que define a Duda & Pipi</div>
  <span class="capsula">🩷 Melhor amiga</span>
  <span class="capsula">🐾 Mãe da Pipi</span>
  <span class="capsula">✨ Incrível</span>
  <span class="capsula">🌸 Fofa demais</span>
  <span class="capsula">🌊 Praia</span>
  <span class="capsula">🐕 Pomerânia</span>
  <span class="capsula">💅 Estilosa</span>
  <span class="capsula">🎀 Barbie vibes</span>
  <span class="capsula">💖 Amizade</span>
  <span class="capsula">🌟 Especial</span>
</div>
""", unsafe_allow_html=True)

# ── RODAPÉ ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="rodape">
  Feito com muito 🩷 em homenagem à Duda e à Pipi<br>
  <small>🌸 ✨ 🌸 ✨ 🌸</small>
</div>
""", unsafe_allow_html=True)
