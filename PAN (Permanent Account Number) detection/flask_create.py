import os
import click

@click.command()
@click.argument('project_name')
def create_flask_project(project_name):
    dirs = [
        f'{project_name}/app',
        f'{project_name}/app/templates',
        f'{project_name}/app/static',
        f'{project_name}/sample_data',
        f'{project_name}/__pycache__'
    ]
    files = {
        f'{project_name}/app/__init__.py': """from flask import Flask\n\napp = Flask(__name__)\n\nfrom app import routes\n""",
        f'{project_name}/app/routes.py': """from app import app\n\n@app.route('/')\ndef home():\n    return "Hello, Flask!"\n""",
        f'{project_name}/config.py': """import os\n\nclass Config:\n    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'\n""",
        f'{project_name}/requirements.txt': "Flask\n",
        f'{project_name}/readme.md': "# Flask App\nThis is a simple Flask application.\n",
        f'{project_name}/run.py': """from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"""
    }

    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

    for file, content in files.items():
        with open(file, 'w') as f:
            f.write(content)

    click.echo(f'Flask project {project_name} created successfully.')

if __name__ == '__main__':
    create_flask_project()
