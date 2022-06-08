from django.forms import ValidationError

#funcion para establecer un maximo tamaño
class MaxSizeFileValidator(object):
    def __init__(self, max_file_size = 10):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        max_size = self.max_file_size * 1048576 #convertimos a bytes

        if size > max_size:
            raise ValidationError(f"El tamaño máximo del archivo deber ser de {self.max_file_size}MB")
        
        return value

#clase