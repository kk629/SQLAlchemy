from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import DatbaseInitialization, Insert
from datetime import datetime

engine = create_engine("sqlite:///db1.sqlite")
session = Session(bind=engine)



result = session.query(DatbaseInitialization.Customer).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)




result = session.query(DatbaseInitialization.Item).all()
for row in result:
   print ("Name: ",row.name," Cost Price:",row.cost_price, " Selling Price:",row.selling_price, " Quantity:",row.quantity)


result = session.query(DatbaseInitialization.Order).all()
for row in result:
   print ("ID: ",row.id," Date Placed:",row.date_placed, " Customer Id:",row.customer_id)



print(session.query(DatbaseInitialization.Customer))
print(session.query(DatbaseInitialization.Customer).count())
print(session.query(DatbaseInitialization.Item).count())
print(session.query(DatbaseInitialization.Order).count())



result = session.query(DatbaseInitialization.Customer).first()
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)

result = session.query(DatbaseInitialization.Item).first()
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)

result = session.query(DatbaseInitialization.Order).first()
print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)

result = session.query(DatbaseInitialization.Customer).get(1)
print ("Name: ",result.first_name," ",result.last_name, " Address:",result.address, " Email:",result.email)
result = session.query(DatbaseInitialization.Item).get(1)
print ("Name: ",result.name," Cost Price:",result.cost_price, " Selling Price:",result.selling_price, " Quantity:",result.quantity)
result = session.query(DatbaseInitialization.Order).get(100)
if(result != None): print ("ID: ",result.id," Date Placed:",result.date_placed, " Customer Id:",result.customer_id)
else: print(result)

result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.first_name == 'John').all()
print("All customers with name starting with John:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

result = session.query(DatbaseInitialization.Customer).filter(DatbaseInitialization.Customer.id <= 5, DatbaseInitialization.Customer.town.like("Nor%")).all()
print("All customers with id less than or equal to 5 and living in Norfolk town:")
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all customers who either live in Peterbrugh or Norfolk")
result = session.query(DatbaseInitialization.Customer).filter(or_(DatbaseInitialization.Customer.town == 'Peterbrugh',DatbaseInitialization.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all customers whose first name is John and live in Norfolk")
result = session.query(DatbaseInitialization.Customer).filter(and_(DatbaseInitialization.Customer.first_name == 'John',DatbaseInitialization.Customer.town == 'Norfolk')).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("find all johns who don't live in Peterbrugh")
result = session.query(DatbaseInitialization.Customer).filter(and_(DatbaseInitialization.Customer.first_name == 'John',not_(DatbaseInitialization.Customer.town == 'Peterbrugh',))).all()
for row in result:
   print ("Name: ",row.first_name," ",row.last_name, " Address:",row.address, " Email:",row.email)

print("")