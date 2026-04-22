
init project (สร้าง โปรเจค)
```
uv run django-admin startproject my_project_name .

```

run server ( รันโปรแกรม )
```
uv run python manage.py runserver
```

run migration ( รัน ก่อนใช้งาน )
```
 python manage.py migrate medium ## OPTION 1 (เลือกแล้วทำการ migrate อีกรอบ)

 ```


 # 1. ลบ migration เก่าและ db
rm medium/migrations/0001_initial.py medium/migrations/0002_rename_post_blog_content_and_more.py
rm db.sqlite3

# 2. สร้าง migration ใหม่
python manage.py makemigrations medium
python manage.py migrate

# 3. สร้าง superuser
python manage.py createsuperuser