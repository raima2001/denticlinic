from django.db import models


class Doctor(models.Model):
    docid = models.AutoField(primary_key=True)
    docname = models.CharField(max_length=100)
    degree = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.docname


class TimeFrame(models.Model):
    tfid = models.AutoField(primary_key=True)
    docid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=100)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.docid.docname + " -- " + self.weekday + " >> " + str(self.starttime) + " - " + str(self.endtime)


class Appointment(models.Model):
    apid = models.AutoField(primary_key=True)
    tframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    pname = models.TextField()
    pmobile = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pname+" - "+self.pmobile+" >> "+str(self.tframe)
