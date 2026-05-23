<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,100:10B981&height=250&section=header&text=KrishiNode%20AI&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Protecting%20Crops%20With%20Real-Time%20AI&descAlignY=55&descSize=22" width="100%" alt="KrishiNode AI Header" />

<br/>
<a href="https://krishinode-ai.vercel.app/">
  <img src="https://readme-typing-svg.herokuapp.com?font=Plus+Jakarta+Sans&weight=600&size=24&pause=1000&color=10B981&center=true&vCenter=true&width=800&lines=🌱+Smart+AI+for+Healthier+Farms;🚜+Stop+Crop+Waste+Before+It+Starts;⚡+Real-Time+Alerts+for+Farmers;🌍+Securing+Our+Food+Supply" alt="Typing SVG" />
</a>

<p align="center">
  <strong>If a website crashes, we fix it in minutes. If a farm fails, we lose our food. It's time to protect what matters most.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq_AI-F56565?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Datadog_Ready-632CA6?style=for-the-badge&logo=datadog&logoColor=white" />
</p>

<p align="center">
  <a href="https://krishinode-ai.vercel.app/">
    <img src="https://img.shields.io/badge/🌍_View_Live_Deployment-10B981?style=for-the-badge" alt="Live Deployment"/>
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="YOUR_YOUTUBE_DEMO_LINK_HERE">
    <img src="https://img.shields.io/badge/🎥_Watch_Demo_Video-050505?style=for-the-badge" alt="Demo Video"/>
  </a>
</p>

</div>

---

## 📖 The Story: Why We Built KrishiNode

Imagine waking up to find that a whole season of hard work on the farm is ruined because a water pipe broke overnight, or a sudden disease wiped out a crop before anyone noticed. 

In the tech world, software engineers never wait to find out if a website goes down. They have powerful dashboards that monitor everything 24/7. The moment something breaks, an alarm goes off on their phone, and they fix it immediately. 

**But what about our farmers?** The people who grow the food we eat every single day often find out about a problem when it is already too late. 

That is why we built **KrishiNode AI**. It acts as a 24/7 digital guardian for farms. It tracks the health of the farm—like soil moisture, weather changes, and equipment status—in real-time. If water levels drop dangerously low or a sensor detects a failing pump, our AI instantly catches the error, diagnoses the problem, and tells the farmer exactly what to do to save the crop. **We are stopping food waste before it even happens.**

---

## ✨ Key Features

* 📡 **Live Dashboard:** Watch the heartbeat of the farm in real-time.
* ⚡ **One-Click AI Diagnosis:** When a warning light flashes, one click tells our AI to figure out exactly what broke and how to fix it immediately.
* 🌙 **Night-Shift Ready (Dark Mode):** A beautiful, high-contrast dark theme designed for easy reading, day or night.
* 🔌 **Enterprise-Grade Monitoring:** Built to seamlessly connect with professional tools used by top tech companies.

---

## 📸 Sneak Peek

> **Note:** *Click the image below to watch how KrishiNode responds to a live farm outage in milliseconds.*

<div align="center">
  <img src="https://via.placeholder.com/800x450/050505/10B981?text=+Drop+Your+Animated+App+GIF+Here+" alt="KrishiNode Demo UI" style="border-radius: 10px; box-shadow: 0 4px 14px 0 rgba(0,0,0,0.5);"/>
</div>

---

## 🔌 Connecting to Enterprise Monitoring (Datadog, Grafana, New Relic)

KrishiNode isn't just a standalone web app; it is built to be the "AI Brain" that plugs directly into existing, powerful monitoring ecosystems. Here is how you connect it:

1. **The IoT Sensors (The Eyes):** Physical farm sensors (soil moisture, temperature, pump pressure) send their raw data using protocols like MQTT or HTTP.
2. **The Dashboard (The Hub):** You route this sensor data directly into **Datadog, Grafana, or New Relic**. These tools are incredible at graphing data and spotting when numbers drop below normal levels.
3. **The Webhook (The Trigger):** You set up an "Alert" in Datadog/Grafana. *Rule: If soil moisture drops below 20%, trigger an alert.*
4. **The KrishiNode Connection (The Brain):** You configure that alert to send a **Webhook POST Request** directly to your KrishiNode API endpoint (e.g., `https://krishinode-ai.vercel.app/api/simulate`).
5. **The Magic:** As soon as Datadog detects the farm issue, it pings KrishiNode. KrishiNode's Groq-powered AI instantly reads the alert, generates a human-readable emergency repair plan, and displays it on the KrishiNode interface for the farmer.

---

## 🛠️ Built With

* **Frontend:** HTML5, Tailwind CSS, Javascript (Vanilla)
* **Backend:** Python, Flask
* **AI Engine:** Groq Cloud API for ultra-fast, zero-latency inference.

---

## 💻 Run it Locally

Want to test the platform yourself? 

```bash
# 1. Clone the repository
git clone [https://github.com/krishnayankashyap-hub/krishinode-ai.git](https://github.com/krishnayankashyap-hub/krishinode-ai.git)
cd krishinode-ai

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up Environment Variables
# Create a .env file in the root directory and add:
GROQ_API_KEY=your_api_key_here

# 5. Run the application
python api.py
