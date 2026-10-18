#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Exercise:1

def greeting_system(name, course = "Python Programming"):
    print("Hello", name,"!")
    print("Welcome in", course, "course")
    print("======================================================================")
    print()

greeting_system("Amisha","Data Science")
greeting_system("Priyanshi")


# In[11]:


# Exercise:2

def calculate_discount(bill, discount_per = 5):
    if bill <= 0:
        return "Error: Invalid Bill Amount"
    if discount_per < 0 or discount_per > 100:
        return "Error: Invalid discount percentage"
    else:
        if bill < 1000:
            discount_per = 5
        elif bill < 5000:
            discount_per = 10
        elif bill < 10000:
            discount_per = 15
        else:
            discount_per = 20

    discount_amount = bill * discount_per / 100
    final_amount = bill - discount_amount

    print("Original Bill Amount:", bill)
    print("Discount:", discount_per, "%")
    print("Discount Amount:", discount_amount)
    print("final payable amount:", final_amount)
    print("=======================================")
    print()
calculate_discount(0)
calculate_discount(900)
calculate_discount(1300)
calculate_discount(8000,12)


# In[7]:


# Exercise:3

def employee_details(**details):
    for key, value in details.items():
        print(key, ":", value)
    print("===========================")
    print()
employee_details(Name = "Priyanshi", Department = "IT", Salary = 70000, City = "Noida", Experience = "2 year")
employee_details(Name = "Adarsh", Department = "IT", Salary = 100000, City = "Noida", Experience = "3 year")


# In[12]:


# Exercise:4

def student_result(name,*marks,**details):
    print("Student Name:", name)
    print("Subject Marks:", marks)

    if len(marks)>0:
        total_marks = sum(marks)
        Avg = total_marks/len(marks)
        print("Total Marks:", total_marks)
        print("Avg Marks:", Avg)
    print("=====Additional Information=====")
    for key, value in details.items():
        print(key, ":", value)
    print("=============================================================")
    print()
student_result("Priya",89,93,94,97,87, student_id = "MCA2026069", semester = 1)
student_result("Aditya",69,91,54,67,87, student_id = "MCA2025047", semester = 3)
student_result("Anu",54,66,74,63,88, student_id = "MCA2026058", semester = 2)


# In[5]:


# Exercise:5

def add_items(*prices):
    print("prices:", prices)
    print("total:", sum(prices))

def Customer_details(name, city, member):
    print("Name:", name)
    print("City:", city)
    print("Member:", member)

prices = [147,369,324,691]
add_items(*prices)

customer = {
    "name":"priya",
    "city":"bareilly",
    "member":"gold"
}
Customer_details(**customer)


# In[6]:


# Exercise:6

def calculate_avg(*marks):
    if not marks:
        return "Error: no marks provided"
    for x in marks:
        if not isinstance(x, (int, float)) or isinstance(x,bool):
            return "Error: Marks Must be Numeric"
        if x < 0 or x > 100:
            return "Error: Marks Must be Between 0 and 100"
    return sum(marks)/len(marks) 

print(calculate_avg(55, 66, 97, 75, 58))
print(calculate_avg()) 
print(calculate_avg(55, 66, 97, 75, 58, "abc", True)) 
print(calculate_avg(55, -66, 97, 175, 58))





