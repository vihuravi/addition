from orm_configuration import db

class Employee(db.Model):
    eid = db.Column('emp_id', db.Integer(),primary_key=True)
    ename = db.Column('emp_name', db.String(100))
    erole = db.Column('emp_role', db.String(50))
    esalary = db.Column('emp_sal', db.Float())
    eadr = db.Column('emp_adr', db.String(100))

    @classmethod
    def dummy_employee(cls):
        return cls(eid=0, ename='', erole='', esalary=0.0,eadr='')


db.create_all()