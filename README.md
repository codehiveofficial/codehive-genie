# Codehive Genie 🧞‍♂️✨  
**An AI-driven coding assistant integrated into the [Codehive](https://github.com/codehiveofficial/codehive) platform.**  

Codehive Genie is a Python-based Flask API that leverages advanced Large Language Models (LLMs) to provide coding assistance within the Codehive collaborative platform. It specializes in generating, debugging, and optimizing code, designed to empower developers with seamless and accurate coding support.

---

## ✨ Features  

### 🌟 Core Capabilities  
- 🚀 **Code Assistance**: Generate, debug, and optimize code snippets.  
- 🌐 **Supported Languages**: Python, C, JavaScript, Java, TypeScript, and C++ (CPP).  
- 🔧 **High-Quality Output**: Delivers well-structured, production-ready code with inline comments and concise explanations.  
- 🌀 **Streaming Responses**: Enables real-time responses to ensure minimal latency.  
- ❌ **Strict Query Handling**: Ignores non-coding-related queries with polite and concise error messages.  

### 🔒 Security Enhancements  
- 🌍 **Language Detection**: Ensures input is in English for consistency and accuracy.  
- 🛡️ **Authentication**: API access secured with an `Authorization` header.  
- 📜 **Robust Logging**: Detailed query and response logging for improved monitoring and debugging.  

### 🌐 Deployment  
- 🖥️ **Hosted on Vercel**: Optimized deployment using Vercel's Flask template for high performance and scalability.  

---

## 💻 Tech Stack  

### Backend  
- 🐍 **Flask**: Lightweight and efficient framework for API development.  
- 🤖 **Groq AI Cloud**: LLM parameterization using **Llama 3.3-70B Versatile**.  
- 📚 **Python Libraries**:  
  - 🔄 `flask-cors`: To handle cross-origin requests.  
  - 🔐 `dotenv`: For secure environment variable management.  
  - 🧩 `langdetect`: For detecting input language.  

### Deployment  
- 🚀 **Vercel**: Optimized and scalable deployment with Flask templates.  

---

## 🌐 API Overview  

### 🌍 Base URL  
Deployed on [Vercel](https://vercel.com/):  

### 📜 Endpoints  

#### 1. **Home Endpoint**  
- **GET** `/`  
- **Description**: Basic health check for the server.  
- **Response**:  
```text  
Hello, World!  
```  

#### 2. **Codehive Genie Endpoint**  
- **POST** `/genie`  
- **Description**: Processes user queries to provide AI-generated coding assistance.  

- **Headers**:  
  - 🔐 `Authorization`: The authorization secret key for secure access.  

- **Request Body**:  
  ```json  
  {
    "query": "Write a Python function to reverse a string."
  }  
  ```  

- **Response**:  
  - ✅ **For Valid Queries** (Streamed Response):  
    ```plaintext  
    def reverse_string(s):  
        # Return the string in reverse order  
        return s[::-1]
    ```  

  - 🚫 **For Invalid Queries**:  
    ```json  
    {
      "error": "Invalid authorization secret."
    }
    ```  

  - ⚠️ **For Non-Coding Queries**:  
    ```plaintext  
    Sorry, I am an AI assistant tuned for coding and programming purposes only. I cannot assist with this query.  
    ```  

---

## 🛠️ Installation  

### Prerequisites  
- 🐍 **Python**: 3.8 or higher  
- 🤖 **Groq API Key**: Available from [Groq Cloud Platform](https://groq.com/groqcloud/)  
- 🌟 **Node.js** (optional for integration testing with Codehive)  

### 🚀 Clone the Repository  
```bash  
git clone https://github.com/codehiveofficial/codehive-genie.git  
cd codehive-genie  
```  

### 🔐 Set Up Environment Variables  
Create a `.env` file in the root directory and add the following:  
```env  
AUTH_SECRET=<your_auth_secret>  
GROQ_API_KEY=<your_groq_api_key>  
```  

### 📦 Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

---

## 🚦 Usage  

### ▶️ Start the Server Locally  
```bash  
python api/index.py  
```  
- The server will run locally on **http://127.0.0.1:5000/** by default.  
- You can access the **home endpoint** at **http://127.0.0.1:5000/** to verify the server is running.  

---  

Let me know if you need further adjustments! 🚀

### 🔄 Test the API  
- Use tools like **Postman** or **cURL** to test the `/genie` endpoint.  
- Include the required `Authorization` header and send a JSON body with your query.  

---

## 🤝 Integration with Codehive  

Codehive Genie is integrated as the AI assistant within the **[Codehive](https://github.com/codehiveofficial/codehive)** platform. It powers the AI-driven **Codehive Genie** feature, enabling users to receive coding assistance directly within collaborative rooms.  

---

## 📜 License  

Codehive Genie is licensed under the **[MIT License](https://github.com/codehiveofficial/codehive-genie/blob/main/LICENSE)**.  
