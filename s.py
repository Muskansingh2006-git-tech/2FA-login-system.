import secrets
import time
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "change-this-demo-secret-key"

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or len(password) < 8:
            flash("Username bharo aur password kam se kam 8 characters ka rakho.")
            return redirect(url_for("register"))

        conn = get_db()
        try:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, generate_password_hash(password))
            )
            conn.commit()
        except sqlite3.IntegrityError:
            flash("This username already registered.")
            conn.close()
            return redirect(url_for("register"))

        conn.close()
        flash("Registration successful!"
        "\nplz login\n.")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["pending_user"] = user["id"]
            return redirect(url_for("verify"))

        flash("Username or password are incorrect.")

    return render_template("login.html")


    
@app.route("/verify", methods=["GET", "POST"])
def verify():
    if "pending_user" not in session:
        return redirect(url_for("login"))

    # OTP expires after 120 seconds.
    if request.method == "GET":
        if "otp" not in session:
            session["otp"] = f"{secrets.randbelow(1000000):06d}"
            session["otp_expiry"] = time.time() + 120
            session["otp_attempts"] = 0
            print("DEMO OTP:", session["otp"])

    if request.method == "POST":
        otp = request.form.get("otp", "").strip()

        if time.time() > session.get("otp_expiry", 0):
            session.pop("otp", None)
            flash("OTP is expired. try again.")
            session.pop("pending_user", None)
            return redirect(url_for("login"))

        if session.get("otp_attempts", 0) >= 3:
            session.clear()
            flash("Maximum attempts reached. plz try again.")
            return redirect(url_for("login"))

        if secrets.compare_digest(otp, session.get("otp", "")):
            user_id = session.pop("pending_user")
            session.clear()
            session["user_id"] = user_id
            return redirect(url_for("dashboard"))

        session["otp_attempts"] = session.get("otp_attempts", 0) + 1
        flash("Incorrect OTP. Try again.")

    return render_template("verify.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
init_db()

if __name__ == "__main__":
    app.run(debug=True)
