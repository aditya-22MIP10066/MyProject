# 🏠 Hostel Market

## 🌟 Project Overview

**Hostel Market** is a web-based marketplace specifically designed for hostel students. It enables students to buy and sell items easily within their hostel community. From second-hand books and electronics to daily necessities or handmade goods, Hostel Market fosters a localized and efficient platform for peer-to-peer transactions.

---

## 🎥 Demo Video

📽️ [Click here to watch the demo video](https://drive.google.com/file/d/1UPEo9_B57aHQgXzJB5dod5d0uy6p2GWt/view?usp=sharing)

---

## ✨ Features

### 🛍️ Item Listings (CRUD Functionality)
- **Create**: Add items for sale with name, description, quantity, price, and image.
- **Read**: Browse all available items and view detailed pages.
- **Update**: Edit existing listings (only by the owner).
- **Delete**: Remove listed items (only by the owner).

### 🔐 User Authentication & Authorization
- **User Accounts**: Secure registration, login, and logout using Django's auth system.
- **Authorization**: Only logged-in users can manage their listings.
- **Ownership**: Users can edit/delete only their own items.

### 🖼️ Image Uploads
- Upload and display item images.
- Thumbnail view in listings; detailed view in item page.

### 🕒 Timezone Localization (IST)
- Item timestamps are localized to Indian Standard Time.

### 🚀 User-Friendly Interface
- Clean, simple, and intuitive frontend design for ease of use.

---

## 💻 Technologies Used

- **Backend**: Python 3.x, Django 5.x  
- **Frontend**: HTML5, CSS3  
- **Database**: SQLite3 (development)  
- **Image Handling**: Pillow library  
- **Dependency Management**: pip, `requirements.txt`

---

## ⚙️ Setup and Installation

```bash
#1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/hostel-market.git
cd hostel-market

#2. Create and Activate a Virtual Environment
python -m venv myvenv
#Windows:
myvenv\Scripts\activate
#macOS/Linux:
source myvenv/bin/activate

#3. Install Dependencies
pip install -r requirements.txt

#4. Apply Migrations
python manage.py makemigrations listings
python manage.py migrate

#5. Create Superuser
python manage.py createsuperuser

#🚀 Usage
python manage.py runserver
# Open your browser at: http://127.0.0.1:8000/market/
```
### Test It Out
- Register a new user account.
- Login and post your first item.
- Explore other listings.
- Visit the Admin Panel at: http://127.0.0.1:8000/admin/

---

## 📁 Project Structure

```bash
hostel-market/
├── hostel_market/              # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── listings/                   # App for item listings
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── templates/
│   │   ├── listings/
│   │   │   ├── item_list.html
│   │   │   ├── item_detail.html
│   │   │   ├── item_form.html
│   │   │   └── item_confirm_delete.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── signup.html
│   ├── static/
│   │   └── css/
│   │       ├── login.css
│   │       └── item_confirm_delete.css
├── media/                      # Uploaded images
├── db.sqlite3                  # SQLite DB
├── manage.py
├── myvenv/                     # Virtual environment
└── requirements.txt
```

## 🌱 Future Enhancements
- 🔍 Advanced Search & Filters (by keyword, price, category)

- 👤 User Profiles with listing history

- 💬 Direct Messaging between buyers and sellers

- ⭐ Ratings & Reviews for users/items

- 🗂️ Categories like Books, Electronics, Clothing, etc.

- ❤️ Favorites/Bookmarks

- 🔔 Notifications System

- ☁️ Deployment with Docker or a cloud host (e.g., Render, Heroku)
