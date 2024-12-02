# **AI-KMS**  
### _AI-Powered Chatbot with Streamlit and Gemini_  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Framework-orange) ![Gemini](https://img.shields.io/badge/Gemini-AI_Model-green)
<!-- ![License](https://img.shields.io/badge/license-MIT-blue) -->

This project demonstrates an AI-powered chatbot built with **Streamlit**, integrating **Google's Gemini-1.5-Flash** model for seamless conversational interactions. The chatbot supports text-based responses and experimental file upload features.


## 🌟 **Features**  

- **🤖 Conversational AI:** Engage in natural language interactions.  
- **💡 Gemini Integration:** Leverages **Gemini-1.5-Flash** for intelligent responses.  
- **🎨 User-Friendly UI:** Clean and simple interface built with Streamlit.  
- **📂 File Upload (Experimental):** Upload and process supported file types ([view file types](#-supported-file-types)).  


## 🚀 **Getting Started**  

### ✅ **Prerequisites**  
- **Python 3.8+**  
- Install dependencies:  
  ```bash  
  pip install -r requirements.txt  
  ```  

### 🔑 **API Key Setup**  
1. Obtain your **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/apikey).  
2. Create a file named `secrets.toml` in the project root:  
   ```toml  
   GOOGLE_API_KEY = "YOUR_API_KEY_HERE"  
   ```  

### ▶️ **Run the Application**  
To start the app locally:  
```bash  
streamlit run app.py  
```  

### 🌐 **Online Access**  
Access the hosted app on Streamlit Cloud: [AI-KMS Chatbot](https://kmschatbot.streamlit.app).  


## 🗂️ **Project Structure**  

| File/Folder       | Description                                   |  
|-------------------|-----------------------------------------------|  
| `app.py`          | Main Streamlit application file.              |  
| `secrets.toml`    | API key storage (keep secure).                |  
| `requirements.txt`| Python package dependencies.                  |  


## 🤔 **Model Details**  

| Feature                     | Description                              |  
|-----------------------------|------------------------------------------|  
| **Model**                   | Gemini-1.5-Flash                         |  
| **Max Tokens**              | 1 Million                                |  
| **Tokens per File/Page**    | ~258 tokens (document/image)             |  
| **Tokens per Audio Second** | ~25 tokens                               |  


## 📂 **Supported File Types**  

### 📝 **Text Formats**  
`pdf`, `txt`, `csv`, `tsv`, `html`, `py`, `js`, `json`

### 🖼️ **Image Formats**  
`png`, `jpg`, `jpeg`, `webp`, `gif`, `tiff`, `bmp`

### 🔊 **Audio Formats**  
`wav`, `mp3`, `aac`, `ogg`, `flac`, `dts`

### 🎥 **Video Formats**  
`mp4`, `mov`, `mkv`, `webm`, `avi`

> [!Note]
> - Ensure files are clear and properly oriented.  
> - File processing is experimental and supports limited file types.  


## 🔮 **Future Enhancements**  

- 🚀 **Improved File Handling**: Seamless integration of uploaded files.  
- 🧠 **Contextual Memory**: Retain and utilize conversation history.  
- 🛠️ **Error Handling**: Enhanced feedback and error messaging.  
- 🌍 **Expanded File Support**: Include additional formats.  

<!-- 
## 🤝 **Contributing**  

Contributions are always welcome!  

1. Fork the repository.  
2. Create a new feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add new feature"`).  
4. Push to your branch (`git push origin feature-name`).  
5. Open a Pull Request.  


## 📜 **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---
 -->