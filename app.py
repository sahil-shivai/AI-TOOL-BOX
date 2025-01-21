import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI
st.title("AI-Powered Image Prompt Generator")
st.write("Generate creative prompts for image generation using AI.")


# User input
user_input = st.text_input("Enter your basic idea (e.g. 'a futuristic city')")

# Prompt length selection
length = st.slider("Select Prompt Length:", 50, 500, 150)

# Paragraph format checkbox
paragraph_format = st.checkbox("Provide output in paragraph format")

# Generate prompt function
def generate_prompt(user_input, length, paragraph_format):
    if not user_input:
        return "Please enter an idea to generate a prompt."
    
    format_type = "paragraph format" if paragraph_format else "bullet points"
    prompt_template = f"Generate a {format_type} image description based on the idea: {user_input}. Keep it under {length} words."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt_template)
    
    return response.text

# Button to generate
if st.button("Generate Prompt :white_check_mark:"):
    with st.spinner("Generating..."):
        prompt = generate_prompt(user_input, length, paragraph_format)
        st.success("Generated Prompt:")
        st.code(prompt, language="text")  # Provides copy button


st.markdown('''
---  

# **User Guide: AI-Powered Image Prompt Generator**  

Welcome to the **AI-Powered Image Prompt Generator**, a tool designed to help you create highly detailed and creative prompts for AI-generated images effortlessly.  

---  

## **How to Use**  

### **1. Enter Your Idea**  
- In the input field, type a basic idea or concept for your image.  
  - Example: *"A futuristic cyberpunk city at sunset"*  

### **2. Adjust Prompt Length**  
- Use the slider to control how detailed you want the prompt to be.  
  - **Short (50 words)** – Quick descriptions.  
  - **Medium (150 words)** – Balanced details.  
  - **Long (500 words)** – Highly detailed descriptions.  

### **3. Choose Output Format**  
- Select the checkbox **“Provide output in paragraph format”** if you want the prompt in paragraph form.  
- If unchecked, the output will be provided as bullet points for better structure.  

### **4. Generate the Prompt**  
- Click the **"Generate Prompt"** button to let the AI create a detailed image prompt based on your inputs.  
- The generated prompt will appear below the button.  

### **5. Copy the Prompt**  
- Use the **"Copy" button** next to the prompt to copy it to your clipboard for easy pasting into your preferred AI image generator.  

---

## **Example Usage**  

**Input:**  
*"A majestic medieval castle surrounded by misty mountains."*  

**Settings:**  
- Length: *250 words*  
- Paragraph format: *Checked*  

**Generated Output (Example):**  
*"A grand medieval castle stands tall amidst misty, towering mountains. The structure is adorned with towering spires, intricate stone carvings, and weathered banners fluttering in the wind. The atmosphere is serene yet majestic, with a faint golden sunrise piercing through the mist, illuminating the castle's silhouette..."*  

---

## **Tips for Best Results**  

- Be as specific as possible with your input idea to get more accurate prompts.  
- Use the bullet point format for easier breakdown of elements when working with detailed image composition.  
- Try different prompt lengths to experiment with varying levels of detail.  

---

Enjoy creating your AI-generated art with rich and creative prompts! 🎨✨  

---  
''')

st.info("this app created by sahil makwana for more AI content follow me on instagram @pixeln.biz")
st.link_button("Follow me on Instagram :camera:", "https://www.instagram.com/pixeln.biz")