import streamlit as st
import random

# 1. Cấu hình trang
st.set_page_config(page_title="Nhà Hàng Mèo Phép Thuật", page_icon="🍳", layout="centered")

# 2. CSS Tùy chỉnh để nâng cấp Đồ họa
st.markdown("""
<style>
    /* Gradient nền chính */
    .stApp {
        background: linear-gradient(135deg, #fff5eb 0%, #ffe3d1 100%);
    }
    
    /* Khung NPC & Món ăn */
    .npc-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center;
        border: 2px solid #ffd8be;
    }
    
    /* Bong bóng thoại NPC */
    .speech-bubble {
        background-color: #fff3e0;
        border-radius: 12px;
        padding: 12px 18px;
        font-weight: bold;
        color: #e65100;
        display: inline-block;
        margin-top: 10px;
        border: 1px dashed #ffb74d;
    }
</style>
""", unsafe_allow_html=True)

# 3. Dữ liệu NPC, Công thức & Hình ảnh
RECIPES = {
    "Bánh Mì Ốp La": ["Bánh mì", "Trứng"],
    "Bánh Mì Thịt": ["Bánh mì", "Thịt", "Rau"],
    "Cà Phê Sữa": ["Cà phê", "Sữa"],
    "Súp Nấm Phép Thuật": ["Nấm", "Sữa"]
}

NPCS = [
    {
        "name": "Mèo Thần Thoại",
        "avatar": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXp2ZnR4bmRzc292eXFud2x4OW8zeGNuOW14a3BxODR4c2VnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mCRJDo24UvJMA/giphy.gif",
        "dialogue": "Cho ta một món ăn nhẹ để nạp năng lượng làm phép!"
    },
    {
        "name": "Mèo Quý Bà",
        "avatar": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmN5ZXRwbWx1YnJzeHg0NDc5bzlyZWR4eG01azlhbW9vZjFvd3M4YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lq0h93752f6J9tijrh/giphy.gif",
        "dialogue": "Ta muốn một bữa sáng thanh lịch và thơm ngon!"
    },
    {
        "name": "Mèo Lười Nhủ",
        "avatar": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTN5d25zcWRzcXZnb3o5OXc1OW8zcTh4NGxwcTRkbmJmdzRtY3M3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif",
        "dialogue": "Nhanh lên nào, ta đang đói ngất đi được đây..."
    }
]

# 4. Quản lý Trạng thái Session
if "game_state" not in st.session_state:
    st.session_state.game_state = "MENU"  # MENU hoặc PLAYING
if "gold" not in st.session_state:
    st.session_state.gold = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_npc" not in st.session_state:
    st.session_state.current_npc = random.choice(NPCS)
if "current_recipe" not in st.session_state:
    st.session_state.current_recipe = random.choice(list(RECIPES.keys()))
if "selected_ingredients" not in st.session_state:
    st.session_state.selected_ingredients = []

# ==========================================
# MÀN HÌNH CHÍNH (MAIN MENU)
# ==========================================
if st.session_state.game_state == "MENU":
    st.title("🐱 Tiệm Bánh & Cà Phê Mèo Phép Thuật")
    st.subheader("Chào mừng bạn đến với nhà hàng dễ thương nhất thế giới!")
    
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXp2ZnR4bmRzc292eXFud2x4OW8zeGNuOW14a3BxODR4c2VnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mCRJDo24UvJMA/giphy.gif",
        use_container_width=True
    )
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎮 BẮT ĐẦU CHƠI", use_container_width=True, type="primary"):
            st.session_state.game_state = "PLAYING"
            st.rerun()
    with col2:
        with st.popover("📖 Hướng Dẫn Chơi"):
            st.write("""
            1. **Xem yêu cầu:** Quan sát NPC Mèo gọi món gì.
            2. **Chọn nguyên liệu:** Bấm chọn đủ nguyên liệu theo công thức.
            3. **Phục vụ:** Nấu đúng món để nhận tiền vàng!
            """)

# ==========================================
# MÀN HÌNH CHƠI GAME (GAMEPLAY)
# ==========================================
elif st.session_state.game_state == "PLAYING":
    # Thanh điều hướng trên cùng
    col_nav1, col_nav2 = st.columns([3, 1])
    with col_nav1:
        st.title("🍳 Bếp Trưởng Mèo")
    with col_nav2:
        if st.button("🏠 Màn chính"):
            st.session_state.game_state = "MENU"
            st.rerun()
            
    # Hiển thị Chỉ số
    c1, c2 = st.columns(2)
    c1.metric("💰 Tiền Vàng", f"{st.session_state.gold} G")
    c2.metric("⭐ Món đã hoàn thành", f"{st.session_state.score}")
    
    st.write("---")

    # KHU VỰC NPC GỌI MÓN (ĐỒ HỌA THẺ)
    npc = st.session_state.current_npc
    recipe = st.session_state.current_recipe
    
    st.markdown(f"""
    <div class="npc-card">
        <h3>🐱 {npc['name']} đang ghé thăm!</h3>
        <img src="{npc['avatar']}" width="180" style="border-radius:50%; margin: 10px 0;">
        <br>
        <div class="speech-bubble">
            💬 "{npc['dialogue']}" <br>
            👉 <b>Món gọi: <span style="color:#d84315;">{recipe}</span></b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    
    # KHU VỰC BÀN CHẾ BIẾN
    st.subheader("🛒 Chọn nguyên liệu cho món ăn:")
    
    all_ingredients = ["Bánh mì", "Trứng", "Thịt", "Rau", "Cà phê", "Sữa", "Nấm"]
    
    # Hiển thị nút nguyên liệu dạng lưới 4 cột
    cols = st.columns(4)
    for idx, ing in enumerate(all_ingredients):
        if cols[idx % 4].button(f"➕ {ing}", key=f"ing_{ing}"):
            st.session_state.selected_ingredients.append(ing)

    # Hiển thị các nguyên liệu đã chọn
    if st.session_state.selected_ingredients:
        st.info(f"🥣 **Dĩa của bạn hiện có:** {', '.join(st.session_state.selected_ingredients)}")
    else:
        st.caption("Dĩa nguyên liệu đang trống...")

    # Nút Hành động
    act_col1, act_col2 = st.columns(2)
    
    with act_col1:
        if st.button("🔥 Phục Vụ Món", type="primary", use_container_width=True):
            target_ingredients = RECIPES[st.session_state.current_recipe]
            
            # So sánh nguyên liệu (không quan trọng thứ tự)
            if sorted(st.session_state.selected_ingredients) == sorted(target_ingredients):
                st.session_state.gold += 50
                st.session_state.score += 1
                st.success(f"🎉 Rất chính xác! {npc['name']} rất thích món này!")
                
                # Đổi NPC và Món mới
                st.session_state.current_npc = random.choice(NPCS)
                st.session_state.current_recipe = random.choice(list(RECIPES.keys()))
                st.session_state.selected_ingredients = []
                st.rerun()
            else:
                st.error("❌ Món ăn sai công thức rồi! NPC giận dỗi rời đi.")
                st.session_state.current_npc = random.choice(NPCS)
                st.session_state.current_recipe = random.choice(list(RECIPES.keys()))
                st.session_state.selected_ingredients = []
                st.rerun()

    with act_col2:
        if st.button("🗑️ Đổ Làm Lại", use_container_width=True):
            st.session_state.selected_ingredients = []
            st.rerun()
