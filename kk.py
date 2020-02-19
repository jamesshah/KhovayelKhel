from kk import app, dotenv_path, db
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    app.run(debug=True, port=5000)
