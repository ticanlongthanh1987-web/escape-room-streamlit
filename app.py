import streamlit as st
import streamlit.components.v1 as components

GAME_URL = "https://euphonious-cupcake-48a34c.netlify.app"

st.set_page_config(page_title="Escape Room 3D", page_icon="🚪", layout="wide")

st.title("🚪 Escape Room 3D")
st.caption(
    "Game kinh dị giải đố thoát phòng. "
    "WASD: đi · Chuột: nhìn · E: tương tác · F: đèn pin · Esc: tạm dừng"
)
st.warning("Game có cảnh hù dọa đột ngột và âm thanh lớn. Hãy chỉnh âm lượng vừa phải trước khi chơi.")

st.link_button("Mở game ở tab mới (chơi mượt hơn)", GAME_URL)

components.html(
    f'<iframe src="{GAME_URL}" width="100%" height="720" '
    f'allow="fullscreen; autoplay" style="border:0"></iframe>',
    height=740,
)
