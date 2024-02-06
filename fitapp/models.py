from django.db import models

# Create your models here.

class Trainer_tbl(models.Model):
    trainer_Name=models.CharField(max_length=20,null=True)
    trainer_images = models.FileField(upload_to="media", null=True)
    trainer_Email = models.EmailField(max_length=20, null=True)
    trainer_Password = models.CharField(max_length=20, null=True)
    trainer_Contact = models.IntegerField(null=True)
    trainer_Address=models.CharField(max_length=30,null=True)
    trainer_Gender=models.CharField(max_length=10,null=True)
    trainer_DOB = models.DateField(max_length=10, null=True)
    trainer_Salary = models.IntegerField(null=True)

class doctor_tbl(models.Model):
    doctor_Name = models.CharField(max_length=20,null=True)
    doctor_Email = models.EmailField(max_length=20, null=True)
    doctor_Contact = models.IntegerField(null=True)
    doctor_Gender = models.CharField(max_length=10, null=True)
    doctor_images = models.FileField(upload_to="media", null=True)
    doctor_NameOfProof = models.FileField( upload_to="media", null=True)
    doctor_ID_Number = models.CharField(max_length=20, null=True)
    doctor_qualification = models.CharField(max_length=25,null=True)
    doctor_experience = models.IntegerField(null=True)
    DateOfJoining = models.DateField(null=True)
    doctor_Status =models.CharField(max_length=20, null=True)
    doctor_salary =models.IntegerField(null=True)
    doctor_Password = models.CharField(max_length=20, null=True)

class package_tbl(models.Model):
    package_type = models.CharField(max_length=20, null=True)
    package_duration = models.IntegerField(null=True)
    package_price = models.IntegerField(null=True)
    package_status = models.CharField(max_length=20,null=True)

class Event_tbl(models.Model):
    event_name = models.CharField(max_length=20,null=True)
    event_category = models.CharField(max_length=20,null=True)
    event_agelimit = models.IntegerField(null=True)
    event_weightlimit = models.IntegerField(null=True)
    event_place = models.CharField(max_length=20,null=True)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)
    event_status = models.CharField(max_length=20,null=True)

class Product_category_tbl(models.Model):
    product_category = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
class Products_tbl(models.Model):
    product_category = models.ForeignKey(Product_category_tbl, on_delete=models.CASCADE, null=True)
    product_name =  models.CharField(max_length=20,null=True)
    product_images = models.FileField(upload_to="media",null=True)
    product_details = models.CharField(max_length=50,null=True)
    product_delivery_charge = models.IntegerField(null=True)
    product_gst = models.IntegerField(null=True)
    product_discounts = models.IntegerField(null=True)
    product_totalprice = models.IntegerField(null=True)
    product_status = models.CharField(max_length=20,null=True)

class memberregistration_tbl(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, null=True)
    Age = models.IntegerField(null=True)
    DOB = models.DateField(max_length=10, null=True)
    Contact = models.IntegerField(null=True)
    state = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    pincode = models.IntegerField(null=True)
    email = models.EmailField(max_length=20, null=True)
    DateOfJoining = models.DateField(null=True)
    password = models.CharField(max_length=20, null=True)
    person_type= models.CharField(max_length=20, null=True)
    purpose = models.CharField(max_length=20, null=True)
    package_type = models.ForeignKey(package_tbl,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=20, null=True)
    expiry_date=models.DateField(null=True)


class RegPayment_tbl(models.Model):
    memberid=models.ForeignKey(memberregistration_tbl,on_delete=models.CASCADE,null=True)
    membername=models.CharField(max_length=20,null=True)
    totalamount=models.IntegerField(null=True)
    advanceamount=models.IntegerField(null=True)
    paid_amount=models.IntegerField(null=True)
    monthlyPayment=models.IntegerField(null=True)
    balanceamount=models.IntegerField(null=True)
    paymenttime=models.TimeField(null=True,auto_now_add=True)
    paymentdate=models.DateField(null=True,auto_now_add=True)
    status = models.CharField(max_length=20, null=True)


class AssignTrainer_tbl(models.Model):
    memberid = models.ForeignKey(memberregistration_tbl,on_delete=models.CASCADE, null=True)
    membername = models.CharField(max_length=20, null=True)
    trainer_id= models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=100,null=True)
    time = models.TimeField(null=True, auto_now_add=True)
    date = models.DateField(null=True, auto_now_add=True)

class ScheduleTime_tbl(models.Model):
    memberassigned = models.ForeignKey(AssignTrainer_tbl, on_delete=models.CASCADE, null=True)
    trainer_id= models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    StartTime = models.TimeField(null=True )
    EndTime = models.TimeField(null=True)

class ViewCart_tbl(models.Model):
     Product_id =models.ForeignKey(Products_tbl,on_delete=models.CASCADE,null=True)
     memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)

class MemberBooking_tbl(models.Model):
    memberid = models.ForeignKey(memberregistration_tbl,on_delete=models.CASCADE,null=True)
    full =  models.CharField(max_length=20, null=True)
    mobile= models.IntegerField(null=True)
    email = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=20, null=True)
    house = models.CharField(max_length=20, null=True)
    road = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    pincode = models.CharField(max_length=20, null=True)
    near = models.CharField(max_length=20, null=True)
    con_name= models.CharField(max_length=20, null=True)
    con_mob = models.IntegerField(null=True)
    del_add = models.CharField(max_length=20, null=True)
    build = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=20, null=True)
    states = models.CharField(max_length=20, null=True)
    town = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    product_totalprice = models.IntegerField(null=True)
    product_delivery_charge =models.IntegerField(null=True)
    pay =models.CharField(max_length=20, null=True)
    date = models.DateField(null=True, auto_now_add=True)
    time = models.TimeField(null=True, auto_now_add=True)

class Feedback_tbl(models.Model):
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=20, null=True)
    Email = models.EmailField(max_length=30, null=True)
    Message = models.CharField(max_length=300, null=True)
    star1 = models.CharField(max_length=300, null=True)

class member_health_details_tbl(models.Model):
    memberid=models.ForeignKey(memberregistration_tbl,on_delete=models.CASCADE,null=True)
    height=models.IntegerField(null=True)
    weight=models.IntegerField(null=True)
    bp=models.CharField(max_length=100,null=True)
    heart_disease=models.CharField(max_length=100,null=True)
    joint_problem = models.CharField(max_length=100, null=True)
    dizziness = models.CharField(max_length=100, null=True)

class Doctor_Member_Report(models.Model):
    health_id=models.ForeignKey(member_health_details_tbl,on_delete=models.CASCADE,null=True)
    month=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    phone=models.IntegerField(null=True)
    previous_weight=models.IntegerField(null=True)
    current_weight=models.IntegerField(null=True)
    previous_height=models.IntegerField(null=True)
    current_height=models.IntegerField(null=True)
    medical_exam=models.CharField(max_length=100,null=True)
    medical_test=models.CharField(max_length=100,null=True)
    overall_condition=models.CharField(max_length=100,null=True)
    instructions=models.CharField(max_length=100,null=True)
    signature=models.ImageField(upload_to="media", null=True)

class workout_details(models.Model):
    memberid=models.ForeignKey(memberregistration_tbl,on_delete=models.CASCADE,null=True)
    Trainer_id=models.ForeignKey(Trainer_tbl,on_delete=models.CASCADE,null=True)
    Total_Workout = models.IntegerField(null=True)
    Completed_Work_out=models.IntegerField(null=True)
    Pending_Workout=models.IntegerField(null=True)
    Total_Time_Taken=models.IntegerField(null=True)
    Date=models.DateField(null=True)



class Trainer_Member_Report(models.Model):
    Trainer_id=models.ForeignKey(Trainer_tbl,on_delete=models.CASCADE,null=True)
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=100, null=True)
    Total_Workout = models.IntegerField(null=True)
    Completed_Work_out = models.IntegerField(null=True)
    Pending_Workout = models.IntegerField(null=True)
    Total_Time_Taken = models.IntegerField(null=True)
    performance = models.CharField(max_length=100, null=True)

class Trainer_Feedback(models.Model):
    Trainer_id = models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)
    membername= models.CharField(max_length=100, null=True)
    memberemail=models.EmailField(null=True)
    overall_exp= models.CharField(max_length=100, null=True)
    behavior= models.CharField(max_length=100, null=True)
    helpfulness= models.CharField(max_length=100, null=True)
    comments= models.CharField(max_length=100, null=True)
    date=models.DateField(auto_now_add=True)

class Trainer_Feedback_Report(models.Model):
    Trainer_id = models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    total_overall_exp = models.CharField(max_length=100, null=True)
    total_behavior = models.CharField(max_length=100, null=True)
    total_helpfulness = models.CharField(max_length=100, null=True)
    instructions = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=True)


class Leave_Tbl(models.Model):
    trainer_id=models.ForeignKey(Trainer_tbl,on_delete=models.CASCADE,null=True)
    trainer_name=models.CharField(max_length=100, null=True)
class leave_dates_tbl(models.Model):
    dates=models.DateField(null=True)
    leave_id=models.ForeignKey(Leave_Tbl,null=True,on_delete=models.CASCADE)
    trainer_id=models.ForeignKey(Trainer_tbl,on_delete=models.CASCADE,null=True)


class workoutlist_tbl(models.Model):
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)

    trainer_id = models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    wrktype=models.CharField(max_length=100, null=True)
    week=models.CharField(max_length=100, null=True)
    month=models.CharField(max_length=100,null=True)


class Exercise_Name(models.Model):
    work_id=models.ForeignKey(workoutlist_tbl,on_delete=models.CASCADE,null=True)
    excname=models.CharField(max_length=100, null=True)
    reps=models.IntegerField(null=True)
    week=models.CharField(max_length=100, null=True)
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)




class Doctor_Leave_Tbl(models.Model):
    doctor_id=models.ForeignKey(doctor_tbl,on_delete=models.CASCADE,null=True)
    doctor_Name=models.CharField(max_length=100, null=True)

class Doctor_leave_dates_tbl(models.Model):
    dates=models.DateField(null=True)
    leave_id=models.ForeignKey(Doctor_Leave_Tbl,null=True,on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(doctor_tbl,on_delete=models.CASCADE,null=True)


class TrainerSalary_tbl(models.Model):
    trainer_id = models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    trainer_Name=models.CharField(max_length=100,null=True)
    month=models.CharField(max_length=100,null=True)
    total_leave=models.IntegerField( null=True)
    total_working_days=models.IntegerField( null=True)
    basic_pay=models.IntegerField( null=True)
    total_salary=models.IntegerField( null=True)
    status=models.CharField(max_length=100,null=True)

class DoctorSalary_tbl(models.Model):
    doctor_id = models.ForeignKey(doctor_tbl, on_delete=models.CASCADE, null=True)
    doctor_Name=models.CharField(max_length=100,null=True)
    month=models.CharField(max_length=100,null=True)
    total_leave=models.IntegerField( null=True)
    total_working_days=models.IntegerField( null=True)
    basic_pay=models.IntegerField( null=True)
    total_salary=models.IntegerField( null=True)
    status=models.CharField(max_length=100,null=True)

class Take_Appointment_tbl(models.Model):
    memberid=models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)
    doctor_id = models.ForeignKey(doctor_tbl, on_delete=models.CASCADE, null=True)
    membername = models.CharField(max_length=100, null=True)
    reason=models.CharField(max_length=100, null=True)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    status=models.CharField(max_length=100,null=True)

class AddDietPlan_tbl(models.Model):
    trainer_id = models.ForeignKey(Trainer_tbl, on_delete=models.CASCADE, null=True)
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)

    week = models.CharField(max_length=100, null=True)
    day=models.CharField(max_length=100, null=True)
    brkfst=models.CharField(max_length=100, null=True)
    lunch=models.CharField(max_length=100, null=True)
    snack=models.CharField(max_length=100, null=True)
    dinner=models.CharField(max_length=100, null=True)

class Booking(models.Model):
    booking=models.ForeignKey(MemberBooking_tbl,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=100,null=True)
    price=models.IntegerField(null=True)
    Product_image=models.ImageField(upload_to="media",null=True)


class MonthlyFeePayment_tbl(models.Model):
    memberid = models.ForeignKey(memberregistration_tbl, on_delete=models.CASCADE, null=True)
    reg_payment= models.ForeignKey(RegPayment_tbl, on_delete=models.CASCADE, null=True)
    membername = models.CharField(max_length=20, null=True)
    email= models.CharField(max_length=20, null=True)
    package_type=models.CharField(max_length=20, null=True)
    totalamount = models.IntegerField(null=True)
    totalpaid = models.IntegerField(null=True)
    balanceamount = models.IntegerField(null=True)
    monthlyPayment = models.IntegerField(null=True)
    month = models.CharField(max_length=100, null=True)
    paymenttime = models.TimeField(null=True, auto_now_add=True)
    paymentdate = models.DateField(null=True, auto_now_add=True)
    pay =models.CharField(max_length=20, null=True)




