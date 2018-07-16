from django.contrib.auth import get_user_model
from django.db import models

from core.models import TimeStampedModel

User = get_user_model()

MEDICINE_TYPE = (
    ('', ''),
    (1, 'Analgésico'),
    (2, 'Antidepresivos'),
    (3, 'Hormonas'),
    (4, 'Antibioticos'),
)

class Medicine(TimeStampedModel):
    name = models.CharField('Nombre', max_length=255)
    description = models.TextField('Descripción', blank=True)
    fantasy_name = models.CharField('NOmbre de fantasia', max_length=255, blank=True)
    type_medicine = models.CharField(
        max_length=255, verbose_name='tipo de medicina', choices=MEDICINE_TYPE,  blank=True)

    def __str__(self):
        return self.name

class Exam(TimeStampedModel):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField('codigo examen', max_length=255)
    name = models.CharField('Nombre examen', max_length=255)
    description = models.TextField('Descripción examen', blank=True)

    def __str__(self):
        return "{}-{}".format(self.patient, self.code)

class MedicalRecord(TimeStampedModel):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    height =  models.FloatField('Altura', null=True, blank=True)
    weight = models.IntegerField(verbose_name='Peso')
    observations = models.TextField('observaciones', blank=True)
    exams = models.ManyToManyField(Exam, blank=True )
    medicines = models.ManyToManyField(Medicine, blank=True)
