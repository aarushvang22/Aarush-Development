## 📌 Project Context

I'm working on a **minimal weather application** to practice full-stack development using Flask. The app will fetch and display real-time weather data using the [WeatherAPI.com](https://www.weatherapi.com/) service.

### 🛠️ Tech Stack

- **Frontend**: Basic HTML and CSS (no frameworks)
- **Backend**: Python with Flask
- **API Source**: [weatherapi.com](https://www.weatherapi.com/)
- **Goal**: Simple and clean user interface with only essential weather data.

---

## 🧩 Problem Statement

I want the user to enter a **city name**, and the app should:

1. Make a **GET request** to the WeatherAPI endpoint using Flask.
2. Parse the **current weather data** (like temperature, condition, humidity, wind speed).
3. Render it cleanly on a minimal HTML page using Flask templates.
4. Provide basic error handling (e.g., invalid city, empty input, API errors).

I'm aiming to keep everything **lightweight** and avoid external JS frameworks, frontend libraries, or complex templating engines.

---

## ❓ Question

What are the **best practices and recommendations** for building this project with the following in mind:

1. **Flask App Structure**:
   - How should I organize the routes, templates, and static files?
   - Should I use Blueprints even for small apps?

2. **API Integration**:
   - What’s the cleanest way to make the HTTP request to WeatherAPI within Flask?
   - How can I **securely manage the API key**, especially if I plan to host this later?

3. **Frontend Design**:
   - How can I keep the CSS responsive and minimal without using Bootstrap or Tailwind?
   - Suggestions for clean layout patterns for showing weather data?

4. **Error Handling**:
   - How can I gracefully show errors to the user if the API fails or the input is invalid?
   - Should I return to the same form with error messages or redirect?

5. **Optional Features**:
   - What are some small yet useful features I can add without breaking minimalism? (e.g., loading animation, location-based weather using IP)

---

## 📁 Folder Structure
```
weather-app/
├── backend/
│   ├── app.py               # Main Flask app
│   ├── config.py            # API key and config variables
│   └── weather_service.py   # Logic for calling WeatherAPI and handling responses
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Minimal styling
│   │   └── images/          # (Optional) Weather icons or assets
│   │
│   └── templates/
│       ├── index.html       # Home page with form
│       ├── result.html      # Weather results page
│       └── error.html       # Display API errors or invalid city
│
├── .env                     # Store your WeatherAPI key here (use python-dotenv)
├── .gitignore               # Exclude .env, __pycache__, etc.
├── README.md                # Project description
├── requirements.txt         # Flask, requests, python-dotenv

```

---
