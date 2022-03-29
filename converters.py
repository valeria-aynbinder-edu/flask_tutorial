from werkzeug.routing import BaseConverter, ValidationError
import re


class IPv4Converter(BaseConverter):
    def to_python(self, value):
        match = re.search(r'(\d+)\.(\d+)\.(\d+)\.(\d+)$', value)
        if not match:
            raise ValidationError()
        for i in range(1, 5):
            if not 0 <= int(match.group(i)) <= 255:
                raise ValidationError()
        return value