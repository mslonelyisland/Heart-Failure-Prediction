from django.db import models

# Create your models here.
class HeartPrediction(models.Model):
    age = models.FloatField() #columns and the data type
    anemia = models.IntegerField()
    creatinine_phosphokinase = models.IntegerField()
    diabetes = models.IntegerField()
    ejection_fraction = models.IntegerField()
    high_blood_pressure = models.IntegerField()
    platelets = models.FloatField()
    serum_creatinin = models.FloatField()
    serum_sodium = models.IntegerField()
    sex = models.IntegerField()
    smoking = models.IntegerField()
    time = models.IntegerField()
    predicted_death_event = models.IntegerField()

    #create db table
    class Meta:
        db_table = 'prediction'