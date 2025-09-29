# Financial Literacy Web Application

This is a Flask-based web application designed to help first-time earners understand their salary breakdown, track expenses, and view savings insights.

## Features

- User Authentication (Register, Login, Logout) with Flask-Login
- User-specific Dashboard with navigation links (Salary, Expenses, Savings & Insights)
- Salary page with editable deduction rates and net salary computation
- Expense tracking with full CRUD (Create, Read, Update, Delete)
- Savings & Insights page showing savings calculation, spending breakdown, and fun confetti animation when savings are positive
- Calendar and clock widget displayed on the dashboard page
- Responsive UI with Bootstrap 5

## Project Structure


## Setup Instructions

1. **Clone the repository** (or copy the files)

2. **Create and activate a virtual environment:**  

3. **Install dependencies:**  

4. **Run the app:**  

The app will run locally at `http://localhost:5000`.

## Usage

- Register a new user account.
- Log in to access your personalized dashboard.
- Enter your gross salary and adjust deduction rates.
- Track your expenses with categories, descriptions, and dates.
- View savings insights with helpful analytics and encouragement.

## Notes

- The SQLite database file (`app.db`) is auto-created on the first run.
- Bootstrap 5 and canvas-confetti are loaded via CDN.
- To stop the server, press `Ctrl+C` in the terminal.

---

Developed as a learning project to improve financial literacy using Flask and Python!

