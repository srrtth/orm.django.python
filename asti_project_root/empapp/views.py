from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse


# Create your views here.

def create_employee(req):
    if req.method == "GET":
        return render(req, 'empapp/employee_form.html')
    elif req.method == "POST":
        # Step 1 Read employee
        empid = req.POST.get('emp_id')
        name = req.POST.get('emp_name')
        age = req.POST.get('emp_age')
        salary = req.POST.get('emp_salary')
        address = req.POST.get('emp_address')

        # step 2: Create "Employee model" object using employee input data
        employee = Employee(empid=empid, name=name, age=age, salary=salary, address=address)

        # step 3 call save() method on "employee model" object
        employee.save()

        # step 4 return response to the client saying employee created successfully
        return HttpResponse("<h1  style = 'Color: cherry'> employee created successfully </h1>")

def list_employees(req):
    #   STEP-1: x = Get all employees from Database table(EMPLOYEE) ===> QuerySet
    ### employees = {emp1, emp2}
    employees_db = Employee.objects.all()

    # STEP-2 - Create Context object(dict) with QuerySet
    context_data = {
        "employees": employees_db
    }

    # STEP-3 - Send context object through render() function
    return render(req, 'empapp/list_emp.html', context=context_data)


def del_emp_form(request):
    if request.method == 'GET':
        return render(request, 'empapp/del_emp_form.html')
    elif request.method == 'POST':
        # step1 - read the input employee id to be deleted  3
        id_input = request.POST.get('emp_pk')

        # step2 - get Employee object from DB based on input employee id...
        try:
            employee = Employee.objects.get(id=id_input)
            employee.delete()
            resp_msg = '<h1 style = "color:green">Employee Deleted Successfully!!!</h1>'
        except Exception:
            resp_msg = '<h1 style = "color:red"> Sorry, Employee with id {} did not find in the table </h1>'.format(id_input)
        return HttpResponse(resp_msg)
