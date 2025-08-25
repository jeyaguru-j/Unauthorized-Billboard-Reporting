# Unauthorized-Billboard-Reporting

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-Framework-black)](https://flask.palletsprojects.com/)  
[![Leaflet](https://img.shields.io/badge/Leaflet-Maps-brightgreen)](https://leafletjs.com/)  
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)](https://www.sqlite.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

A Flask-based web app that lets citizens report unauthorized billboards by uploading images with auto-fetched GPS coordinates. Features a modern UI, live image preview, and a dashboard to track all reports.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Workflow](#workflow)
- [Results](#results)
- [Future Scope](#future-scope)
- [Author](#author)
- [License](#license)

---

## About the Project

Unauthorized billboards clutter cities, block visibility, and violate regulations. This project provides a citizen-friendly reporting platform where users can:
- Upload billboard images.
- Automatically capture latitude & longitude via geolocation.
- View all reports on an interactive map with heatmap layers.
- Track reported cases in a modern, styled dashboard.
- This system was built as part of the TechNova Hackathon 2025.

---

## Tech Stack

- **Language:** Python 3.13
- **Backend Framework:** Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Mapping & Visualization:** Leaflet.js + Heatmap.js
- **Database:** SQLite (via SQLAlchemy ORM)
- **Deployment Ready:** Can run locally or on any Flask-supported server

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/unauthorized-billboard-reporting.git
   cd unauthorized-billboard-reporting

2. **Create Virtual Environment & Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt

3. **Run the Application**
   ```bash
   flask run

4. **Access in Browser**
   - Homepage → http://127.0.0.1:5000
   - Upload Report → http://127.0.0.1:5000/upload
   - Dashboard → http://127.0.0.1:5000/dashboard

---

## Workflow

1. **User opens Upload Page**
   - Enters details & uploads billboard image.
   - Latitude & Longitude auto-fetched via geolocation.
2. **Report stored in the database**
3. **Dashboard View**
   - Tabular list of reports (user, violation type, coordinates, image).
   - Interactive map showing exact billboard locations.
   - Heatmap highlights high-density violation zones.

---

## Results

- Simple & fast citizen reporting interface.
- Accurate geo-tagged violation reports.
- Dashboard with clean visualization for authorities.

**Homepage**
<img width="942" height="675" alt="image" src="https://github.com/user-attachments/assets/34f66ef9-7746-49ba-91f6-4d5d74be6ea0" />

**Upload Report**
<img width="615" height="879" alt="image" src="https://github.com/user-attachments/assets/027d5d70-fac4-4d9c-9e37-a1f5c6fa2270" />

**Dashboard**
<img width="1010" height="908" alt="image" src="https://github.com/user-attachments/assets/81268b0c-398c-4745-b831-96f42d54f8ef" />

---

## Future Scope

- Add Admin Approval / Rejection workflow
- SMS/Email alerts to city officials
- Predictive analytics to find emerging billboard hotspots
- Integration with city regulatory APIs for automated removal notices
- Mobile app support (React Native / Flutter)

---

## Author

Jeyaguru J

B.Tech Artificial Intelligence and Data Science

Email: jeyaguru1507@gmail.com

Hackathon Project – TechNova 2025

---

## License

This project is licensed under the MIT License
