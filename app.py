import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bedside.settings')

# Import Django WSGI application
from bedside.wsgi import application

# Make the application available as 'app' for Render
app = application
