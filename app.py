import os
import importlib
import threading
import requests
import time
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Automatically register all blueprints from the 'blueprints' folder
def register_blueprints(app):
    blueprints_dir = os.path.join(os.path.dirname(__file__), 'blueprints')

    for filename in os.listdir(blueprints_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"blueprints.{filename[:-3]}"
            module = importlib.import_module(module_name)
            blueprint = getattr(module, f"{filename[:-3]}_blueprint")
            app.register_blueprint(blueprint)

register_blueprints(app)

# Serve JavaScript files from 'scripts' folder
@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory('scripts', filename)

# Serve static files (CSS, images, etc.) from 'static' folder
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Custom 404 Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Keep-Alive route
@app.route('/keep_alive')
def keep_alive():
    return "I'm alive!", 200

# Function to periodically ping the Keep-Alive route
def keep_alive_task():
    while True:
        try:
            # Send a GET request to the keep_alive route
            requests.get('https://nekotools.onrender.com/keep_alive')
            print("Keep-alive ping sent.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send keep-alive ping: {e}")
        
        # Sleep for 20 minutes (1200 seconds)
        time.sleep(1200)

# Start the keep-alive thread when the Flask app starts
if __name__ == "__main__":
    threading.Thread(target=keep_alive_task, daemon=True).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
