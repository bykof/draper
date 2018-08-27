from flask import (
    Blueprint,
)


class ModelBlueprintFactory(Blueprint):
    def __init__(self, model):
        super(ModelBlueprintFactory, self).__init__(model.underscore_name, __name__)
        self.model = model
        self.add_url_rule('/', view_func=self.list, methods=['GET'])
        self.add_url_rule('/<int:object_id>', view_func=self.get, methods=['GET'])
        self.add_url_rule('/<int:object_id>', view_func=self.update, methods=['POST'])
        self.add_url_rule('<int:object_id>', view_func=self.delete, methods=['DELETE'])

    def get(self, object_id):
        return str(object_id)

    def list(self):
        return f'This is the list route for: {self.model.__name__}'

    def update(self, object_id):
        pass

    def delete(self, object_id):
        pass
