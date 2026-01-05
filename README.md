# EcoFlow Monitor for Sway/Waybar 🔋🛰️

A mission-critical power monitoring utility for **EcoFlow Power Stations**, specifically engineered for Linux environments (SwayWM/Wayland).

## 🌍 Context: Engineering Under Pressure
This project was born out of necessity during the energy crisis in Ukraine. When official software is unavailable for Linux, and continuous power is vital for remote work during blackouts, I developed this tool to bridge the gap between IoT hardware and the Linux desktop.

## 🚀 Key Features
- **Official API Integration**: Securely fetches data via HMAC-SHA256 signing.
- **Real-time Visualization**: SoC (Charge %), PV Input (Solar), and Home Load in your status bar.
- **Resilience**: Designed to run as a lightweight background process with minimal resource impact.
- **Customizable**: Dynamic CSS classes for different battery states (Normal/Warning/Critical).

## 🛠 Tech Stack
- **Python 3.10+** (Requests, HMAC, Secrets)
- **Wayland / SwayWM / Waybar**
- **Systemd Integration**

## 📦 Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file with your `ECOFLOW_ACCESS_KEY`, `ECOFLOW_SECRET_KEY`, and `SN`.
4. Add the script to your Waybar configuration.

---
*Developed by a System Engineer with 30+ years of experience in making things work.*
