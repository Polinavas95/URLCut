import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates/")
print(TEMPLATES_DIR)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)
print(STATICFILES_DIRS)