from draper.db.fields import Field


class StringField(Field):

    def is_valid(self):
        return isinstance(value, str)

    def to_python(self):
    	return str(self.value)

class IntegerField(Field):

	def is_valid(self):
		return isinstance(value,int)

	def to_python(self):
		return int(self.value)