from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

# If you're trying to send a request from one origin (e.g., Postman) to a different origin (localhost),
# make sure the server's CORS policy allows this.
# Cross-Origin Resource Sharing (CORS)
app = Flask(__name__)
CORS(app)   # Enable CORS for all routes

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getsensordata', methods = ['GET', 'POST'])
def sensor_data():
    # Ensure the request contains JSON data
    if request.is_json:
        data = request.get_json()  # Parse the incoming JSON data
        sensor_type = data.get('sensor_type')  # Get sensor type from the JSON
        sensor_value = data.get('sensor_value')  # Get sensor value from the JSON
        # Process the sensor data here (e.g., log it, send to a database, etc.)
        response = {
            "message": f"Received {sensor_type} data: {sensor_value}"
        }

        # Return a JSON response to acknowledge the request
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid data format. Please send JSON."}), 400


                                # @app.route('/submit', methods=['POST'])
                                # def submit_data():
                                #     if request.method == 'POST':
                                #         sensor_type = request.form['sensor_type']
                                #         sensor_value = request.form['sensor_value']
                                #         # You can process or store the sensor data here
                                #         return f"Received {sensor_type} data: {sensor_value}"
    
if __name__ == '__main__':
    app.run(debug=True)