from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import openpyxl
from openpyxl.styles import Font
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as login_django , logout as logout_django
from django.contrib.auth.decorators import login_required
from .models import Employee , ManpowerEntry
from django.db.models import Count
from datetime import datetime , date
import json

# allowing super user 
from django.contrib.auth.decorators import login_required, user_passes_test


# @login_required(login_url='login')
# def home(request):
#     return render (request, 'home.html')
@login_required(login_url='login')
def FFR(request):
    selected_site = request.GET.get('site_selection', 'ALL')
    report_date = request.GET.get('report_date', str(date.today()))

    # FIX: Fetch ALL entries for the date so Indicators stay green
    entries_for_date = ManpowerEntry.objects.filter(date=report_date)

    if request.method == "POST":
        form_site = request.POST.get('site_selection')
        form_date = request.POST.get('report_date')

        if 'delete_all_database' in request.POST:
            ManpowerEntry.objects.all().delete()
            messages.success(request, "Database reset successfully.")
            return redirect('FFR')

        if 'save_data' in request.POST:
            present_keys = [k for k in request.POST.keys() if k.startswith('p_')]
            
            for p_key in present_keys:
                sr_no = p_key.split('_')[1]
                try:
                    # Logic to ensure we save to the correct site
                    row_site = request.POST.get(f'site_{sr_no}') or form_site
                    dept = request.POST.get(f'dept_{sr_no}')
                    desig = request.POST.get(f'desig_{sr_no}')

                    ManpowerEntry.objects.update_or_create(
                        date=form_date,
                        site=row_site,
                        department=dept,
                        designation=desig,
                        defaults={
                            'skill_level': request.POST.get(f'skill_{sr_no}'),
                            'scope': int(request.POST.get(f'scope_{sr_no}', 0)),
                            'present': int(request.POST.get(f'p_{sr_no}', 0)),
                            'absent': int(request.POST.get(f'a_{sr_no}', 0)),
                            'weekly_off': int(request.POST.get(f'w_{sr_no}', 0)),
                            'overtime': int(request.POST.get(f'o_{sr_no}', 0)),
                            'remarks': request.POST.get(f'rem_{sr_no}', "")
                        }
                    )
                except Exception as e:
                    continue

            messages.success(request, f"FFR Records for {form_site} saved successfully.")
            return redirect(f"/FFR/?site_selection={form_site}&report_date={form_date}")

    return render(request, 'ffr.html', {
        'entries': entries_for_date,
        'selected_site': selected_site,
        'report_date': report_date,
    })

@login_required(login_url='login')
def export_ffr_all(request):
    site_filter = request.GET.get('site_selection', 'ALL')
    date_filter = request.GET.get('report_date')

    queryset = ManpowerEntry.objects.all()
    if site_filter != 'ALL':
        queryset = queryset.filter(site=site_filter)
    if date_filter:
        queryset = queryset.filter(date=date_filter)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "FFR Ledger"

    headers = ['Date', 'Site', 'Dept', 'Designation', 'Skill', 'Scope', 'P', 'A', 'Abs%', 'W/O', 'OT', 'FFR%', 'Remarks']
    sheet.append(headers)

    for record in queryset:
        # Use getattr to prevent crash if property is missing
        ff = getattr(record, 'ff_ratio', 0)
        ab = getattr(record, 'absent_ratio', 0)
        
        sheet.append([
            str(record.date), record.site, record.department, record.designation,
            record.skill_level, record.scope, record.present, record.absent,
            f"{ab}%", record.weekly_off, record.overtime, f"{ff}%", record.remarks or ""
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="FFR_Report.xlsx"'
    workbook.save(response)
    return response
@login_required(login_url='login')
def employee_list(request):
    """
    Handles displaying the employee list and calculating the status counts
    to be displayed on the dashboard.
    """
    # 1. Fetch all employees from the database.
    employees = Employee.objects.all()

    # 2. Calculate the total count and the count for each status.
    total_employees = employees.count()
    joined_count = employees.filter(status__iexact ='joined').count()
    offered_count = employees.filter(status__iexact ='offered').count()
    selected_count = employees.filter(status__iexact ='selected').count()
    pending_count = employees.filter(status__iexact ='pending').count()
    rejected_count = employees.filter(status__iexact ='rejected').count()
    left_count = employees.filter(status__iexact ='left').count()
    
    # 3. Add all calculated numbers to the context dictionary.
    context = {
        'employees': employees,
        'total_employees': total_employees,
        'joined_count': joined_count,
        'offered_count': offered_count,
        'selected_count': selected_count,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
        'left_count': left_count,
    }
    
    # 4. Render the dashboard template with the context data.
    return render(request, 'dashboard.html', context)
@login_required(login_url='login')
def add_employee(request):
    """
    Handles the creation of a new employee.

    - If the request method is GET, it displays the empty registration form.
    - If the request method is POST, it processes the submitted form data,
      saves the new employee to the database, and redirects to a success page.
    """
    if request.method == 'POST':
        # --- Process Form Data ---
        
        # Extracting data from the POST request
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact_number = request.POST.get('contact')
        company = request.POST.get('company')
        role = request.POST.get('role')
        status = request.POST.get('status')
        
        # The resume file is handled separately via request.FILES
        resume = request.FILES.get('resume')

        if Employee.objects.filter(contact_number=contact_number).exists():
            # 2. If it exists, add an error message.
            messages.error(request, 'This contact number already exists. Please use a different one.')
            # 3. Redirect back to the form so the user can see the message.
            return redirect('employee_list')  # Assuming you have a URL named 'employee_list'
        
        # Create a new Employee instance with the form data
        Employee.objects.create(
            name=name,
            age=age,
            contact_number=contact_number,
            company=company,
            role=role,
            status=status,
            resume=resume
        )
        

        # Redirect to a new URL after successful submission.
        # You should create a 'success' URL and template, 
        # or redirect to an employee list page.
        messages.success(request, 'Employee created successfully!')
        return redirect('employee_list') # Assuming you have a URL named 'employee_list'

    # --- Display Blank Form ---
    
    # If the request method is not POST (i.e., it's a GET request),
    # simply render the HTML form template.
    return render(request, 'add_employee.html')


@login_required(login_url='login')
def edit_employee(request, employee_id):
    # Get the specific employee object we want to edit
    employee = get_object_or_404(Employee, id=employee_id)

    # --- This block runs when the user submits the "Update Profile" form ---
    if request.method == 'POST':
        
        # 1. Update all the text-based fields from the form
        employee.name = request.POST.get('name')
        employee.age = request.POST.get('age')
        employee.contact_number = request.POST.get('contact')
        employee.company = request.POST.get('company')
        employee.role = request.POST.get('role')
        employee.status = request.POST.get('status')
        employee.remarks = request.POST.get('remarks')

        # 2. Clean up conditional fields
        # If status is not 'rejected', clear any old remarks
        if employee.status != 'rejected':
            employee.remarks = None # or '', depending on your model
        
        # If status is not 'offered', clear any old offer letter
        if employee.status != 'offered' and employee.offer_letter:
            employee.offer_letter.delete(save=False)
            employee.offer_letter = None

        # --- 3. Handle the Offer Letter File ---
        
        # Check if the "delete_offer_letter" checkbox was ticked
        if request.POST.get('delete_offer_letter'):
            if employee.offer_letter:
                employee.offer_letter.delete(save=False) # Delete file from storage
                employee.offer_letter = None # Clear the field in the database

        # Check if a *new* offer letter was uploaded
        new_offer_letter = request.FILES.get('offer_letter')
        if new_offer_letter:
            if employee.offer_letter:
                employee.offer_letter.delete(save=False) # Delete the old one first
            employee.offer_letter = new_offer_letter # Save the new one

        # --- 4. Handle the Resume File ---
        
        # Check if the "delete_resume" checkbox was ticked
        if request.POST.get('delete_resume'):
            if employee.resume:
                employee.resume.delete(save=False)
                employee.resume = None

        # Check if a *new* resume was uploaded
        new_resume = request.FILES.get('resume')
        if new_resume:
            if employee.resume:
                employee.resume.delete(save=False)
            employee.resume = new_resume

        # --- 5. Save all changes to the database ---
        employee.save()
        
        # Redirect back to the employee list page
        return redirect('employee_list') # Make sure 'employee_list' is the name of your URL

    # --- This runs if it's a GET request (just loading the page) ---
    context = {
        'employee': employee
    }
    return render(request, 'edit_employee.html', context)

@login_required(login_url='login')
def export_to_excel(request):
    """
    Handles the logic for exporting the employee list to an .xlsx file.
    Includes clickable hyperlinks for uploaded resumes.
    """
    # 1. Fetch all employee data
    employees = Employee.objects.all()
    
    # 2. Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Employee List'
    
    # 3. Define the table headers
    headers = [
        'REF_ID',
        'CREATED_AT',
        'NAME', 
        'AGE', 
        'CONTACT_NUMBER', 
        'DESIGNATION', 
        'SITE', 
        'STATUS',
        'RESUME', 
        'UPDATED_AT'
    ]
    sheet.append(headers)
    
    # Style the header row (Bold)
    for cell in sheet[1]:
        cell.font = Font(bold=True)
    
    # 4. Loop through employees and add their data as rows
    for index, employee in enumerate(employees, start=2):
        resume_cell_value = "No File"
        has_resume = False
        
        if employee.resume:
            # IMPORTANT: Excel needs the full absolute URL (http://...)
            resume_url = request.build_absolute_uri(employee.resume.url)
            resume_cell_value = f'=HYPERLINK("{resume_url}", "View Resume")'
            has_resume = True
        
        row = [
            employee.ref_id,
            employee.created_at.strftime('%Y-%m-%d'),
            employee.name,
            employee.age,
            employee.contact_number,
            employee.role,
            employee.company,
            employee.status,
            resume_cell_value,
            employee.updated_at.strftime('%Y-%m-%d')
        ]
        sheet.append(row)
        
        # If a resume exists, style that specific cell to look like a hyperlink
        if has_resume:
            resume_cell = sheet.cell(row=index, column=9) # Column 9 is 'RESUME'
            resume_cell.font = Font(color="0000FF", underline="single")

    # 5. Create the HttpResponse object with the correct headers for an Excel file
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    # This header tells the browser to treat the response as a file download
    response['Content-Disposition'] = 'attachment; filename="RMS_Database.xlsx"'
    
    # 6. Save the workbook to the response and return it
    workbook.save(response)
    
    return response

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser, login_url='employee_list')
def delete_employee(request, employee_id):
    """
    Deletes an employee from the database.
    """
    # Retrieve the specific employee object, or return a 404 error if not found.
    employee = get_object_or_404(Employee, id=employee_id)
    
    # Delete the employee record.
    employee.delete()
    
    # Redirect to the employee list page after deletion.
    return redirect('employee_list')

def login_view(request):

    if request.method == 'POST':
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']

        user = authenticate( request, username = email, password = password)

        if user is not None:
            login_django(request, user)
            # fname = user.first_name
            return redirect('employee_list')
        else:
            messages.error(request, 'The entered Email or password is incorrect.')
            return redirect('login')

    return render(request, 'authentication/login.html')


def logout(request):
    logout_django(request)
    return redirect('login')


SUMMARY_STATUSES = ['selected', 'offered', 'rejected', 'joined', 'pending', 'left']

@require_POST
@csrf_exempt 
def monthly_summary_api(request):
    """
    API endpoint to filter Employee data by created_at date range and company (site),
    and return the count of each status.
    """
    try:
        # Load JSON data from the request body
        data = json.loads(request.body)
        from_date_str = data.get('from_date')
        to_date_str = data.get('to_date')
        site = data.get('site')
        
        if not all([from_date_str, to_date_str, site]):
            return JsonResponse({'error': 'Missing date or site parameters.'}, status=400)

        # Convert date strings to datetime.date objects
        from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
        to_date_inclusive = datetime.strptime(to_date_str, '%Y-%m-%d').date()

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    except ValueError:
        return JsonResponse({'error': 'Invalid date format. Expected YYYY-MM-DD.'}, status=400)
    
    try:
        # 1. Filter the base queryset: Filter by company (site) and date range (using created_at field's date)
        filtered_employees = Employee.objects.filter(
            company=site,
            created_at__date__gte=from_date,
            created_at__date__lte=to_date_inclusive
        )

        # 2. Aggregate status counts: Group by status and count the records
        status_counts_queryset = filtered_employees.values('status').annotate(count=Count('status'))
        
        # Initialize the results dictionary with all statuses set to 0
        summary_results = {status: 0 for status in SUMMARY_STATUSES}
        total_count = 0

        # 3. Populate results and calculate total
        for item in status_counts_queryset:
            # Ensure the key is lowercase to match the JavaScript expectations
            status_key = item['status'].lower()
            if status_key in summary_results:
                summary_results[status_key] = item['count']
                total_count += item['count']

        # 4. Add the total count
        summary_results['total'] = total_count

        # 5. Return JSON response
        return JsonResponse(summary_results)

    except Exception as e:
        # Catch any database or unexpected errors
        print(f"Database error during summary generation: {e}")
        return JsonResponse({'error': f'An internal server error occurred: {e}'}, status=500)