import os


if '/Users/rizquuula/Desktop/geox' == os.getcwd():
    SERVER_HOST = 'http://localhost:8000'
else:
    SERVER_HOST = 'https://api.geoxdat.com'