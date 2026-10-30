# 🔐 Secure Login System with Two-Factor Authentication (2FA)

## 📌 About the Project

This project is a web-based Secure Login System developed using Python and Flask. It provides an additional layer of security through Two-Factor Authentication (2FA).

Users must first enter their username and password, followed by a 6-digit OTP to access their dashboard.

## ✨ Features

- User Registration
- Secure Password Hashing
- User Login Authentication
- 6-Digit OTP Verification
- OTP Expiry (120 Seconds)
- Maximum 5 OTP Attempts
- Protected Dashboard
- Logout Functionality
- SQLite Database Integration

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- SQLite
- Werkzeug Security

## 📂 Project Structure

```text
secure-login-2fa/
│
├── app.py
├── users.db
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── verify.html
│   └── dashboard.html
│
└── README.md
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd secure-login-2fa
```

3. Install Flask:

```bash
py -m pip install flask
```

4. Run the application:

```bash
py app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔑 How It Works

1. Register using a username and password.
2. Login using your registered credentials.
3. A 6-digit OTP is generated and displayed in the terminal.
4. Enter the OTP on the verification page.
5. After successful verification, access the dashboard.
6. Logout securely from your account.

## 🎯 Project Objective

The main objective of this project is to demonstrate how Two-Factor Authentication can improve login security by adding an extra verification step.

## ⚠️ Security Note

This is an educational demonstration project. The OTP is displayed in the development terminal and the session configuration should be improved before production use. It is not intended for production deployment.

## 👩‍💻 Author

**Muskan**

## 📜 License

This project is open-source and available for educational purposes.
