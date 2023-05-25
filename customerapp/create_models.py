from django.db import models
from django.forms import CharField

class ColorCodeField(models.CharField):
    description = "A color code in the format #RRGGBB"
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': CharField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
