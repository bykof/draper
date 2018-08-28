

class ObjectSet:
    def __init__(self, model_class):
        self.model_class = model_class

    def _results_to_objects(self, results):
        object_list = []

        for result in results:
            object_list.append(self.model_class(**result))
        return object_list

    def get(self, object_id):
        result = self.model_class.table.get(object_id).run()
        return self._results_to_objects([result])

    def list(self, **kwargs):
        results = self.model_class.table.filter(kwargs).run()
        return self._results_to_objects(results)
