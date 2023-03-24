from django.db import models

# Create your models here.
class Department(models.Model):
    """Department Table"""
    title = models.CharField(verbose_name='Title', max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """Employees Table"""
    name = models.CharField(verbose_name='Name', max_length=16)
    password = models.CharField(verbose_name='Password', max_length=64)
    age = models.IntegerField(verbose_name='Age')
    balance = models.DecimalField(verbose_name='Balance', max_digits=10, decimal_places=2, default=0)
    entry_time = models.DateField(verbose_name='Entry Time')
    # Create restrictions for the department ID where each employee belongs to
    # -to assigns which table to connect
    # -to field assign which column to connect
    # If one ID in the department table is deleted, all employees in the userinfo table will be deleted too
    depart = models.ForeignKey(verbose_name='Department', to='Department', to_field="id", on_delete=models.CASCADE)
    # all employees in the userinfo table will be set to none
    # depart = models.ForeignKey(to='Department', to_field="id", null=True, blandk=True, on_delete=models.SET_NULL)

    # The restriction in Django
    gender_choices = ((1, "Male"), (2, "Female"))
    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_choices)

class AccountAdmin(models.Model):
    # If null value is permitted, add attribute (null = True, blank = True)
    mobile = models.CharField(verbose_name='Mobile', max_length=11)
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2, default=0)
    level_choices = ((1, "Used"), (2, "Used With Good Condition"), (3, "Like New"), (4, "Brand New"))
    level = models.SmallIntegerField(verbose_name='Level', choices=level_choices)
    status_choices = ((1, "Occupied"), (2, "Available"))
    status = models.SmallIntegerField(verbose_name='Status', choices=status_choices, default=2)

class Admin(models.Model):
    """Administrator Info"""
    username = models.CharField(verbose_name="UserName", max_length=32)
    password = models.CharField(verbose_name="PassWord", max_length=32)

    def __str__(self):
        return self.username

class Task(models.Model):
    """Create Task Table"""
    level_choices = (
        (1, "Urgent"),
        (2, "Important"),
        (3, "Temporary"),
    )
    level = models.SmallIntegerField(verbose_name="level", choices=level_choices, default=3)
    title = models.CharField(verbose_name="title", max_length=64)
    detail = models.TextField(verbose_name="detail")
    user = models.ForeignKey(verbose_name="principal", to="Admin", on_delete=models.CASCADE)



class Order(models.Model):
    """Order Data Table"""
    oid = models.CharField(verbose_name="OrderNumber", max_length=64)
    title = models.CharField(verbose_name="Title", max_length=32)
    price = models.IntegerField(verbose_name="Price")

    status_choices = (
        (1, "Pending"),
        (2, "Finished"),
    )

    status  = models.SmallIntegerField(verbose_name="Status", choices=status_choices, default=1)

    admin = models.ForeignKey(verbose_name="Administrator", to="Admin", on_delete=models.CASCADE)




class Boss(models.Model):
    name = models.CharField(verbose_name="name", max_length=32)
    age = models.IntegerField(verbose_name="age")
    img = models.CharField(verbose_name="photo", max_length=128)




class City(models.Model):
    name = models.CharField(verbose_name="name", max_length=32)
    population = models.IntegerField(verbose_name="population")
    # Actually filefield is also charfield, but it can save files automatically
    img = models.FileField(verbose_name="logo", max_length=128, upload_to='city/')





