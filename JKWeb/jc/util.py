from django.db import models
import json
def format1(pe):
    te = str(pe).decode(encoding='raw_unicode_escape').encode('utf-8').replace('u','')
    return te
def format2(pt):
    te=str(pt).decode(encoding='raw_unicode_escape')
    return te

class JsonField(models.TextField):
    def to_python(self, value):
        v = models.TextField.to_python(self, value)
        try:
            return json.loads(v)['v']
        except:
            pass
        return v
    def get_prep_value(self, value):
        return json.dumps({'v': value})
