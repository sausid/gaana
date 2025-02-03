# Gaana Assignment

A Django project for handling location data with CRUD operations.

## 🚀 Project Setup

1. **Clone the Repository:**  
   ```bash
   git clone <repository_url>
   cd gaana
   ```

2. **Create a Virtual Environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. **Install Dependencies:**  
   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations:**  
   ```bash
   python manage.py migrate
   ```

5. **Run Initial Data Setup:**  
   ```bash
   python manage.py initial_setup data.json
   ```

6. **Start the Development Server:**  
   ```bash
   python manage.py runserver
   ```

---

## 📦 API Endpoints

### 1️⃣ **List All Locations**  
- **URL:** `/api/locations/`  
- **Method:** `GET`  
- **Response:** Returns a list of all locations.

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

### 3️⃣ **Retrieve a Single Location**  
- **URL:** `/api/locations/<id>/`  
- **Method:** `GET`  
- **Response:** Returns details of the specific location.

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

### 5️⃣ **Delete a Location**  
- **URL:** `/api/locations/<id>/`  
- **Method:** `DELETE`

---

## 🔑 Notes
- Ensure `data.json` is in the project root before running `initial_setup`.
- Use `make initial_setup` if a `Makefile` is configured.

---

**Developed with Django & DRF**

