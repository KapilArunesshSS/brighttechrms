from django.db import models

class Employee(models.Model):
    """
    Represents an employee profile in the database, corresponding to the
    'New Employee Registration' form.
    """
    # --- Renamed field to ref_id ---
    ref_id = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True, 
        editable=False,
        help_text="Custom, auto-generated employee ID (e.g., RMS0001)."
    )

    # Corresponds to the 'Full Name' input field.
    name = models.CharField(max_length=255, help_text="Full name of the employee.")

    # Corresponds to the 'Age' input field.
    age = models.PositiveIntegerField(help_text="Age of the employee.")

    # Corresponds to the 'Company' dropdown.
    company = models.CharField(
        max_length=50,
        default='Default Company',
        help_text="Company the employee is being registered for."
    )

    # Corresponds to the 'Job Role' dropdown.
    role = models.CharField(max_length=150, help_text="Job role of the employee.")

    # Corresponds to the 'Application Status' dropdown.
    status = models.CharField(
        max_length=10,
        default='pending',
        help_text="Current status of the application."
    )

    # Corresponds to the 'Upload Resume' file input.
    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True,
        help_text="The employee's resume file."
    )
    
    # --- NEW FIELD ---
    # Corresponds to the 'Upload Offer Letter' file input.
    offer_letter = models.FileField(
        upload_to='offer_letters/', # Saves to a different folder
        null=True, 
        blank=True,
        help_text="The employee's offer letter file."
    )

    # --- NEW FIELD ---
    # Corresponds to the 'Remarks' text area.
    remarks = models.TextField(
        null=True, 
        blank=True,
        help_text="Remarks, typically for 'rejected' status."
    )
    
    # Creating Contact
    contact_number = models.CharField(max_length=15, unique=True)

    # Timestamps for tracking when the record was created and last updated.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the Employee object,
        which is useful in the Django admin interface and for debugging.
        """
        return f"{self.ref_id}: {self.name}"

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a custom employee ID
        before the record is created.
        """
        # Only generate an ID if the object is being created for the first time.
        if not self.pk:
            # Get the last employee object from the database.
            last_employee = Employee.objects.all().order_by('id').last()
            
            # If no employees exist, start with 1.
            if not last_employee:
                new_id_num = 1
            else:
                # Extract the number from the last ID (e.g., 'RMS0001' -> 1) and increment it.
                last_id_num = int(last_employee.ref_id[3:]) # Get characters after 'RMS'
                new_id_num = last_id_num + 1
            
            # Format the new ID with the "RMS" prefix and 4-digit zero padding.
            self.ref_id = f'RMS{str(new_id_num).zfill(4)}'
            
        super(Employee, self).save(*args, **kwargs)

class ManpowerEntry(models.Model):
    date = models.DateField()
    site = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    skill_level = models.CharField(max_length=10)
    scope = models.IntegerField(help_text="The required manpower count")
    
    # User Input Fields
    present = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)
    weekly_off = models.IntegerField(default=0)
    overtime = models.IntegerField(default=0)

    @property
    def ff_ratio(self):
        # Calculation: (Present / Scope) * 100
        if self.scope > 0:
            return round((self.present / self.scope) * 100, 2)
        return 0

    def __str__(self):
        return f"{self.date} - {self.site} - {self.designation}"