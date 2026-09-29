# 🛒 Online Shop

A simple e-commerce web application built with **Django**, featuring user authentication with email verification, a shopping cart, product categories, and a clean, modern UI.

> یک فروشگاه اینترنتی ساده با جنگو — شامل ثبت‌نام با تایید ایمیل، سبد خرید، دسته‌بندی محصولات و رابط کاربری مدرن.

---

## ✨ Features

- **Custom User Authentication**
  - Registration with 6-digit email verification code
  - Login with phone number
  - Logout
  - Password confirmation validation
- **User Profile**
  - View account details
  - Cart summary stats
- **Product Catalog**
  - Home page with product grid
  - Product detail page
  - Category filtering
  - Search by product name
- **Shopping Cart**
  - Session-based cart (works for guests too)
  - Add / remove items
  - Choose quantity
  - Total price calculation
- **Modern UI**
  - Responsive Bootstrap 5 (RTL) layout
  - Custom blue-themed design
  - Animated particle background on auth pages

---

## 🛠 Tech Stack

- **Backend:** Django 6
- **Database:** SQLite (default)
- **Frontend:** Bootstrap 5 (RTL) + custom CSS
- **Email:** Django SMTP backend (Gmail)
- **Font:** Vazirmatn (Persian web font)

---

## 📁 Project Structure

```
A/
├── account/        # Custom user model, auth views, forms
├── home/           # Products, categories, home page
├── cart/           # Session-based shopping cart
├── static/         # CSS, JS
├── templates/      # Base templates, navbar, includes
├── media/          # Uploaded product images
└── manage.py
```

---

## 🚀 Setup

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd shop-env
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root (see `.env.example`) with:
   ```
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. Run migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/`

---

## 📌 Notes

- Cart data is stored per-session, so it works even before logging in.
- Email codes are sent via Gmail SMTP — make sure to use an **App Password**, not your real Gmail password.
- This project is for learning purposes; payment/checkout flow is not implemented.

---

## 📄 License

This project is open for educational use.
