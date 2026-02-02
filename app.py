from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# --- 1. ENTRY POINT: WELCOME SCREEN ---
@app.route('/')
def home():
    # Loads the "Face ID" simulation
    return render_template('welcome.html')

# --- 2. SECOND SCREEN: UPLOAD PAGE ---
@app.route('/upload_page')
def upload_page():
    # Loads your "index.html" (The Drag & Drop UI)
    return render_template('index.html') 

# --- 3. TRANSITION: PROCESS UPLOAD ---
@app.route('/process_upload', methods=['POST'])
def process_upload():
    # ZOMBIE MODE: Redirect immediately to Dashboard
    return redirect(url_for('dashboard'))

# --- 4. FINAL SCREEN: DASHBOARD ---
@app.route('/dashboard')
def dashboard():
    # POLISHED DUMMY DATA (Makes the demo look real)
    fake_events = [
        {
            "event_time": "2023-10-12 14:30:05", 
            "event_type": "GPS", 
            "main_info": "Coords: 12.9757, 77.5971", 
            "extra_details": "Location: Cubbon Park (Suspicious Stop)"
        },
        {
            "event_time": "2023-10-12 14:32:10", 
            "event_type": "SMS", 
            "main_info": "Outgoing Message", 
            "extra_details": "To: +91 98XXX XXXXX (Content: 'Package secured')"
        },
        {
            "event_time": "2023-10-12 14:45:22", 
            "event_type": "CALL", 
            "main_info": "Missed Call", 
            "extra_details": "From: Unknown Number (Duration: 0s)"
        },
        {
            "event_time": "2023-10-12 15:00:00", 
            "event_type": "APP", 
            "main_info": "WhatsApp Launched", 
            "extra_details": "Foreground Activity"
        },
        {
            "event_time": "2023-10-12 15:10:45", 
            "event_type": "WIFI", 
            "main_info": "Connected to 'Public_Cafe'", 
            "extra_details": "IP: 192.168.1.105"
        }
    ]
    return render_template('dashboard.html', events=fake_events)

# --- FAKE API: AI ANALYSIS ---
@app.route('/analyze', methods=['POST'])
def analyze():
    return jsonify({
        "summary": "### FORENSIC AI SUMMARY\n\n**Status:** Analysis Complete.\n**Threat Level:** High.\n\n**Key Findings:**\n* **Timeline Correlation:** The suspect sent a confirmation SMS immediately after arriving at the GPS location.\n* **Suspicious Comms:** Multiple interactions with an unregistered number (+91 98XXX).\n* **Pattern:** Movement suggests a 'dead drop' operation near the park area.\n\n(Note: This is a cloud demo response generated for the hackathon)."
    })

# --- FAKE API: CHAT ---
@app.route('/chat_evidence', methods=['POST'])
def chat_evidence():
    return jsonify({
        "answer": "Based on the logs, the suspect was at Cubbon Park at 14:30. This correlates with the message 'Package secured' sent at 14:32."
    })

if __name__ == '__main__':
    # Running on 5001 to prevent AirPlay conflicts
    app.run(host='0.0.0.0', port=5001)