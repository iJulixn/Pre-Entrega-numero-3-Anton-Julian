from django.db import models

class motorv8 (models.Model):
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    año = models.IntegerField()
    potencia = models.IntegerField()

    def __str__(self):
        return f"{self.marca} V8 {self.cilindrada} ({self.año})"

class motorv6 (models.Model):
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    año = models.IntegerField()
    potencia = models.IntegerField()

    def __str__(self):
        return f"{self.marca} V6 {self.cilindrada} ({self.año})"

class motori4 (models.Model):
    cilindrada = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    año = models.IntegerField()
    potencia = models.IntegerField()

    def __str__(self):
        return f"{self.marca} I4 {self.cilindrada} ({self.año})"
