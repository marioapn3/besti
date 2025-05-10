
# 🌟 **BESTI (Bot STI)** 🚀  
An efficient backend built with **FastAPI** and **MongoDB** to power automation and decision-making for modern applications.

---

## 📝 **Overview**  
BESTI (Bot STI) is designed to be **scalable**, **maintainable**, and **developer-friendly**. Whether you're a **junior engineer** exploring backend systems or a **principal engineer** architecting robust solutions, this project caters to all levels.  

---

## ✨ **Key Features**  
- 🔥 **FastAPI Framework**: High-performance, async-ready web framework.  
- 🗄️ **MongoDB Integration**: Flexible and schema-less NoSQL database with async operations.  
- 🔐 **Secure by Design**: JWT-based authentication and bcrypt password hashing.  
- 📤 **Standardized API Output**: Pagination and response time included in all responses.  
- 🧪 **Test-Friendly**: Pytest and HTTPx for end-to-end testing.  
- 🧰 **Developer Utilities**: Advanced logging, linting, and formatting tools.

---

## 🛠️ **Tech Stack**  
| Technology                 | Purpose                                      |
| -------------------------- | -------------------------------------------- |
| 🖥️ **FastAPI**              | Web framework                                |
| 🗃️ **Motor**                | Async MongoDB driver                         |
| 🧾 **Pydantic**             | Data validation and settings management      |
| 🔐 **Python-Jose**          | JWT authentication                           |
| 🔒 **Passlib**              | Password hashing (bcrypt)                    |
| 📜 **Python-Dotenv**        | Environment variable management              |
| 🔬 **Pytest**               | Testing framework                            |
| 🧪 **HTTPx**                | Async HTTP requests for tests                |
| 🧹 **Black, Flake8, Isort** | Linting, code formatting, and import sorting |

---

## 🚀 **Quick Start Guide**  

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo/monago-automation.git
cd monago-automation
```

### 2️⃣ **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure Environment Variables**  
Create a `.env` file in the project root:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=monago_automation
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5️⃣ **Run the Application**  
```bash
uvicorn app.main:app --reload
```

### 6️⃣ **Access the API**  
📂 Visit your interactive API docs at:  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 📂 **Project Structure**  
```
monago-automation/
├── app/
│   ├── api/          # API routes
│   ├── core/         # Configuration and security
│   ├── db/           # Database connection
│   ├── models/       # Pydantic models
│   ├── schemas/      # Request/response schemas
│   ├── services/     # Business logic
│   ├── utils/        # Utility functions
│   ├── main.py       # Entry point
├── tests/            # Test cases
├── .env              # Environment variables
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

---

## 📤 **API Response Template**  

All API endpoints follow a **consistent response structure** to ensure predictability and ease of integration.

### **Response Template**
```json 
{
    "response_code": 200,
    "success": true,
    "message": {
        "ID": "Pesan dalam Bahasa Indonesia",
        "EN": "Message in English"
    },
    "data": {},
    "pagination": {
        "total": 0,
        "page": 1,
        "limit": 10,
        "total_pages": 0
    },
    "response_time": "5ms"
}
```

---

## 🔧 **Developer Tools**  

| Tool          | Command                         | Description                 |
| ------------- | ------------------------------- | --------------------------- |
| 🧹 **Black**   | `black app`                     | Code formatter              |
| 🔍 **Flake8**  | `flake8 app`                    | Linter for Python code      |
| 📜 **Isort**   | `isort .`                       | Sorts imports               |
| 🧪 **Pytest**  | `pytest`                        | Runs test cases             |
| 🌐 **HTTPx**   | Used in tests for HTTP requests |
| 🧰 **Loguru**  | Advanced logging tool           |
| 🌐 **Uvicorn** | `uvicorn app.main:app --reload` | Runs the development server |

---

## 📜 **Dependencies**  

### **Core Dependencies**
```text
fastapi>=0.100.1
uvicorn[standard]==0.23.0
motor==3.2.0
bson>=0.5.10
pydantic[email]>=2.0.0
pydantic-settings>=2.0.0
python-jose==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
```

### **Testing Dependencies**
```text
pytest==7.4.0
pytest-asyncio==0.21.0
httpx==0.24.0
```

### **Linting and Formatting**
```text
flake8==6.1.0
black==23.10.0
isort==5.12.0
```

### **Optional Tools**
```text
loguru==0.7.0
```

---

## 🧑‍💻 **Contributing**  
We welcome contributions from **juniors** to **principals**! 💪  

### Steps to Contribute:
1. Fork the repo 🍴  
2. Create a feature branch: `git checkout -b my-feature`  
3. Commit your changes: `git commit -m "Add new feature"`  
4. Push and create a Pull Request 🚀  

---

## 🌟 **Feedback & Support**  
Your feedback is invaluable! Share your thoughts or report issues:  
- 📧 Email: support@monago.io  
- 🐛 Issues: [GitHub Issues](https://github.com/monagoio/monago-automation/issues)  

---

### ✍️ **Authors**  
Developed with ❤️ by the **Founders & AI**.

---
