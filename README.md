
## E-Shop Application

Sweet Mart is a complete E-Shop application through which customers can buy sweets online.
Using this application, customers/users can view blogs and products, share thier review about it (blog comments and product review), add, edit and modify cart items (products) and checkout after entering delivary address and completing payment.
Customer authentication is done using *JWT Authentication*. Database used is *mySQL* which is django's default database. Payment Gateway used is *Razorpay*.

### 🔗 Content

* [Overview](#e-shop-application)
* [Content](#-content)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Environment Variables](#-environment-variables)
* [Run Locally](#-run-locally)
* [Documentation](#-documentation)
* [Demo](#-demo)
* [Screen-Shots](#-screen-shots)
* [Author](#-author)


### 📋 Features

- **USER AUTHENTICATION :** Users can Signup for a new account, Verify thier email id, Login using email and password, make a Forgot request to reset thier password.

- **PRODUCTS AND BLOGS :** Users can view all products and blogs.

- **REVIEWS AND RATING :** User can add blogs comments, product review and rateings.

- **CONTACT US FORM :** User can fill up the Contact Us form. (Auto Corrospondence email sending feature)

- **CART FUNCTIONALITY :** User can add and remove products from cart. Users can also change the quantity of items in thier cart.

- **PAYMENT GATEWAY :** Users can make payment using Net-Banking, UPI, Card Payments, etc. through Razorpay Payment Gateway which is integrated in the system.

- **AUTO INVOICE :** After payment, users would recieve invoice (auto-generated) in thier mailbox.


### 🧰 Tech Stack

- **`BACKEND`** : Django *(Python)*

- **`DATABASE`** : mySQL


### 🛠 API Reference

**Postman Endpoints** : https://www.getpostman.com/collections/810602ef1d1d81df854b

![Endpoints](docs/endpoints.png)

**API Endpoints JSON file** (for importing into thunderclient / postman) is available in the docs folder or click [here](docs/endpoints.json)


### 🔐 Environment Variables

To run this project, you will need to add the following environment variables to your **.env** file

- `EMAIL_ID`  -  Email ID (which would be used to send emails)

- `EMAIL_PW`  -  Email Password

- `PUBLIC_KEY` - Razorpay API Public Key

- `PRIVATE_KEY` - Razorpay API Private Key

![ENV file](docs/env.png)


### 💻 Run Locally

***Step#1 : Clone Project Repository***

```bash
git clone https://github.com/atharvparkhe/basic-e-shop.git && cd basic-e-shop
```

***Step#2 : Create Virtual Environment***

* If *virtualenv* is not istalled :
```bash
pip install virtualenv && virtualenv env
```
* **In Windows :**
```bash
env/Scripts/activate
```
* **In Linux or MacOS :**
```bash
source env/bin/activate
```

***Step#3 : Install Dependencies***

```bash
pip install --upgrade pip -r requirements.txt
```

***Step#4 : Add .env file***

- ENV file contents
    - **In Windows :**
    ```bash
        copy .env.example .env
    ```
    - **In Linux or MacOS :**
    ```bash
        cp .env.example .env
    ```
- Enter Your Credentials in the *".env"* file. Refer [Environment Variables](#-environment-variables)

***Step#5 : Run Server***

```bash
python manage.py runserver
```

- Open `http://127.0.0.1:8000/` or `http://localhost:8000/` on your browser.

*Check the terminal if any error.*


### 📄 Documentation

The docs folder contain all the project documentations and screenshots of the project.

**Local Server Base Link :** http://localhost:8000/

**Admin Pannel Access :**
- ***Email :*** "admin@admin.com"
- ***Password :*** "password"

**Admin Pannel :** *Django Jazzmin*

### 🌄 Screen-Shots

- **Authentication**
![Signup](docs/project/accounts/signup.png)
![Login](docs/project/accounts/login.png)
![Forgot](docs/project/accounts/forgot.png)

- **Product**
![All Products](docs/project/products/all-products.png)
![Single Products](docs/project/products/single-product.png)

- **Cart**
![Cart](docs/project/cart/cart.png)
![Address](docs/project/cart/address.png)
![Payment](docs/project/cart/payment.png)
![Payment Success](docs/project/cart/payment-success.png)
![Invoice](docs/project/cart/invoice.png)

- **Admin**
![Admin](docs/project/admin/dashboard.png)
![All Products](docs/project/admin/all-products.png)
![New Product](docs/project/admin/payment.png)
![New Category](docs/project/admin/new-category.png)
![Sale Coupons](docs/project/admin/sale-coupons.png)


### 🙋🏻‍♂️ Author

**🤝 Connect with Atharva Parkhe**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/atharvparkhe/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/atharvparkhe/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/atharvparkhe/)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/patharv777/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UChimOJO64hOqtE7HCgtiIig)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8WNC43Xsfc)
