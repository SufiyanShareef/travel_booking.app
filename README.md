# 🧳 Travel Booking Application

A **full-stack web application** built with **Django** to allow users to browse travel options, book tickets, and manage their bookings. The app includes **user authentication**, a **responsive design**, and a **modern travel-themed UI**.

![Django](https://img.shields.io/badge/Django-5.2.5-green.svg) 
![Python](https://img.shields.io/badge/Python-3.13-blue.svg) 
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-purple.svg) 
![Railway](https://img.shields.io/badge/Deployed_on-Railway-black.svg)

---

## 🌟 Live Demo

**Try the app:** [Travel Booking App](https://travel-bookings.up.railway.app)

---

## ✨ Features

### 🔐 **User Authentication**
- Sign up, login, and logout functionality
- Manage user profile with personal information
- Secure password handling with Django's built-in authentication system

### 🎫 **Travel Management**
- Browse a wide variety of travel options (Flights, Trains, Buses)
- Advanced filtering by destination, source, travel type, and date
- Real-time seat availability and pricing details

### 📋 **Booking System**
- Easy-to-use seat selection for booking tickets
- Automatic price calculation and summary
- Booking history and tracking
- View, modify, and cancel bookings

### 🎨 **User Interface**
- Modern and clean UI using **Bootstrap 5**
- Mobile-friendly and responsive design
- Travel-themed color scheme and sleek hover animations

---

## 🛠️ Technology Stack

- **Backend:** Django 5.2.5, Python 3.13
- **Database:** MySQL 8.0
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.1
- **Icons:** Font Awesome 6.0
- **Deployment:** Railway.app
- **Static Files:** Whitenoise

---

## 📦 Installation & Local Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- Git

### Step-by-Step Setup

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/SufiyanShareef/travel_booking.app.git
    cd travel_booking.app
    ```

2. **Create a Virtual Environment**  
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Database Setup**
    1. Create a MySQL database named `travel_booking_db`.
    2. Update the `DATABASES` settings in `travel_booking/settings.py` with your credentials.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'travel_booking_db',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. **Run Migrations**  
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser**  
    ```bash
    python manage.py createsuperuser
    ```

7. **Collect Static Files**  
    ```bash
    python manage.py collectstatic
    ```

8. **Start Development Server**  
    ```bash
    python manage.py runserver
    ```

Now, visit `http://localhost:8000` to see the app in action!

---

## 🚀 Deployment on Railway

1. **Fork** this repository
2. **Connect** your GitHub account to Railway
3. **Create a new project** from your GitHub repository
4. **Add MySQL plugin** to the Railway project
5. **Connect services** - Link MySQL to your Web service
6. **Deploy automatically** - Railway will detect Django and deploy the app for you

### Environment Variables for Production
- `DATABASE_URL`: MySQL connection string (auto-set by Railway)
- `DEBUG`: Set to `False` in production
- `SECRET_KEY`: Django secret key (keep it safe!)
- `ALLOWED_HOSTS`: Set this to your Railway domain

---

## 📁 Project Structure

```plaintext
travel_booking.app/
├── bookings/                 # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   ├── views.py             # Views for handling requests
│   ├── urls.py              # App URL routes
│   └── forms.py             # Django forms
├── travel_booking/          # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL routes
│   └── wsgi.py              # WSGI configuration
├── static/                  # Static files
├── requirements.txt         # Python dependencies
└── manage.py                # Django management script


🎯 Usage Guide
Registration: Sign up to create a new account or log in with existing credentials

Browse Travel Options: Use filters to find flights, trains, and buses that suit your preferences

Booking: Select your preferred seats and confirm your booking

Manage Bookings: View and cancel your bookings directly from the dashboard

Profile Management: Keep your contact and account information updated

🔧 API Endpoints
Endpoint	Method	Description
/	GET	Homepage
/register/	GET/POST	User registration
/login/	GET/POST	User login
/logout/	POST	User logout
/travel/	GET	Browse travel options
/booking/new/<id>/	GET/POST	Create booking
/bookings/	GET	View user bookings
/booking/cancel/<id>/	POST	Cancel booking
/profile/	GET/POST	User profile management

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👤 Author
Sufiyan Shareef

GitHub: @SufiyanShareef

Project Link: https://github.com/SufiyanShareef/travel_booking.app

🙏 Acknowledgments
Django Documentation and Community

Bootstrap for responsive UI components

Font Awesome for beautiful icons

Railway for seamless deployment

MySQL for reliable database management

⭐ Star this repo if you found it helpful! ✨



