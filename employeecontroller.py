from employee.models import Employee
from employee.orm_configuration import app,db
from flask import request,render_template

empId = 0
def get_employee_id():
    global empId
    emplist = Employee.query.all()
    if emplist:
        empId = None
    else:
        empId = 1000


@app.route('/',methods=['GET','POST'])
def add_update_employee():
    msg = ''
    get_employee_id()
    if request.method == 'POST':
        fromdata = request.form
        dbemp = Employee.query.filter_by(eid=fromdata.get('empid')).first()
        if dbemp:
            dbemp.ename = fromdata['empname']
            dbemp.erole = fromdata['emprole']
            dbemp.esalary = fromdata['empsal']
            dbemp.eadr = fromdata['adr']
            db.session.commit()
            msg = 'Employee ID {} Record Updated Successfully..!'.format(dbemp.eid)
            return render_template('emp.html',msg=msg,emplist=Employee.query.all(),emp=Employee.dummy_employee())

        emp = Employee(ename=fromdata['empname'],erole=fromdata['emprole'],esalary=fromdata['empsal'],eadr=fromdata['adr'])
        if emp.ename and emp.erole and emp.esalary and emp.eadr:
            if empId:
                emp.eid = empId
            db.session.add(emp)
            db.session.commit()
            msg = 'Employee ID {} Record Added Successfully..!'.format(emp.eid)
        else:
            msg = 'Fill all field..!'

    return render_template('emp.html',msg=msg,emplist=Employee.query.all(),
                           emp=Employee.dummy_employee())

@app.route('/emp/delete/<int:empid>')
def delete_employee(empid):
    emp = Employee.query.filter_by(eid=empid).first()
    msg = ''
    if emp:
        db.session.delete(emp)
        db.session.commit()
        msg = 'Employee ID {} Delete Successfully..!'.format(empid)

    return render_template('emp.html',msg=msg,emplist=Employee.query.all(),
                           emp=Employee.dummy_employee())

@app.route('/emp/edit/<int:empid>')
def edit_employee(empid):
    emp = Employee.query.filter_by(eid=empid).first()
    msg = ''
    return render_template('emp.html',msg=msg,emplist=Employee.query.all(),emp=emp)

if __name__ == '__main__':
    app.run(debug=True)