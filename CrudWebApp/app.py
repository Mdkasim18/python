from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB_NAME = "students.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # so we can use column names
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    email = request.form.get("email")

    if name and email:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO students (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        conn.close()

    return redirect("/")


@app.route("/edit/<int:id>")
def edit(id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()
    if student is None:
        return redirect("/")
    return render_template("edit.html", student=student)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form.get("name")
    email = request.form.get("email")

    conn = get_db_connection()
    conn.execute(
        "UPDATE students SET name = ?, email = ? WHERE id = ?",
        (name, email, id)
    )
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
