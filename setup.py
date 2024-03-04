import os
from dotenv import load_dotenv

env_file = '.env.production' if os.getenv('FLASK_ENV') == 'production' else '.env.development'
load_dotenv(env_file)
