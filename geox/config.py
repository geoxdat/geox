import os

if os.getenv('MODE') == 'development':
    SERVER_HOST = 'http://localhost:8000'
else:
    SERVER_HOST = 'https://api.geoxdat.com'