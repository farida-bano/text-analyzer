import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text Analysis", page_icon="📝", layout="centered")

    st.markdown("""
    <style>
        body {
            background-color: #f0f4f8; /* Light background color for the page */
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #ebeefo;
        }
        .stTextArea, .stTextInput { 
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton > button { 
            background-color: #4CAF50; 
            color: white; 
            border-radius: 10px; 
            padding: 12px 24px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049; /* Slightly darker green on hover */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #4CAF50;
        }
        .stMarkdown {
            font-size: 18px;
            color: #333;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("Text Analysis in Python 📝")
    st.write("Analyze your text quickly and efficiently. 📊")

    paragraph = st.text_area("Enter a paragraph: ✍️", "", height=150)

    if paragraph:
        st.markdown("---")
        st.subheader("Analysis Results 📋")

        # Word and character count
        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)
        col1, col2 = st.columns(2)
        col1.metric("Total Words 📝", word_count)
        col2.metric("Total Characters ✨", char_count)

        # Search and Replace feature
        st.subheader("Search and Replace 🔍")
        search_word = st.text_input("Enter a word to search from the paragraph: 🔎")
        replace_word = st.text_input("Enter a word to replace with: 🔄")

        if search_word and replace_word:
            # Use re.sub with \b to match word boundaries
            modified_paragraph = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.success("Modified Paragraph! ✅")
            st.text_area("Modified Paragraph:", modified_paragraph, height=150)

        # Uppercase and Lowercase feature
        st.subheader("Uppercase and Lowercase Feature 🔠")
        st.text_area("Uppercase 🔡:", paragraph.upper(), height=150)
        st.text_area("Lowercase 🔡:", paragraph.lower(), height=150)

        # Check for 'Python' keyword
        contains_python = "Python" in paragraph
        st.write(f"Contains 'Python' 🐍: {contains_python}")

        # Average word length
        average_word_length = char_count / word_count if word_count else 0
        st.write(f"Average Word Length 📏: {average_word_length:.2f}")

    else:
        st.warning("Please enter a paragraph for analysis. ⚠️")

if __name__ == "__main__":
    main()
