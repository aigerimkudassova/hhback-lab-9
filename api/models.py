from django.db import models

class Company(models.Model):

   name = models.CharField(max_length=200)
   description = models.TextField(default='')
   city = models.CharField(max_length=200)
   address = models.TextField(default='')

   def str(self):
       return self.name + " " + self.city

   def company_to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):

   name = models.CharField(max_length=200)
   description = models.TextField(default='')
   salary = models.IntegerField()
   company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

   def vacancy_to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            # 'company': str(self.company)
        }


# from django.db import models
#
#
# class Company(models.Model):
#    name = models.CharField(max_length=200)
#    description = models.TextField(default='')
#    city = models.CharField(max_length=200)
#    address = models.TextField(default='')
#
#    def to_json(self):
#       return{
#          'id': self.id,
#          'name': self.name,
#          'description': self.description,
#          'city': self.city,
#          'address': self.address
#       }
#
#
# class Vacancy(models.Model):
#    name = models.CharField(max_length=200)
#    description = models.TextField(default='')
#    salary = models.IntegerField
#    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
#
#    def vacancy_to_json(self):
#       return {
#          'id': self.id,
#          'name': self.name,
#          'description': self.description,
#          'salary': self.salary,
#          'company': self.company.to_json()
#       }