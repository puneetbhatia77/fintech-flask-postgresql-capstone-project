from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from pathlib import Path
import sys

# Add scripts/ folder to sys.path so we can import init_db
sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
load_dotenv()

# SINGLE shared db instance
db = SQLAlchemy()

# ✅ NEW: Import and call init_db
from init_db import init_db

def create_app():
    app = Flask(__name__)

    # ✅ Ensure this is called during startup
    try:
        print("🚀 Calling init_db() from create_app()")
        init_db()
    except Exception as e:
        print("❌ DB init failed:", e)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind db to app
    db.init_app(app)

    from api.routes import auth, loan
    app.register_blueprint(auth.bp)
    app.register_blueprint(loan.bp)

    @app.route("/")
    def index():
        return "API is running and DB initialized!"

    return app


# --------------------------------------------------------------------------------------
#$env:FLASK_APP="api"  
#$env:FLASK_RUN_HOST="127.0.0.1"    
#$env:FLASK_ENV="development"   
#flask run

# uncomment below code if you want to test the Flask app directly by running above commands

#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#from api.routes import auth, loan
#app.register_blueprint(auth.bp)
#app.register_blueprint(loan.bp)


#if __name__ == "__main__":
#    app = create_app()
#    app.run(debug=True, use_reloader=False)