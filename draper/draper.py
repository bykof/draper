import sys
import os
import importlib.util
import inspect
from typing import Type

from mongoengine import connect

from flask import Flask

from draper.model import Model
from draper.flask_blueprints.model_blueprint_factory import ModelBlueprintFactory
from draper.settings import Settings
from draper.utils import camelcase_to_underscore


class Draper:
    MODELS = 'models'

    def __init__(self):
        self.models: [Type[Model]] = []
        self.blueprints = {}
        self.settings = None
        self.flask_app = Flask(__name__)

    @property
    def current_main_file(self):
        return os.path.abspath(sys.argv[0])

    @property
    def current_project_directory(self):
        return os.path.dirname(self.current_main_file)

    def add_model(self, model: Type[Model]):
        self.flask_app.register_blueprint(
            ModelBlueprintFactory(model),
            url_prefix=f'/{camelcase_to_underscore(model.__name__)}s'
        )
        self.models.append(model)

    def scan_for_models(self):
        models_path = os.path.join(self.current_project_directory, 'models', '__init__.py')
        spec = importlib.util.spec_from_file_location('models', location=models_path)
        models = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(models)

        for model in models.__dict__.values():
            if inspect.isclass(model) and issubclass(model, Model):
                self.add_model(model)
                print(f'{model} is loaded...')

    def scan_for_settings(self):
        models_path = os.path.join(self.current_project_directory, 'settings.py')
        spec = importlib.util.spec_from_file_location('settings', location=models_path)
        settings = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(settings)

        parsed_settings = {
            key: value
            for key, value in settings.__dict__.items()
            if not key.startswith('__')
        }
        self.settings = Settings(**parsed_settings)

    def init_database(self):
        connect(self.settings.DATABASE_NAME)

    def start(self):
        self.scan_for_settings()
        self.init_database()
        print(f'Draper started at {self.current_project_directory}...')
        self.scan_for_models()
        #  self.flask_app.run()


draper = Draper()
