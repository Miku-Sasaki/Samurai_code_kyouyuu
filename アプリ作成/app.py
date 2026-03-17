import streamlit as st
import io
from PIL import Image, ImageEnhance

def main():
    st.set_page_config(page_title="画像彩度エンハンサー")
    st.title("画像を鮮やかにするアプリ")
    st.write("画像をアップロードして、彩度を調整し美しく仕上げましょう。")

    uploaded_file = st.file_uploader("画像ファイルを選択 (jpg, png)", type=['jpg', 'jpeg', 'png'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        
        # 調整用のスライダーを配置
        st.subheader("画像調整")
        saturation = st.slider("彩度", min_value=0.0, max_value=3.0, value=1.5, step=0.1)
        contrast = st.slider("コントラスト", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
        brightness = st.slider("明るさ", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
        
        # フィルターを順番に適用
        # 1. 彩度
        enhancer_sat = ImageEnhance.Color(image)
        img_sat = enhancer_sat.enhance(saturation)
        # 2. コントラスト
        enhancer_con = ImageEnhance.Contrast(img_sat)
        img_con = enhancer_con.enhance(contrast)
        # 3. 明るさ
        enhancer_bri = ImageEnhance.Brightness(img_con)
        enhanced_image = enhancer_bri.enhance(brightness)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("元画像")
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("編集後")
            st.image(enhanced_image, use_column_width=True)
            
            # 画像をバイト列に変換してダウンロードボタンを作成
            buf = io.BytesIO()
            enhanced_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="編集した画像をダウンロード",
                data=byte_im,
                file_name="enhanced_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()