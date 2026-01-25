## Django-course / (setup, MVC/MTV, models, admin)

### This is a simple Django project created to consolidate the learned material, and practical experience in working with (CRUD) operations through the UI, and using the admin panel 

### In this educational project, the following were implemented:
- Note model with several fields: (title, body, created_at)
- Basic views based on: CBV - (Class-Based Views)
- Created templates for displaying views based on: CRUD - (create, read, update, delete)
- Configured: static, basic setting file using python-decouple package, via .env (SECRET_KEY, DEBUG)
- Connected static and bootstrap (CDN) to templates

### Start-up instructions

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    ```
    ```bash
    cd <Django-Basics/django_project>
    ```
    ```bash
    python -m venv .venv
    ```
    ```bash
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```
    ```bash
    pip install -r requirements.txt
    ```
2. **Configuration:**
    ```bash
    cp .env.example .env # Create environment variables
    ```
    ```bash
    python -c 'from django.core.management.utils import 
    ```
    ```bash
    get_random_secret_key; print(get_random_secret_key())' # Generate SECRET_KEY
    # Copy the output and paste it into your .env file as the value for SECRET_KEY.
    ```
3. **Apply migrations:**
   ```
   python manage.py migrate
   ```
4. **Create Superuser(Admin)**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the development server:**
   ```
   python manage.py runserver
   ```
6. **Open in browser: Visit http://127.0.0.1:8000**