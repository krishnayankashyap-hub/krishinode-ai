import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)


nodes_data = [
    {"id": "node_1", "name": "Rural Soil Sensor", "type": "Farmer Tools", "status": "Online", "log": "Ping OK. Soil moisture 45%."},
    {"id": "node_2", "name": "Smart Irrigation Valve", "type": "Farmer Tools", "status": "Online", "log": "Flow rate nominal. 12 L/min."},
    {"id": "node_3", "name": "Harvest Drone Feed", "type": "Surveillance", "status": "Online", "log": "Flight path locked. Battery 88%."},
    {"id": "node_4", "name": "Transport Truck (Highway)", "type": "Logistics", "status": "Online", "log": "GPS active. Refer temp 4°C."},
    {"id": "node_5", "name": "City Cold Storage", "type": "B2B Warehouse", "status": "Online", "log": "API Active. Ambient temp 2°C."},
    {"id": "node_6", "name": "Sorting Conveyor", "type": "Processing", "status": "Online", "log": "Motor temp 42°C. Speed OK."},
    {"id": "node_7", "name": "Retail Smart Shelf", "type": "Consumer/Grocery", "status": "Online", "log": "Weight sensors active. Stock 80%."},
    {"id": "node_8", "name": "Last-Mile Delivery Bike", "type": "Consumer/Delivery", "status": "Online", "log": "App connected. Location updating."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    return jsonify(nodes_data)


@app.route('/api/webhook', methods=['POST'])
def handle_real_webhook():

    
    return jsonify({"status": "Webhook received from Datadog/IoT interface. Awaiting AI processing."}), 200

@app.route('/api/simulate', methods=['POST'])
def process_incident():
    data = request.json
    node_id = data.get('node_id')
    node_name = data.get('node_name')
    node_type = data.get('node_type')

    system_error = ""
    if "Farmer" in node_type: system_error = "Error 408: Ground Node Timeout."
    elif "Logistics" in node_type or "Delivery" in node_type: system_error = "Error 503: GPS/Telemetry Lost."
    elif "Grocery" in node_type: system_error = "Error 404: Inventory Sync Failed."
    else: system_error = "Error 500: Datadog Alert - API Unresponsive."

    prompt = f"""
    You are an AI SRE Incident Analyzer for a global food supply chain. 
    Node '{node_name}' ({node_type}) failed with error: '{system_error}'.
    Cross-reference with hypothetical external data (weather, traffic, grid).
    
    Respond ONLY in JSON format:
    "cause": A 1-sentence physical root cause (e.g., storm, traffic, power outage).
    "impact": A 1-sentence explanation of who suffers (farmer loss, consumer food spoilage).
    "action": A 1-sentence specific physical action to fix it.
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            response_format={"type": "json_object"}
        )
        ai_response = json.loads(chat_completion.choices[0].message.content)
    except Exception:
        ai_response = {"cause": "AI Offline", "impact": "Unknown", "action": "Check API"}

    return jsonify({
        "system_error": system_error, 
        "cause": ai_response.get("cause"),
        "impact": ai_response.get("impact"),
        "action": ai_response.get("action")
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
