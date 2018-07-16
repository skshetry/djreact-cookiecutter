import pathlib
ROOT_DIR = pathlib.Path(__file__).parents[3] # is 3 level deep
# .
# |
# ├── backend
BACKEND_DIR = ROOT_DIR / 'backend'
# │   ├── manage.py
# │   ├── notes
# │   ├── requirements
# │   ├── requirements.txt
# │   ├── sambad
PROJECT_DIR =  BACKEND_DIR / '{{cookiecutter.project_name}}'
# |   |  ├── media
MEDIA_DIR = PROJECT_DIR / 'media'
# |   |  ├── settings
SETTINGS_DIR = PROJECT_DIR / 'settings'
# |   |  ├── templates
TEMPLATE_DIR = PROJECT_DIR / 'templates'
# │   ├── utils
# |   └── *all apps here*
# └── frontend
FRONTEND_DIR = ROOT_DIR / 'frontend'
#     ├── config
#     ├── public
#     ├── scripts
#     └── src
