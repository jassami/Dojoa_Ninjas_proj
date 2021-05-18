from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    state = models.CharField(max_length= 255)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # ninjas = list of ninjas associated with a given dojo

    def __str__(self):
        return '{}'.format(self.name)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete= models.CASCADE)
    first_name= models.CharField(max_length= 255)
    last_name= models.CharField(max_length= 255)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


