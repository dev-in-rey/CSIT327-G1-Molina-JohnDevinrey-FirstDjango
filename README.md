# CampusConnect — CSIT327 Lab Challenge

- **Student Name:** John Devinrey A. Molina
- **Section:** G1
- **Course:** CSIT327

---

## Overview

**CampusConnect** is a Django web portal featuring role-based user authentication, profile viewing and self-service profile editing (`UpdateView`), user feedback notifications via Django's `messages` framework, and a responsive institutional UI styled with **Bootstrap 5 (via CDN)**.

### Key Features
1. **Profile Page (`ProfileView` & `ProfileUpdateView`)**
   - Logged-in users can view (`/accounts/profile/`) and edit (`/accounts/profile/edit/`) their own profile using Django's class-based `UpdateView`.
   - Protected by `LoginRequiredMixin` and locked to `self.request.user` (`get_object()`), preventing any user from opening or editing another user's profile.
2. **Sign-Up Feedback (`SuccessMessageMixin` + Django Messages Framework)**
   - Displays a dismissible Bootstrap 5 alert (`alert alert-success`) after a user registers successfully and redirects to the login page.
3. **Bootstrap 5 Polish (`base.html` & Styled Forms)**
   - Shared `templates/base.html` loads Bootstrap 5 CSS & JS bundle from jsDelivr CDN and provides a responsive navigation bar.
   - All pages (`login.html`, `signup.html`, `profile.html`, `profile_edit.html`, `home.html`, `admin_panel.html`) extend `base.html`.
   - All forms (`CustomAuthenticationForm`, `CustomerUserCreationForm`, `ProfileUpdateForm`) style inputs with Bootstrap's `form-control` and `btn` classes.

---

## Steps to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
cd CSIT327-G1-Molina-JohnDevinrey-FirstDjango
```

### 2. Create and Activate a Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. (Optional) Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```
Open your browser and visit: **http://127.0.0.1:8000/**
