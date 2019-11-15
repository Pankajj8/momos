from django.db import models

# Create your models here.


class Project(models.Model):
    Pid = models.AutoField(primary_key=True)
    Pname = models.CharField(max_length=500)
    Pdescription = models.CharField(max_length=3000)
    Cname = models.CharField(max_length=300)
    Cdetails = models.CharField(max_length=4000)
    Pdeadline = models.CharField(max_length=100)
    Pstartdate = models.CharField(max_length=100)
    Pmanagedby = models.CharField(max_length=400)
    Pcontract = models.CharField(max_length=2000)
    Ptextresource = models.CharField(max_length=6000)
    Pimage1=models.ImageField(upload_to="media")
    Pimage2  = models.ImageField(upload_to="media")
    Pimage3 =models.ImageField(upload_to="media")
    Pstatus  = models.IntegerField()

    class Meta:
        db_table="project"


    def __str__(self):
        return str(self.Pid)+"  "+self.Pname



class Task(models.Model):
    Tid = models.AutoField(primary_key=True)
    Ttitle = models.CharField(max_length=3000)
    Pid = models.IntegerField()
    Tstatus= models.IntegerField()

    Tttechnology = (
        ('JAVA', 'JAVA'),
        ('PYTHON', 'PYTHON'),
        ('MATLAB', 'MATLAB'),
        ('JULIA', 'JULIA'),
        ('R','R')
    )
    Ttechnology = models.CharField(max_length=1, choices=Tttechnology)
    Tassignedto=models.CharField(max_length=600)
    Tassignedby=models.CharField(max_length=600)
    Tassigneddate=models.CharField(max_length=600)
    Tdeadline = models.CharField(max_length=400)

    class Meta:
        db_table ="task"

    def __str__(self):
        return  str(self.Pid)+"    "+self.Ttitle


class Message(models.Model):
    Mid = models.AutoField(primary_key=True)
    sender_username = models.CharField(max_length=3000)
    receiver_username = models.CharField(max_length=3000)
    content = models.CharField(max_length=45000)

    class Meta:
        db_table="message"





class TaskUpdate(models.Model):
    Uid= models.AutoField(primary_key=True)
    Tid = models.CharField(max_length=300)
    Utitle=models.CharField(max_length=3000)
    UDtime = models.CharField(max_length=3000)
    Udescription = models.CharField(max_length=4000)
    Uempname =models.CharField(max_length=4000)
    Uimg1 = models.ImageField(upload_to="media")
    Uimg2 = models.ImageField(upload_to="media")
    Uimg3 = models.ImageField(upload_to="media")

    class Meta:
        db_table="update"



class Login(models.Model):
    uname=models.CharField(max_length=100)
    password=models.CharField(max_length=300)


    def __str__(self):
        return self.uname

    class Meta:
        db_table="login"






















