from django.db import models

class Employee(models.Model):
    """
    Represents an employee profile.
    """
    ref_id = models.CharField(max_length=20, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    company = models.CharField(max_length=50, default='Default Company')
    role = models.CharField(max_length=150)
    status = models.CharField(max_length=50, default='pending')
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    offer_letter = models.FileField(upload_to='offer_letters/', null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            last_employee = Employee.objects.all().order_by('id').last()
            new_id_num = 1 if not last_employee else int(last_employee.ref_id[3:]) + 1
            self.ref_id = f'RMS{str(new_id_num).zfill(4)}'
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ref_id}: {self.name}"

class SiteStructure(models.Model):
    """
    MASTER DATA TABLE: Stores the permanent structure of each site.
    Equivalent to the old hardcoded MASTER_DATA_LIST.
    """
    sr_no = models.IntegerField(unique=True)
    site = models.CharField(max_length=100) # e.g., AGNI-CCM, BMM, SLR
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    skill_level = models.CharField(max_length=10)
    scope = models.IntegerField(default=0)

    class Meta:
        ordering = ['sr_no']
        verbose_name = "Site Structure Row"

    def __str__(self):
        return f"[{self.sr_no}] {self.site} - {self.designation}"

class ManpowerEntry(models.Model):
    """
    DAILY DATA TABLE: Stores daily attendance records.
    """
    date = models.DateField()
    # Link to the master structure
    structure = models.ForeignKey(SiteStructure, on_delete=models.CASCADE, null=True, blank=True)
    
    # Denormalized fields (copies of metadata at the time of entry)
    site = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    skill_level = models.CharField(max_length=10)
    scope = models.IntegerField(default=0)
    
    # User Inputs
    present = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)
    weekly_off = models.IntegerField(default=0)
    overtime = models.IntegerField(default=0) 
    remarks = models.TextField(null=True, blank=True)

    @property
    def ff_ratio(self):
        return round((self.present / self.scope) * 100, 2) if self.scope > 0 else 0.00

    def __str__(self):
        return f"{self.date} - {self.site} - {self.designation}"