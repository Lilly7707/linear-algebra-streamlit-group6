import streamlit as st
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

# App title
st.title("Linear Algebra Group 6")

# Navigation section
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select a page:", ["Home", "Group Members", "Image Transformations"])

# Home page
if menu == "Home":
    st.header("Welcome to Group 6's Project on Image Processing!")
    st.write(
        "This Streamlit app showcases the contributions of Group 6 in the subject of Image Processing. "
        "Navigate through the pages to learn more about us, view examples, and explore the concepts we worked on."
    )

# Group Members page
elif menu == "Group Members":
    st.header("Anggota Group 6")
    st.write("Here are the members of our group:")
    st.write("1. Ivana SintaUli Manurung")
    st.write("2. Lilia Prita Irawati")
    st.write("3. Talitha Elga Kurniawan")
    st.write("4. Yohana Nadia Gabriella S.")

# Image Transformations page
elif menu == "Image Transformations":
    st.header("Image Transformations")

    uploaded_file = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Original Image", use_container_width=True)

        # Convert image to numpy array for manipulation
        img_array = np.array(image)

        # Brightness Adjustment
        brightness_factor = st.slider("Adjust Brightness", 0.1, 2.0, 1.0)
        enhancer = ImageEnhance.Brightness(image)
        img_bright = enhancer.enhance(brightness_factor)
        st.image(img_bright, caption="Brightness Adjusted Image", use_container_width=True)

        # Shear Transformation Adjustment
        shear_x = st.slider("Adjust Shear X", -2.0, 2.0, 0.5)
        shear_y = st.slider("Adjust Shear Y", -2.0, 2.0, 0.5)

        def shear_image(image, shear_x, shear_y):
            # Corrected shear transformation using a 6-element affine matrix
            rows, cols = image.size
            shear_matrix = [
                1, shear_x, 0,  # scale_x, shear_x, translation_x
                shear_y, 1, 0   # shear_y, scale_y, translation_y
            ]
            sheared_img = image.transform((cols, rows), Image.AFFINE, shear_matrix)
            return sheared_img

        sheared_img = shear_image(image, shear_x, shear_y)
        st.image(sheared_img, caption="Sheared Image", use_container_width=True)

        # Rotation Adjustment
        rotation_angle = st.slider("Adjust Rotation Angle", -180, 180, 0)
        img_rotated = image.rotate(rotation_angle)
        st.image(img_rotated, caption="Rotated Image", use_container_width=True)

        # Zoom Adjustment (using resizing without OpenCV)
        zoom_factor = st.slider("Adjust Zoom Factor", 1.0, 2.0, 1.0)

        def zoom_image(image, zoom_factor):
            # Zoom using PIL by resizing and then cropping to original size
            width, height = image.size
            new_width, new_height = int(width * zoom_factor), int(height * zoom_factor)
            zoomed_image = image.resize((new_width, new_height), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
            # Crop back to the original size (optional)
            left = (new_width - width) // 2
            top = (new_height - height) // 2
            right = (new_width + width) // 2
            bottom = (new_height + height) // 2
            zoomed_image = zoomed_image.crop((left, top, right, bottom))
            return zoomed_image

        zoomed_img = zoom_image(image, zoom_factor)
        st.image(zoomed_img, caption="Zoomed Image", use_container_width=True)

        # Translation Adjustment
        translation_x = st.slider("Adjust Translation X", -100, 100, 0)
        translation_y = st.slider("Adjust Translation Y", -100, 100, 0)

        def translate_image(image, tx, ty):
            # Translation using PIL's affine transformation
            rows, cols = image.size
            translation_matrix = [1, 0, tx, 0, 1, ty]
            translated_image = image.transform((cols, rows), Image.AFFINE, translation_matrix)
            return translated_image

        translated_img = translate_image(image, translation_x, translation_y)
        st.image(translated_img, caption="Translated Image", use_container_width=True)

    else:
        st.write("Please upload an image to see the transformations.")
