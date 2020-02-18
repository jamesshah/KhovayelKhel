from kk import app, dotenv_path
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG'), port=os.getenv('PORT'))
