# Hệ thống kiểm tra chỉ số sức khoẻ - Health Index System
## Thành viên
* Vũ Bá Hướng
* Nguyễn Duy Mạnh
* Nguyễn Quang Hải
# Install Project
## Backend
### Công nghệ sử dụng:
- Flask: https://flask.palletsprojects.com/en/3.0.x/
- SQLite: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
- Scikit-fuzzy: https://scikit-fuzzy.readthedocs.io/en/latest/
### Cài đặt backend
- first step ``` cd backend ```
- copy file **.env.example** and rename this to **.env**
- Setup Environment ``` python -m venv venv ``` 
- Activate ``` . venv/Scripts/activate ```
- Install packages: ``` pip install -r requirements.txt ```
- Create file database: 
```
mkdir db
cd db
touch database.db
```
- Seeding database: ``` flask db_reset ```
### Before deploying
``` pip freeze > requirements.txt ```
### Run backend
``` flask run ```
## Frontend
### Công nghệ
- React: https://react.dev/
- React-admin: https://marmelab.com/react-admin/
### Cài đặt
first step ``` cd frontend ```
- install **Nodejs**
- copy file **.env.example** and rename this to **.env**
- install packages``` npm install ```
### Run Frontend
``` npm run start ```