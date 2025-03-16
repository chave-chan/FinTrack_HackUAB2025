# 🏦 FinTrack - Educación y Gestión Financiera con IA

**FinTrack** es una aplicación móvil que ayuda a jóvenes y personas con poca experiencia en finanzas a aprender sobre gestión del dinero, seguridad en pagos digitales y ahorro.

## 🚀 Tecnologías Usadas
- **Frontend:** React Native (Expo)
- **Backend:** FastAPI (Python)
- **Base de datos:** PostgreSQL
- **Autenticación:** Google OAuth
- **Pagos:** API de Pay Retailers
- **IA:** Chatbot con Perplexity AI y mascota interactiva
- **Docker:** Para despliegue y desarrollo local

## 📌 Instalación

### **1️⃣ Clonar el repositorio**
```sh
git clone https://github.com/user/FinTrack.git
cd FinTrack
```

### **2️⃣ Crear un entorno virtual e instalar dependencias**
```sh
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Configurar las variables de entorno (.env)**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/fintrack
SECRET_KEY=your_secret_key
```

### **4️⃣ Crear y migrar la base de datos**
```sh
python3 setup_db.py  # Script para inicializar PostgreSQL
```

### **5️⃣ Ejecutar el backend**
```sh
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### **6️⃣ Instalar dependencias del frontend**
```sh
cd frontend
npm install
```

### **7️⃣ Ejecutar el frontend**
```sh
npm start
```

### **Instalar y ejecutar la app en iOS**
```sh
npx expo install expo-dev-client
npx expo run:ios
```

## 📌 Ejecución con Docker

```sh
docker-compose up --build
```