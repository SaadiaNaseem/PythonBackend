# 💼 InfoTech Job Application Portal

A full-stack job application system built with **React (frontend)** and **Flask (backend)**. Applicants can submit their personal information, upload resumes, and get a success confirmation — all connected with a live backend API.

---

## 🛠️ Tech Stack

| Layer      | Technology                                |
|------------|--------------------------------------------|
| Frontend   | React, TailwindCSS, Axios, Framer Motion   |
| Backend    | Python, Flask, Flask-CORS, Flask-SQLAlchemy |
| Deployment | Railway (for Flask backend)                |
| Tools      | Git, GitHub, Railway, dotenv               |

---

## 📁 Project Structure

```

InfoTech-Solutions/
├── Client/                  # React Frontend
│   ├── src/
│   │   ├── pages/
│   │   │   └── ApplicationForm.jsx
│   │   └── api/axios.js
│   └── package.json
│
└── server/                  # Flask Backend
├── app/
│   ├── **init**.py
│   ├── routes.py
│   ├── models.py
│   └── utils.py
├── uploads/             # Folder for uploaded resumes
├── config.py            # (Optional) Flask configurations
├── requirements.txt
└── run.py               # Flask app entry point

````

---

## 🔗 Live Link

- ✅ **Backend (Flask)**:  
  [https://pythonbackend-production-5f89.up.railway.app](https://pythonbackend-production-5f89.up.railway.app)

- ❗**Frontend** (can be deployed on Netlify, Vercel, etc.)

---

## ⚙️ Features

- Beautiful responsive form with TailwindCSS
- Real-time input validation
- Resume upload (PDF, DOC, DOCX)
- Submission feedback with alerts
- Flask backend connected via Axios
- Files saved on backend `/uploads` folder
- Deployed backend — no local server required

---

## 🚀 Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/SaadiaNaseem/PythonBackend.git
````

---

### ✅ 2. Run the Frontend (React)

```bash
cd Client
npm install
npm start
```

➡️ Open `src/api/axios.js` and make sure it looks like:

```js
import axios from "axios";

const API = axios.create({
  baseURL: "https://pythonbackend-production-5f89.up.railway.app",
});

export default API;
```

---

### ✅ 3. Run the Backend Locally (Optional)

```bash
cd server
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For Mac/Linux

pip install -r requirements.txt
python run.py
```

Make sure `run.py` has:

```python
app.run(host="0.0.0.0", port=5000)
```

---

## ☁️ Deploy Flask Backend to Railway

1. Push your `/server` folder to GitHub
2. Go to [https://railway.app](https://railway.app)
3. Create New Project → GitHub Repo
4. Set:

   * **Install Command**: `pip install -r requirements.txt`
   * **Start Command**: `python run.py`
5. Your app will go live at:
   `https://your-app-name.up.railway.app`

---

## 🧾 .gitignore for Backend

```
venv/
__pycache__/
uploads/
.env
*.pyc
```

---

## 📦 Dependencies Used

### 🔹 Backend (Flask)

```txt
flask
flask_sqlalchemy
flask_cors
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

### 🔹 Frontend (React)

```bash
npm install axios framer-motion tailwindcss
```

---

## 👩‍💻 Developed By

**Saadia Naseem**
For Internship Project at **InfoTech Solutions**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

````

---

### ✅ Next Step:

1. Paste this in your GitHub project as `README.md`
2. Run:

```bash
git add README.md
git commit -m "docs: added professional README"
git push
````
