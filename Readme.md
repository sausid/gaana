# Gaana Assignment

A Django project for handling location data with CRUD operations.

## 🚀 Project Setup

1. **Clone the Repository:**  
   ```bash
   git clone git@github.com:sausid/gaana.git
   cd gaana
   ```

2. **Create a Virtual Environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**  
   ```bash
   make migrations
   make migrate
   ```

5. **Run Initial Data Setup:**  
   ```bash
   make initial_setup
   ```

6. **Start the Development Server:**  
   ```bash
   make runserver
   ```

---

## 📦 API Endpoints

### 1️⃣ **List All Locations**  
- **URL:** `/api/locations/`  
- **Method:** `GET`  
- **Response:** Returns a list of all locations.
- **cURL:** 
    ```bash
    curl -X GET http://127.0.0.1:8000/api/locations/
    ```

### 2️⃣ **Create a New Location**  
- **URL:** `/api/locations/`  
- **Method:** `POST`  
- **Body Example:**  
  ```json
  {
    "name": "Abu Dhabi",
    "city": "Abu Dhabi",
    "country": "UAE",
    "code": "52001"
  }
  ```
- **cURL:** 
    ```bash
    curl -X POST http://127.0.0.1:8000/api/locations/ -H "Content-Type: application/json" -d '{"name": "Abu Dhabi", "city": "Abu Dhabi", "country": "UAE", "code": "52001"}'
    ```

### 3️⃣ **Retrieve a Single Location**  
- **URL:** `/api/locations/<id>/`  
- **Method:** `GET`  
- **Response:** Returns details of the specific location.
- **cURL:** 
    ```bash
    curl -X GET http://127.0.0.1:8000/api/locations/<id>/
    ```

### 4️⃣ **Update a Location**  
- **URL:** `/api/locations/<id>/`  
- **Method:** `PUT`  
- **Body Example:**  
  ```json
  {
    "name": "Dubai",
    "city": "Dubai",
    "country": "UAE",
    "code": "52003"
  }
  ```
- **cURL:** 
  ```bash
  curl -X PUT http://127.0.0.1:8000/api/locations/<id>/ -H "Content-Type: application/json" -d '{"name": "Dubai", "city": "Dubai", "country": "UAE", "code": "52003"}'
  ```

### 5️⃣ **Delete a Location**  
- **URL:** `/api/locations/<id>/`  
- **Method:** `DELETE`
- **cURL:** 
  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/locations/<id>/
  ```

---

## 🔑 Notes
- Ensure `data.json` is in the project root before running `initial_setup`.
---
