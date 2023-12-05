# Bài Tập Lớn Hệ thống tri thức
## Thành viên
* Vũ Bá Hướng
* Nguyễn Duy Mạnh
* Nguyễn Quang Hải
# Install Project
## Backend
``` cd backend ```
### Config
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
### Run server
``` flask run ```
## Frontend
``` cd frontend ```
- install **Nodejs**
- copy file **.env.example** and rename this to **.env**
### Install packages
``` npm install ```
### Run server
``` npm run start ```