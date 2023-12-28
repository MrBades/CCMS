from django.core.exceptions import ValidationError

def file_size(value):
    filesize = value.size
    if filesize > 5e+6:
      raise ValidationError("maximum size 100mb")