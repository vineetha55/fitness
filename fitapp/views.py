from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')
def adminlogin(request):
    return render(request,'adminlogin.html')

def  admincheck(request):
    if request.method =='POST':
        username = request.POST.get('email')
        password = request.POST.get('password')


        if memberregistration_tbl.objects.filter(email=username,password=password).exists():
            log_obj = memberregistration_tbl.objects.get(email=username,password=password)
            request.session["userid"] = log_obj.id
            return redirect("/memberdashboard/")

        elif Trainer_tbl.objects.filter(trainer_Email=username,trainer_Password=password).exists():
            log_obj1 = Trainer_tbl.objects.get(trainer_Email=username,trainer_Password=password)
            request.session["trainerid"] = log_obj1.id
            return redirect("/Trainerhome/")
        elif doctor_tbl.objects.filter(doctor_Email=username, doctor_Password=password).exists():
            log_obj1 = doctor_tbl.objects.get(doctor_Email=username, doctor_Password=password)
            request.session["doctorid"] = log_obj1.id
            return redirect("/Doctorhome/")
        else:
            return HttpResponse("Invalid data")
    else:
            return HttpResponse("Invalid data")




from datetime import date
def adminhome(request):
    doc=doctor_tbl.objects.all().count()
    pro=Products_tbl.objects.all().count()
    member=memberregistration_tbl.objects.all().count()
    l_doc=Doctor_leave_dates_tbl.objects.filter(dates=date.today()).count()
    l_tra=leave_dates_tbl.objects.filter(dates=date.today()).count()
    leave=l_doc+l_tra
    return render(request, 'adminhome.html',{"doc":doc,"pro":pro,"member":member,"leave":leave})

def AddTrainer(request):
    return render(request, 'AddTrainer.html')

def saveTrainer(request):
    if request.method == "POST":
        obj=Trainer_tbl()
        obj.trainer_Name=request.POST.get("Name")
        trainer_images = request.FILES['images']
        fs = FileSystemStorage()
        filename = fs.save(trainer_images.name, trainer_images)
        fileurl = fs.url(filename)
        obj.trainer_images = fileurl
        obj.trainer_Email = request.POST.get("email")
        obj.trainer_Password = request.POST.get("Password")
        obj.trainer_Contact = request.POST.get("phone")
        obj.trainer_Address = request.POST.get("Address")
        obj.trainer_Gender = request.POST.get("Gender")
        obj.trainer_DOB = request.POST.get("date")
        obj.trainer_Salary = request.POST.get("sal")
        obj.save()
        return redirect("/AddTrainer/")
def ViewTrainer(request):
    data = Trainer_tbl.objects.all()
    return render(request, "ViewTrainer.html", {"data": data})
def EditTrainer(request,id):
    data = Trainer_tbl.objects.get(id=id)
    return render(request, "EditTrainer.html", {"data": data})

def updateTrainer(request, id):
        obj = Trainer_tbl.objects.get(id=id)
        obj.trainer_Name = request.POST.get("Name")
        obj.trainer_Email = request.POST.get("email")
        obj.trainer_Password = request.POST.get("Password")
        obj.trainer_Contact = request.POST.get("phone")
        obj.trainer_Address = request.POST.get("Address")
        obj.trainer_Salary = request.POST.get("sal")
        obj.save()
        return redirect("/ViewTrainer/")


def DeleteTrainer(request, id):
    data = Trainer_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewTrainer/")

def AddDoctor(request):
    return render(request, 'AddDoctor.html')

def saveDoctor(request):
    if request.method == "POST":
        obj = doctor_tbl()
        obj.doctor_Name=request.POST.get("name")
        obj.doctor_Email = request.POST.get("email")
        obj.doctor_Contact = request.POST.get("phone")
        obj.doctor_Gender = request.POST.get("gender")
        doctor_images = request.FILES['images']
        fs = FileSystemStorage()
        filename = fs.save(doctor_images.name, doctor_images)
        fileurl = fs.url(filename)
        obj.doctor_images = fileurl
        obj.doctor_ID_Number =request.POST.get("idnumber")
        obj.doctor_NameOfProof=request.POST.get("proofname")
        doctor_qualification = request.FILES['qproof']
        fs = FileSystemStorage()
        filename = fs.save(doctor_qualification.name, doctor_qualification)
        fileurl = fs.url(filename)
        obj.doctor_qualification = fileurl
        obj.doctor_experience = request.POST.get("experience")
        obj.DateOfJoining = request.POST.get("joindate")
        obj.doctor_Status = request.POST.get("joindate")
        obj.doctor_salary = request.POST.get("salary")
        obj.doctor_Password = request.POST.get("password")
        obj.save()
        return redirect("/AddDoctor/")

def ViewDoctor(request):
    data = doctor_tbl.objects.all()
    return render(request, "ViewDoctor.html", {"data": data})

def EditDoctor(request,id):
    data = doctor_tbl.objects.get(id=id)
    return render(request, "EditDoctor.html", {"data": data})

def updateDoctor(request, id):
    obj = doctor_tbl.objects.get(id=id)
    obj.doctor_Name = request.POST.get("name")
    obj.doctor_Email = request.POST.get("email")
    obj.doctor_Contact = request.POST.get("phone")
    obj.doctor_Gender = request.POST.get("gender")
    obj.doctor_ID_Number = request.POST.get("idnumber")
    obj.doctor_NameOfProof = request.POST.get("proofname")
    doctor_qualification = request.FILES['qproof']
    fs = FileSystemStorage()
    filename = fs.save(doctor_qualification.name, doctor_qualification)
    fileurl = fs.url(filename)
    obj.doctor_qualification = fileurl
    obj.doctor_experience = request.POST.get("experience")
    obj.DateOfJoining = request.POST.get("joindate")
    obj.doctor_Status = request.POST.get("joindate")
    obj.doctor_salary = request.POST.get("salary")
    obj.doctor_Password = request.POST.get("password")
    obj.save()
    return redirect("/ViewDoctor/")

def DeleteDoctor(request, id):
    data = doctor_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewDoctor/")

def AddPackage(request):
    return render(request, 'AddPackage.html')

def savepackage(request):
    if request.method == "POST":
        obj = package_tbl()
        obj.package_type = request.POST.get("ptype")
        obj.package_duration = request.POST.get("pduration")
        obj.package_type = request.POST.get("ptype")
        obj.package_price = request.POST.get("pprice")
        obj.package_status =request.POST.get("status")
        obj.save()
        return redirect("/AddPackage/")


def ViewPackage(request):
    data = package_tbl.objects.all()
    return render(request, "ViewPackage.html", {"data": data})
def Editpackage(request,id):
    data = package_tbl.objects.get(id=id)
    return render(request, "Editpackage.html", {"data": data})

def updatepackage(request, id):
    obj = package_tbl.objects.get(id=id)
    obj.package_type = request.POST.get("ptype")
    obj.package_duration = request.POST.get("pduration")
    obj.package_price = request.POST.get("pprice")
    obj.package_status = request.POST.get("status")
    obj.save()
    return redirect("/ViewPackage/")

def Deletepackage(request, id):
    data = package_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewPackage/")


def AddEvent(request):
    return render(request, 'AddEvent.html')

def SaveEvent(request):
    if request.method == "POST":
        obj = Event_tbl()
        obj.event_name = request.POST.get("ename")
        obj.event_category= request.POST.get("ecategory")
        obj.event_agelimit = request.POST.get("alimit")
        obj.event_weightlimit = request.POST.get("wlimit")
        obj.event_place = request.POST.get("place")
        obj.event_date= request.POST.get("edate")
        obj.event_time= request.POST.get("etime")
        obj.event_status =request.POST.get("status")
        obj.save()
        return redirect("/AddEvent/")

def ViewEvent(request):
        data = Event_tbl.objects.all()
        return render(request, "ViewEvent.html", {"data": data})

def EditEvent(request, id):
        data = Event_tbl.objects.get(id=id)
        return render(request, "EditEvent.html", {"data": data})
def UpdateEvent(request, id):
        obj = Event_tbl.objects.get(id=id)
        obj.event_name = request.POST.get("ename")
        obj.event_category = request.POST.get("ecategory")
        obj.event_agelimit = request.POST.get("alimit")
        obj.event_weightlimit = request.POST.get("wlimit")
        obj.event_place = request.POST.get("place")
        obj.event_date = request.POST.get("edate")
        obj.event_time = request.POST.get("etime")
        obj.event_status = request.POST.get("status")
        obj.save()
        return redirect("/ViewEvent/")


def DeleteEvent(request, id):
        data = Event_tbl.objects.get(id=id)
        data.delete()
        return redirect("/ViewEvent/")

def AddProduct(request):
    a=Product_category_tbl.objects.all()
    return render(request, 'AddProduct.html',{"a":a})

def SaveProduct(request):
    if request.method == "POST":
        obj = Products_tbl()
        obj.product_category_id = request.POST.get("Category")
        obj.product_name = request.POST.get("Name")
        product_images= request.FILES["Images"]
        fs=FileSystemStorage()
        filename=fs.save(product_images.name, product_images)
        fileurl=fs.url(filename)
        obj.product_images=fileurl
        obj.product_details = request.POST.get("Details")
        obj.product_gst = request.POST.get("gst")
        obj.product_totalprice = request.POST.get("total")
        obj.product_status= request.POST.get("status")
        obj.save()
        return redirect("/AddProduct/")

def ViewProduct(request):
    data = Products_tbl.objects.all()
    return render(request, "ViewProduct.html", {"data": data})

def EditProduct(request,id):
    data =  Products_tbl.objects.get(id=id)
    return render(request, "EditProduct.html", {"data": data})

def UpdateProduct(request,id):
    obj = Products_tbl.objects.get(id=id)
    obj.product_category = request.POST.get("Category")
    obj.product_name = request.POST.get("Name")
    #obj.product_images = request.POST.get("Images")
    obj.product_details = request.POST.get("Details")
    obj.product_gst = request.POST.get("gst")
    obj.product_totalprice = request.POST.get("total")
    obj.product_status = request.POST.get("status")
    obj.save()
    return redirect("/ViewProduct/")

def DeleteProduct(request, id):
        data = Products_tbl.objects.get(id=id)
        data.delete()
        return redirect("/ViewProduct/")


def memberregistration(request):
    p=package_tbl.objects.all()
    return render(request,'memberregistration.html',{"p":p})

def savememberregistration(request):
    obj = memberregistration_tbl()
    obj.first_name= request.POST.get("fname")
    obj.last_name = request.POST.get("lname")
    obj.address = request.POST.get("address")
    obj.gender= request.POST.get("inlineRadioOptions1")
    obj.Age= request.POST.get("age")
    obj.DOB = request.POST.get("dob")
    obj.Contact = request.POST.get("phone")
    obj.state = request.POST.get("state")
    obj.place = request.POST.get("place")
    obj.pincode = request.POST.get("pincode")
    obj.email = request.POST.get("email")
    obj.DateOfJoining = request.POST.get("doj")
    obj.password = request.POST.get("password")
    obj.person_type = request.POST.get("inlineRadioOptions")
    obj.purpose= request.POST.get("purpose")
    obj.package_type_id = request.POST.get("package")

    d=package_tbl.objects.get(id=request.POST.get("package"))
    duration=d.package_duration
    from datetime import date,timedelta
    today=date.today()
    if duration == 3:
        obj.expiry_date=today+timedelta(days=90)
        obj.save()
    elif duration == 6:
        obj.expiry_date = today + timedelta(days=180)
        obj.save()
    obj.save()
    return redirect("MemberPayment" ,id=obj.id)

def memberdashboard(request):
        return render(request, 'memberdashboard.html')


def find_duration(request):
    print("hello")
    packageid=request.GET.get("p")
    data=package_tbl.objects.get(id=packageid)
    duration=data.package_duration
    return JsonResponse(duration, safe=False)

def MemberPayment(request,id):
    a=memberregistration_tbl.objects.get(id=id)
    return render(request, 'MemberPayment.html',{"a":a})

def SaveMemberPayment(request,id):
    if request.method == "POST":
        obj = RegPayment_tbl()
        obj.memberid_id= id
        obj.membername = request.POST.get("Name")
        obj.totalamount = request.POST.get("total")
        obj.advanceamount = request.POST.get("pay")
        obj.monthlyPayment = request.POST.get("monthly")
        totalamount = request.POST.get("total")
        advanceamount = request.POST.get("pay")
        b=int(totalamount)- int(advanceamount)
        obj.balanceamount= b
        obj.paid_amount=request.POST.get("monthly")
        obj.save()
        return redirect("/")

def ViewMemberPayment(request):
    data = RegPayment_tbl.objects.all()
    return render(request,'ViewMemberPayment.html',{"data": data})


def viewmemberregistration(request):
    data = memberregistration_tbl.objects.all()
    return render(request, "viewmemberregistration.html", {"data": data})

def DeleteMember(request, id):
        data = memberregistration_tbl.objects.get(id=id)
        data.delete()
        return redirect("/viewmemberregistration/")

def Trainerhome(request):
    data=Trainer_tbl.objects.get(id=request.session["trainerid"])
    return render(request, 'Trainerhome.html',{"data":data})

def AssignTrainer(request,id):
    data=memberregistration_tbl.objects.get(id=id)
    data1=Trainer_tbl.objects.all()
    return render(request, 'AssignTrainer.html',{"data":data,"data1":data1})

def saveAssignTrainer(request,id):
    obj = AssignTrainer_tbl()
    obj.memberid_id= id
    obj.membername = request.POST.get("mname")
    obj.trainer_id_id = request.POST.get("tname")
    obj.save()
    m=memberregistration_tbl.objects.get(id=id)
    m.status="Assigned"
    m.save()
    return redirect("/viewmemberregistration/")

def TrainerViewAssignedMember(request):
    obj = AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request,"TrainerViewAssignedMember.html",{"obj":obj})

def AddSchedule(request):
    obj = AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])
    #obj1=obj.exclude(status="True")
    #print(obj,"obj")
    #print(obj1,"obj111")

    return render(request, 'AddSchedule.html',{"obj":obj})

def SaveSchedule(request):
    if request.method == "POST":
        obj = ScheduleTime_tbl()
        obj.memberassigned_id = request.POST.get("name")
        obj.trainer_id_id = request.session["trainerid"]

        obj.StartTime = request.POST.get("start")
        obj.EndTime = request.POST.get("end")
        obj.save()
        data=AssignTrainer_tbl.objects.get(id=request.POST.get("name"))
        data.status="True"
        data.save()
        return redirect("/AddSchedule/")

def ViewSchedule(request):
    data = ScheduleTime_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request, "ViewSchedule.html",{"data":data})
def EditSchedule(request,id):
    data = ScheduleTime_tbl.objects.get(id=id)
    return render(request, "EditSchedule.html")

def UpdateSchedule(request, id):
    obj = ScheduleTime_tbl.objects.get(id=id)
    obj.StartTime = request.POST.get("start")
    obj.EndTime = request.POST.get("end")
    obj.save()
    return redirect("/ViewSchedule/")

def DeleteSchedule(request, id):
    data = ScheduleTime_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewSchedule/")

def AddCategory(request):
    return render(request, 'AddCategory.html')

def SaveCategory(request):
    if request.method == "POST":
        obj=Product_category_tbl()
        obj.product_category=request.POST.get("Category")
        obj.status = request.POST.get("status")
        obj.save()
        return redirect("/AddCategory/")

def ViewCategory(request):
    data = Product_category_tbl.objects.all()
    return render(request, "ViewCategory.html",{"data":data})

def EditCategory(request,id):
    data =  Product_category_tbl.objects.get(id=id)
    return render(request, "EditCategory.html",{"data":data})

def UpdateCategory(request,id):
    obj = Product_category_tbl.objects.get(id=id)
    obj.product_category = request.POST.get("Category")
    obj.product_status = request.POST.get("status")
    obj.save()
    return redirect("/ViewCategory/")

def DeleteCategory(request, id):
        data = Product_category_tbl.objects.get(id=id)
        data.delete()
        return redirect("/ViewCategory/")

def memberviewproduct(request):
    data = Products_tbl.objects.all()
    data1=Product_category_tbl.objects.all()
    return render(request, "memberviewproduct.html", {"data": data,"data1":data1})

def SaveCart(request,id):
        obj = ViewCart_tbl()
        obj.memberid_id=request.session["userid"]
        obj.Product_id_id=id
        obj.save()
        return redirect("/ViewCart/")

def ViewCart(request):
    data=ViewCart_tbl.objects.filter(memberid=request.session['userid'])
    subtotal=0
    gst=0
    for i in data:
        p = i.Product_id.product_totalprice
        subtotal += p
        gst+= i.Product_id.product_gst
    print(subtotal)
    total=subtotal+gst
    a=total+50
    return render(request, "ViewCart.html", {"data": data, "subtotal": subtotal,"gst":gst,"a":a})

def DeleteCart(request, id):
    data = ViewCart_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewCart/")

def MemberBooking(request,a,gst,subtotal):
    return render(request, 'MemberBooking.html',{"a":a,"gst":gst,"subtotal":subtotal})

def SaveBooking(request,subtotal,gst):
    if request.method == "POST":
        obj = MemberBooking_tbl()
        obj.memberid_id=request.session["userid"]

        obj.full = request.POST.get("full")
        obj.mobile = request.POST.get("mobile")
        obj.email = request.POST.get("email")
        obj.country = request.POST.get("country")
        obj.address = request.POST.get("address")
        obj.house = request.POST.get("house")
        obj.road = request.POST.get("road")
        obj.state = request.POST.get("state")
        obj.city = request.POST.get("city")
        obj.pincode = request.POST.get("pin")
        obj.near = request.POST.get("near")
        obj.con_name = request.POST.get("name")
        obj.con_mob =  request.POST.get("phone")
        obj.del_add = request.POST.get("new")
        obj.build = request.POST.get("add")
        obj.area = request.POST.get("area")
        obj.states = request.POST.get("state2")
        obj.town = request.POST.get("town")
        obj.code = request.POST.get("code")
        obj.place = request.POST.get("place")
        obj.product_totalprice= request.POST.get("total")
        obj.product_delivery_charge= request.POST.get("charge")
        obj.pay = request.POST.get("pay")


        obj.save()
        price = request.POST.get("total")
        pay = request.POST.get("pay")
        if pay == "upi":
            return render(request,"upi.html",{"price":price,"gst":gst,"subtotal":subtotal,"id":obj.id})
        elif pay == "net_banking":
            return render(request,"net_banking.html",{"price":price,"gst":gst,"subtotal":subtotal,"id":obj.id})
        elif pay == "cod":
            cart_items = ViewCart_tbl.objects.filter(memberid=request.session["userid"])

            # Iterate over cart items
            for cart_item in cart_items:
                # Extract required fields from cart item
                product_name = cart_item.Product_id.product_name
                product_image = cart_item.Product_id.product_images
                price = cart_item.Product_id.product_totalprice

                # Create an instance of the Booking model
                booking = Booking()

                # Set values to the Booking instance
                booking.booking_id = obj.id
                booking.product_name = product_name

                booking.price = price
                booking.Product_image = product_image

                # Save the Booking instance to the database
                booking.save()
            ViewCart_tbl.objects.filter(memberid=request.session["userid"]).delete()
            return render(request, "cod.html", {"price": price, "gst": gst, "subtotal": subtotal})



def AddFeedback(request):
    a = memberregistration_tbl.objects.get(id=request.session["userid"])
    return render(request,'AddFeedback.html',{"a": a})

def saveFeedback(request):
    if request.method == "POST":
        obj = Feedback_tbl()
        obj.memberid_id= request.session["userid"]
        obj.Name = request.POST.get("name")
        obj.Email = request.POST.get("email")
        obj.Message = request.POST.get("message")
        obj.star1= request.POST.get("rating1")
        obj.save()
        return redirect("/memberdashboard/")


def ViewFeedback(request):
    a = Feedback_tbl.objects.filter(memberid=request.session["userid"])
    return render(request, "ViewFeedback.html", {"a": a})


def Doctorhome(request):
    return render(request,"Doctorhome.html")

def DoctorViewMembers(request):
    data=memberregistration_tbl.objects.all()
    return  render(request,"DoctorViewMembers.html",{"data":data})

def add_doctor_member_report(request,id):
    d=member_health_details_tbl.objects.get(id=id)
    return render(request,"add_doctor_member_report.html",{"d":d})


def member_health_details(request):
    return render(request,"member_health_details.html")

def save_health_details(request):
    if request.method=="POST":
        if member_health_details_tbl.objects.filter(memberid=request.session["userid"]).exists():
            obj = member_health_details_tbl.objects.get(memberid=request.session["userid"])
            obj.heart_disease = request.POST.get("heart_disease")
            obj.joint_problem = request.POST.get("joint_problem")
            obj.bp = request.POST.get("bp")
            obj.height = request.POST.get("height")
            obj.weight = request.POST.get("weight")
            obj.dizziness = request.POST.get("dizziness")
            obj.save()
            return redirect("/memberdashboard/")
        else:
            obj=member_health_details_tbl()
            obj.memberid_id=request.session["userid"]
            obj.heart_disease=request.POST.get("heart_disease")
            obj.joint_problem=request.POST.get("joint_problem")
            obj.bp=request.POST.get("bp")
            obj.height=request.POST.get("height")
            obj.weight=request.POST.get("weight")
            obj.dizziness=request.POST.get("dizziness")
            obj.save()
            return redirect("/memberdashboard/")

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
def view_health_details(request):
    try:
        data=member_health_details_tbl.objects.get(memberid=request.session["userid"])
        return render(request,"view_health_details.html",{"data":data})

    except:
        return render(request,"view_health_details.html")

def view_doctor_health_details(request,id):
    try:
        data=member_health_details_tbl.objects.get(memberid=id)
        return render(request,"view_doctor_health_details.html",{"data":data})
    except:

        return render(request,"view_doctor_health_details.html")


def savemember_doctor_report(request,id):
    if request.method=="POST":

        obj=Doctor_Member_Report()
        o=doctor_tbl.objects.get(id=request.session["doctorid"])
        month=request.POST.get("month")
        if Doctor_Member_Report.objects.filter(month=month,health_id=id).exists():
            messages.error(request,"This month Report Already Added")
            return redirect("add_doctor_member_report", id=id)
        else:
            obj.email=request.POST.get("email")
            obj.month=month
            obj.health_id_id=id
            obj.name=request.POST.get("name")
            obj.Email=request.POST.get("email")
            obj.Contact=request.POST.get("phone")
            obj.current_height=request.POST.get("currentHeight")
            obj.previous_height=request.POST.get("previousHeight")
            obj.current_weight=request.POST.get("currentWeight")
            obj.previous_weight=request.POST.get("previousWeight")
            obj.medical_exam=request.POST.get("medical_exam")
            obj.medical_test=request.POST.get("medical_test")
            obj.overall_condition=request.POST.get("overall_condition")
            obj.instructions=request.POST.get("instructions")
            sig=request.FILES["signature"]
            fs=FileSystemStorage()
            filename=fs.save(sig.name,sig)
            fileurl=fs.url(filename)
            obj.signature=fileurl
            obj.save()
            messages.success(request, "This month Report Added")
            return redirect("/DoctorViewMembers/")


def view_doctor_member_report(request,id):
    data=memberregistration_tbl.objects.get(id=id)
    try:
        d=member_health_details_tbl.objects.get(memberid=id)
        data1=Doctor_Member_Report.objects.filter(health_id=d.id)
        return render(request,"view_doctor_member_report.html",{"data1":data1})
    except:
        return render(request, "view_doctor_member_report.html")



def view_trainer_member_report(request):
    data=AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request,"view_trainer_member_report.html",{"data":data})

def view_trainer_member_report1(request):
    if request.method=="POST":
        member=request.POST.get("member")
        print(member)
        try:
            d = member_health_details_tbl.objects.get(memberid=member)
            data1 = Doctor_Member_Report.objects.filter(health_id=d.id)
            return render(request,"view_trainer_member_report1.html",{"data1":data1})
        except:
            messages.error(request,"No Reports Found")
            return redirect("/view_trainer_member_report/")

def add_daily_report(request):
    return render(request,"add_daily_report.html")


def save_daily_report(request):
    if request.method=="POST":
        obj=workout_details()
        d=AssignTrainer_tbl.objects.get(memberid=request.session["userid"])
        trainer=d.trainer_id.id
        obj.Trainer_id_id=trainer
        obj.memberid_id=request.session["userid"]
        obj.Total_Workout=request.POST.get("total_workout")
        obj.Completed_Work_out=request.POST.get("completed")
        obj.Pending_Workout=request.POST.get("pending_workout")
        obj.Total_Time_Taken=request.POST.get("time_taken")
        obj.Date=request.POST.get("date")
        obj.save()
        return redirect("/memberdashboard/")

def view_daily_report(request):
    data=workout_details.objects.filter(memberid=request.session["userid"])
    return render(request,"view_daily_report.html",{"data":data})

def view_member_daily_report_trainer(request):
    data=workout_details.objects.filter(Trainer_id=request.session["trainerid"])
    return render(request,"view_member_daily_report_trainer.html",{"data":data})

def add_trainer_workout_report(request):
    data = AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request, "add_trainer_workout_report.html", {"data": data})

def generate_workout_report(request,id):
    data=memberregistration_tbl.objects.get(id=id)
    return render(request,"generate_workout_report.html",{"data":data})
import datetime
def autofill_report(request):
    month=request.GET.get("month")
    month_number = datetime.datetime.strptime(month, '%B').month
    m_id=request.GET.get("m_id")
    tws=0
    cws=0
    pws=0
    tts=0
    data=workout_details.objects.filter(memberid=m_id,Date__month=month_number)
    print(data)
    for i in data:
        tws+=i.Total_Workout
        cws+=i.Completed_Work_out
        pws+=i.Pending_Workout
        tts+=i.Total_Time_Taken
    return JsonResponse({"tws":tws,"cws":cws,"pws":pws,"tts":tts})
def save_monthly_report(request,id):
    data=Trainer_Member_Report()
    data.month=request.POST.get("month")
    data.memberid_id=id
    data.Trainer_id_id=request.session["trainerid"]
    data.Total_Workout = request.POST.get("total_workout")
    data.Completed_Work_out = request.POST.get("completed")
    data.Pending_Workout = request.POST.get("pending_workout")
    data.Total_Time_Taken = request.POST.get("time_taken")
    data.performance=request.POST.get("performance")
    data.save()
    return redirect("/Trainerhome/")

def member_view_overall_report(request):
    return render(request,"member_view_overall_report.html")

def member_overall_report_monthwise(request):
    month=request.POST.get("month")
    member=request.session["userid"]
    print(month,member)
    data2 = Trainer_Member_Report.objects.filter(memberid=member, month=month)
    try:
        d = member_health_details_tbl.objects.get(memberid=member)
        data1 = Doctor_Member_Report.objects.filter(health_id=d.id,month=month)
        print(data1,"ffffffffffff")
        return render(request, "member_overall_report_monthwise.html", {"data1": data1,"data2":data2})
    except:
        messages.error(request, "No Reports Found")
        return render(request, "member_overall_report_monthwise.html", {"data1": data1, "data2": data2})


def Trainer_For_Feedback(request):
    try:
        d=AssignTrainer_tbl.objects.get(memberid=request.session["userid"])
        trainer=d.trainer_id.id
        data=Trainer_tbl.objects.get(id=trainer)
        return render(request, "Trainer_For_Feedback.html", {"data": data})

    except:
        return render(request,"Trainer_For_Feedback.html")


def Save_trainer_feedback(request,id):
    if request.method=="POST":
        obj=Trainer_Feedback()
        obj.Trainer_id_id=id
        obj.memberid_id=request.session["userid"]
        obj.membername=request.POST.get("YName")
        obj.memberemail=request.POST.get("YEmail")
        obj.overall_exp=request.POST.get("experience")
        obj.behavior=request.POST.get("behavior")
        obj.helpfulness=request.POST.get("help")
        obj.comments=request.POST.get("comments")
        obj.save()
        return redirect("/memberdashboard/")
    
    
def view_admin_trainer_feedback(request):
    data=Trainer_tbl.objects.all()
    return render(request,"view_admin_trainer_feedback.html",{"data":data})

def view_admin_trainer_feedback1(request,id):
    d=Trainer_tbl.objects.get(id=id)
    data=Trainer_Feedback.objects.filter(Trainer_id=id)
    return render(request,"view_admin_trainer_feedback1.html",{"data":data,"d":d})

def generate_feedback_report(request,id):
    data=Trainer_tbl.objects.get(id=id)
    data1 = Trainer_Feedback.objects.filter(Trainer_id=id)
    exp_exce=0
    exp_good=0
    exp_avg=0
    exp_poor=0
    behavior_exce=0
    behavior_good=0
    behavior_avg=0
    behavior_poor=0

    help_exce = 0
    help_good = 0
    help_avg = 0
    help_poor = 0
    for i in data1:
        if i.overall_exp == "Excellent":
            exp_exce+=5
        elif i.overall_exp == "Good":
            exp_good+=4
        elif i.overall_exp == "Average":
            exp_avg+=3
        elif i.overall_exp == "Poor":
            exp_poor+=2
    for i in data1:
        if i.behavior == "Excellent":
            behavior_exce += 5
        elif i.behavior == "Good":
            behavior_good += 4
        elif i.behavior == "Average":
            behavior_avg += 3
        elif i.behavior == "Poor":
            behavior_poor += 2
    for i in data1:
        if i.helpfulness == "Excellent":
            help_exce += 5
        elif i.helpfulness == "Good":
            help_good += 4
        elif i.helpfulness == "Average":
            help_avg += 3
        elif i.helpfulness == "Poor":
            help_poor += 2

    total_overall_exp=exp_exce+exp_good+exp_avg+exp_poor
    total_behavior = behavior_exce + behavior_good + behavior_avg + behavior_poor
    total_helpfulness = help_exce + help_good + help_avg + help_poor
    seventy_percentage=total_overall_exp *0.75
    fifty_percentage = total_overall_exp * 0.50
    twentyfive_percentage = total_overall_exp * 0.25

    seventy_percentage = total_behavior * 0.75
    fifty_percentage = total_behavior * 0.50
    twentyfive_percentage = total_behavior * 0.25

    seventy_percentage = total_helpfulness * 0.75
    fifty_percentage = total_helpfulness * 0.50
    twentyfive_percentage = total_helpfulness * 0.25

    if total_overall_exp >=seventy_percentage:
        total_overall_exp="Excellent"
    elif total_overall_exp >= fifty_percentage and total_overall_exp < seventy_percentage :
            total_overall_exp = "Good"
    elif total_overall_exp >=twentyfive_percentage and total_overall_exp < fifty_percentage :
        total_overall_exp="Average"
    elif total_overall_exp < twentyfive_percentage:
        total_overall_exp="Poor"

    if total_behavior >=seventy_percentage:
        total_behavior="Excellent"
    elif total_behavior >= fifty_percentage and total_overall_exp < seventy_percentage :
            total_behavior = "Good"
    elif total_behavior >=twentyfive_percentage and total_overall_exp < fifty_percentage :
        total_behavior="Average"
    elif total_behavior < twentyfive_percentage:
        total_behavior="Poor"


    if total_helpfulness >=seventy_percentage:
        total_helpfulness="Excellent"
    elif total_helpfulness >= fifty_percentage and total_overall_exp < seventy_percentage :
            total_helpfulness = "Good"
    elif total_helpfulness >=twentyfive_percentage and total_overall_exp < fifty_percentage :
        total_helpfulness="Average"
    elif total_helpfulness < twentyfive_percentage:
        total_helpfulness="Poor"
    return render(request,"generate_feedback_report.html",{"total_helpfulness":total_helpfulness,
                                                          "total_behavior":total_behavior,
                                                           "total_overall_exp": total_overall_exp,"data":data})


def Save_trainer_feedback_report(request,id):
    if request.method=="POST":
        obj=Trainer_Feedback_Report()
        obj.total_overall_exp=request.POST.get("total_overall_exp")
        obj.total_helpfulness=request.POST.get("total_helpfulness")
        obj.total_behavior=request.POST.get("total_behavior")
        obj.instructions=request.POST.get("instructions")
        obj.Trainer_id_id=id
        obj.save()
        return redirect("/adminhome/")

def my_feedback_report(request):
    data=Trainer_Feedback_Report.objects.filter(Trainer_id=request.session["trainerid"])
    return render(request,"my_feedback_report.html",{"data":data})



def my_bookings(request):
    data=MemberBooking_tbl.objects.filter(memberid=request.session["userid"])
    return render(request,"my_bookings.html",{"data":data})

def admin_view_bookings(request):
    data = MemberBooking_tbl.objects.all()
    return render(request, "admin_view_bookings.html", {"data": data})

def Payment_success(request,price,id):
    cart_items = ViewCart_tbl.objects.filter(memberid=request.session["userid"])

    # Iterate over cart items
    for cart_item in cart_items:
        # Extract required fields from cart item
        product_name = cart_item.Product_id.product_name
        product_image = cart_item.Product_id.product_images
        price = cart_item.Product_id.product_totalprice

        # Create an instance of the Booking model
        booking = Booking()

        # Set values to the Booking instance
        booking.booking_id = id
        booking.product_name = product_name

        booking.price = price
        booking.Product_image = product_image

        # Save the Booking instance to the database
        booking.save()
    ViewCart_tbl.objects.filter(memberid=request.session["userid"]).delete()
    return render(request, "Payment_success.html", {"price": price})


def AdminLog(request):
    return render(request,'AdminLog.html')

def adminLogcheck(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        a=authenticate(request,username=username,password=password)
        if a is not None:
            return redirect('/adminhome/')
        else:
            return redirect('/AdminLog/')

def TrainerAddLeave(request,id):
    data = Trainer_tbl.objects.get(id=id)
    return render(request, "TrainerAddLeave.html",{"data":data})

def TrainerSaveLeave(request,id):
        if request.method == "POST":
            data = Leave_Tbl()
            data.trainer_id_id = id
            data.trainer_name = request.POST.get("Name")
            data.save()
            dates = request.POST.getlist("dates")
            print(dates)
            obj = leave_dates_tbl()
            for i in dates:
                obj = leave_dates_tbl()
                obj.leave_id_id = data.id
                obj.trainer_id_id = id
                obj.dates = i
                obj.save()
            return redirect("/LeaveMngt/")

def LeaveMngt(request):
    data = Trainer_tbl.objects.all()
    data1 = doctor_tbl.objects.all()
    return render(request,'LeaveMngt.html', {"data": data,"data1":data1})

def DoctorAddLeave(request,id):
    data=doctor_tbl.objects.get(id=id)
    return render(request, "DoctorAddLeave.html",{"data":data})

def DoctorSaveLeave(request,id):
        if request.method == "POST":
            data = Doctor_Leave_Tbl()
            data.doctor_id_id = id
            data.doctor_Name = request.POST.get("Name")
            data.save()
            dates = request.POST.getlist("dates")
            print(dates)
            obj = Doctor_leave_dates_tbl()
            for i in dates:
                obj = Doctor_leave_dates_tbl()
                obj.leave_id_id = data.id
                obj.doctor_id_id = id
                obj.dates = i
                obj.save()
            return redirect("/LeaveMngt/")


def TrainerAddSalary(request,id):
    data=Trainer_tbl.objects.get(id=id)
    return render(request,"TrainerAddSalary.html",{"data":data})

import calendar
import datetime
def month_wise_leave(request):
    month=request.GET.get("m")
    print(month,"month")
    s_id=request.GET.get("s_id")
    print(s_id,"id")
    month_number = datetime.datetime.strptime(month, '%B').month
    print(month_number,"monthnumber")
    t_leave=leave_dates_tbl.objects.filter(trainer_id=s_id,dates__month=month_number).count()
    total_days = calendar.monthrange(2023, month_number)[1]
    print(total_days,t_leave,"total_days","total_leave")
    t_working=total_days - t_leave
    print(t_working,"total_working")
    bp=Trainer_tbl.objects.get(id=s_id)
    sal=bp.trainer_Salary
    print(sal,"basic pay")
    one_day_salary=sal/30
    print(one_day_salary,"oneday")
    total_salary= one_day_salary * t_working
    print(total_salary,"totalsalary")
    if type(total_salary) == float:
        total_salary=int(total_salary)
    return JsonResponse({"t_leave":t_leave,"t_working":t_working,"t_salary":total_salary})

from django.contrib import messages


def Trainersavesalary(request,id):
    month=request.POST.get("month")
    if TrainerSalary_tbl.objects.filter(month=month,trainer_id=id).exists():
        messages.error(request,"This month salary already given")
        return redirect("TrainerAddSalary",id=id)

    else:
        obj=TrainerSalary_tbl()
        obj.total_working_days=request.POST.get("t_working")
        obj.trainer_id_id=id
        obj.month=request.POST.get("month")
        obj.total_salary=request.POST.get("t_working")
        obj.trainer_Name=request.POST.get("Name")
        obj.basic_pay=request.POST.get("basic_pay")
        obj.total_leave=request.POST.get("t_leave")
        obj.total_salary=request.POST.get("t_salary")
        obj.status="Salary Given"
        obj.save()
        return redirect("TrainerAddSalary",id=id)

def ViewTrainerSalary(request):
    data=TrainerSalary_tbl.objects.all()
    return render(request,"ViewTrainerSalary.html",{"data":data})


def AddDoctorSalary(request,id):
    data=doctor_tbl.objects.get(id=id)
    return render(request,"AddDoctorSalary.html",{"data":data})

import calendar
import datetime
def month_wise_leave_doctor(request):
    month=request.GET.get("m")
    print(month,"month")
    s_id=request.GET.get("s_id")
    print(s_id,"id")
    month_number = datetime.datetime.strptime(month, '%B').month
    print(month_number,"monthnumber")
    t_leave=Doctor_leave_dates_tbl.objects.filter(doctor_id=s_id,dates__month=month_number).count()
    total_days = calendar.monthrange(2023, month_number)[1]
    print(total_days,t_leave,"total_days","total_leave")
    t_working=total_days - t_leave
    print(t_working,"total_working")
    bp=doctor_tbl.objects.get(id=s_id)
    sal=bp.doctor_salary
    print(sal,"basic pay")
    one_day_salary=sal/30
    print(one_day_salary,"oneday")
    total_salary= one_day_salary * t_working
    print(total_salary,"totalsalary")
    if type(total_salary) == float:
        total_salary=int(total_salary)
    return JsonResponse({"t_leave":t_leave,"t_working":t_working,"t_salary":total_salary})

from django.contrib import messages


def Doctorsavesalary(request,id):
    month=request.POST.get("month")
    if DoctorSalary_tbl.objects.filter(month=month,doctor_id=id).exists():
        messages.error(request,"This month salary already given")
        return redirect("/LeaveMngt/")

    else:
        obj=DoctorSalary_tbl()
        obj.total_working_days=request.POST.get("t_working")
        obj.doctor_id_id=id
        obj.month=request.POST.get("month")
        obj.total_salary=request.POST.get("t_working")
        obj.doctor_Name=request.POST.get("Name")
        obj.basic_pay=request.POST.get("basic_pay")
        obj.total_leave=request.POST.get("t_leave")
        obj.total_salary=request.POST.get("t_salary")
        obj.status="Salary Given"
        obj.save()
        return redirect("/LeaveMngt/")

def ViewDoctorSalary(request):
    data=DoctorSalary_tbl.objects.all()
    return render(request,"ViewDoctorSalary.html",{"data":data})

def AddWorkOut(request):
    data=AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request, "AddWorkOut.html",{"data":data})

def SaveAddWorkOut(request):
    if request.method == "POST":
        w=week = request.POST.get("week")
        month=request.POST.get("month")
        m=request.POST.get("name")
        if workoutlist_tbl.objects.filter(month=month,week=w,memberid=m).exists():
            return HttpResponse("This Week is already assigned for this Member")
        else:

            obj=workoutlist_tbl()
            obj.month=month
            obj.trainer_id_id=request.session["trainerid"]
            obj.memberid_id=request.POST.get("name")
            obj.wrktype = request.POST.get("type")
            obj.week = request.POST.get("week")
            exc= request.POST.getlist("exc[]")
            print(exc,"css")

            reps = request.POST.getlist("rep[]")
            print(reps,"reps")
            obj.save()

            if len(exc) == len(reps):
                for exercise, repetitions in zip(exc, reps):
                    obj1 = Exercise_Name()
                    obj1.work_id_id = obj.id
                    obj1.excname = exercise
                    obj1.reps = repetitions
                    obj1.memberid_id=m
                    obj1.week=w
                    obj1.save()

            return redirect("/AddWorkOut/")
def ViewAddWorkOut(request):
    data = Trainer_tbl.objects.all()
    return render(request, "ViewAddWorkOut.html", {"data": data})
def EditAddWorkOut(request,id):
    data = Trainer_tbl.objects.get(id=id)
    return render(request, "EditAddWorkOut.html", {"data": data})

def updateAddWorkOut(request, id):
        obj = workoutlist_tbl.objects.get(id=id)
        obj.membername = request.POST.get("name")
        obj.wrktype = request.POST.get("type")
        obj.week = request.POST.get("week")
        obj.excname = request.POST.get("exc")
        obj.reps = request.POST.get("rep")
        obj.sets = request.POST.get("set")
        obj.save()
        return redirect("/AddWorkOut/")


def DeleteAddWorkOut(request, id):
    data = Trainer_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewAddWorkOut/")

def AddDietPlan(request):
    data=AssignTrainer_tbl.objects.filter(trainer_id=request.session["trainerid"])

    return render(request, "AddDietPlan.html",{"data":data})

def aboutus(request):
    return render(request, "aboutus.html")

def gallery(request):
    return render(request, "gallery.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def blogsingle(request):
    return render(request, "blogsingle.html")


def SalaryDetails(request):
    return render(request, "SalaryDetails.html")
def searchSalary(request):
    month=request.POST.get("mon")
    print(month,"mmmmmmm")
    data=TrainerSalary_tbl.objects.filter(month=month)
    data1=DoctorSalary_tbl.objects.filter(month=month)
    return render(request, "searchSalary.html", {"data": data,"data1":data1})

def view_trainer_salary(request):
    data=TrainerSalary_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request,"view_trainer_salary.html",{"data":data})

def doctor_view_salary(request):
    data=DoctorSalary_tbl.objects.filter(doctor_id=request.session["doctorid"])
    return render(request,"doctor_view_salary.html",{"data":data})

def Take_appointment(request):
    data = doctor_tbl.objects.all()
    data1=memberregistration_tbl.objects.get(id=request.session["userid"])
    return render(request,'Take_appointment.html',{"data": data,"data1":data1})

def SaveTake_appointment(request):
    if request.method == "POST":
        obj = Take_Appointment_tbl()
        obj.memberid_id =request.session["userid"]
        obj.doctor_id_id = request.POST.get("name")
        obj.reason=request.POST.get("reason")
        obj.membername=request.POST.get("mname")
        obj.date=request.POST.get("date")
        obj.time=request.POST.get("time")
        obj.status="Requested"
        obj.save()
        return redirect("/Take_appointment/")



def SaveDietPlan(request):
    if request.method == "POST":
        obj=AddDietPlan_tbl()
        obj.trainer_id_id=request.session["trainerid"]
        obj.memberid_id=request.POST.get("name")
        obj.day=request.POST.get("weekdays")
        obj.week = request.POST.get("week")
        obj.brkfst= request.POST.get("brk")
        obj.lunch= request.POST.get("lun")
        obj.snack = request.POST.get("sna")
        obj.dinner =request.POST.get("din")
        obj.save()
        return redirect("/AddDietPlan/")


def ordered_products(request,id):
    data=Booking.objects.filter(booking=id)
    return render(request,"ordered_products.html",{"data":data})

def DoctorViewAppointment(request):
    data = Take_Appointment_tbl.objects.filter(doctor_id=request.session["doctorid"])
    return render(request, "DoctorViewAppointment.html", {"data": data})

def appointment_confirmation(request,id):
    data=Take_Appointment_tbl.objects.get(id=id)
    data.status="Approved"
    data.save()
    email=data.memberid.email
    message=" your Appointment has confirmed"
    send_mail("Appointment Confirmation",message,settings.EMAIL_HOST_USER,[email])
    return redirect("/DoctorViewAppointment/")

def appointment_reject(request,id):
    data = Take_Appointment_tbl.objects.get(id=id)
    data.delete()
    return redirect("/DoctorViewAppointment/")

def ViewAppointment(request):
    data = Take_Appointment_tbl.objects.all()
    return render(request, "ViewAppointment.html", {"data": data})

def DeleteAppointment(request, id):
    data = Take_Appointment_tbl.objects.get(id=id)
    data.delete()
    return redirect("/ViewAppointment/")

def MemberViewTrainer(request):
    try:
        obj = AssignTrainer_tbl.objects.get(memberid=request.session["userid"])
        return render(request,'MemberViewTrainer.html',{"obj":obj})
    except:
        return render(request, 'MemberViewTrainer.html')


def AdminViewFeedback(request):
    a =Feedback_tbl.objects.all()
    return render(request, "AdminViewFeedback.html", {"a": a})

def Deleteproduct(request, id):
    data = MemberBooking_tbl.objects.get(id=id)
    data.delete()
    return redirect("/my_bookings/")
def ViewWorkOut(request):
    data=workoutlist_tbl.objects.filter(trainer_id=request.session["trainerid"])
    unique_combinations = {}

    for entry in data:
        key = (entry.memberid, entry.month)
        if key not in unique_combinations:
            unique_combinations[key] = entry

    # Extract the unique values from the dictionary to display in the template
    unique_data = list(unique_combinations.values())

    return render(request, "ViewWorkOut.html", {"data": unique_data})


def view_trainer_workout(request,id):
    data = workoutlist_tbl.objects.filter(trainer_id=request.session["trainerid"])
    d=workoutlist_tbl.objects.get(id=id)
    data1=Exercise_Name.objects.filter(memberid=d.memberid.id)
    return render(request,"view_trainer_workout.html",{"data":data,"data1":data1,"d":d})


def ViewDietPlan(request):
    diet_plans=AddDietPlan_tbl.objects.filter(trainer_id=request.session["trainerid"])
    return render(request,"ViewDietPlan.html",{"diet_plans":diet_plans})

def my_diet_plan(request):
    data=AddDietPlan_tbl.objects.filter(memberid=request.session["userid"])
    return render(request,"my_diet_plan.html",{"data":data})

def my_work_out_plan(request):
    data = workoutlist_tbl.objects.filter(memberid=request.session["userid"])
    unique_combinations = {}

    for entry in data:
        key = (entry.trainer_id, entry.month)
        if key not in unique_combinations:
            unique_combinations[key] = entry

    # Extract the unique values from the dictionary to display in the template
    unique_data = list(unique_combinations.values())
    return render(request, "my_work_out_plan.html", {"data": unique_data})
def view_member_workout(request,id):
    data = workoutlist_tbl.objects.filter(memberid=request.session["userid"])
    d = workoutlist_tbl.objects.get(id=id)
    data1 = Exercise_Name.objects.filter(memberid=d.memberid.id)
    return render(request, "view_member_workout.html", {"data": data, "data1": data1, "d": d})

def MemberViewSchedule(request):
    data = ScheduleTime_tbl.objects.filter(memberassigned__memberid=request.session["userid"])
    return render(request, "MemberViewSchedule.html", {"data": data})

def MemberViewEvent(request):
     data = Event_tbl.objects.all()
     return render(request, "MemberViewEvent.html", {"data": data})


# def MemberMonthlyPayment(request):
#     data = memberregistration_tbl.objects.get(id=request.session["userid"])
#     pdata=RegPayment_tbl.objects.get(memberid=data)
#     paid=data.package_type.package_price-pdata.balanceamount
#     print(data)
#     return render(request, "MemberMonthlyPayment.html",{"d": data,'pdata':pdata,'paid':paid})

# def SaveMemberMonthlyPayment(request):
#     if request.method == "POST":
#         data = memberregistration_tbl.objects.get(id=request.session["userid"])
#         bal=request.POST.get('balanceamount')
#         monthly=request.POST.get('monthlyPayment')
#         bal=int(bal)-int(monthly)
#         obj=RegPayment_tbl.objects.filter(memberid=data).update(balanceamount=bal)
#         return redirect("/MonthlyCardPayment/")


def CardPayment(request):
    return render(request, "CardPayment.html")



def MemberMonthlyPayment(request):
    print(request.session["userid"])
    p = RegPayment_tbl.objects.get(memberid=request.session["userid"])
    print(p.balanceamount,"pp")
    if RegPayment_tbl.objects.filter(memberid=request.session["userid"],status="Closed").exists():
        return render(request, "closed.html")
    else:
        data = memberregistration_tbl.objects.get(id=request.session["userid"])
        pdata=RegPayment_tbl.objects.get(memberid=data)
        paid=data.package_type.package_price-pdata.balanceamount
        print(data)
        return render(request, "MemberMonthlyPayment.html",{"pdata":pdata,"data":data,"paid":paid})


def SaveMemberMonthlyPayment(request,id):
    if request.method == "POST":
        obj=MonthlyFeePayment_tbl()
        mon=request.POST.get("monthlyPayment")
        d = RegPayment_tbl.objects.get(id=id)
        print(type(d.balanceamount))
        print(d.balanceamount)

        d = RegPayment_tbl.objects.get(id=id)
        d.paid_amount += int(mon)
        d.balanceamount -= int(mon)
        d.save()
        if d.balanceamount == 0:
            d.status = "Closed"
            d.save()
        pay=request.POST.get("pay")
        obj.pay=pay
        obj.reg_payment_id=id
        obj.memberid_id=request.session["userid"]
        obj.membername=request.POST.get("first_name")
        obj.email=request.POST.get("email")
        obj.package_type = request.POST.get("package_type")
        obj.totalamount= request.POST.get("totalamount")
        obj.totalpaid= d.paid_amount
        obj.monthlyPayment =request.POST.get("monthlyPayment")
        obj.month = request.POST.get("month")

        obj.balanceamount =d.balanceamount
        obj.save()



        if pay == "upi":
            return render(request,"Upipayment.html",{"payment":obj.monthlyPayment})
        elif pay == "net_banking":
            return render(request,"NetBankingPay.html",{"payment":obj.monthlyPayment})
        elif pay == "card":
            return render(request, "CardPayment.html", {"payment": obj.monthlyPayment})



def Payment_success_fees(request,payment):
    return render(request,"Payment_success_fees.html",{"payment":payment})


def ViewMemberMonthlyPayment(request):
    data = memberregistration_tbl.objects.all()
    return render(request, "ViewMemberMonthlyPayment.html", {"data":data})


def ViewMemberMonthlyPayment1(request,id):
    data = MonthlyFeePayment_tbl.objects.filter(memberid=id)
    return render(request, "ViewMemberMonthlyPayment1.html", {"data": data})


def MemberViewMonthlyPayment(request):
    data = MonthlyFeePayment_tbl.objects.filter(memberid=request.session["userid"])
    return render(request, "MemberViewMonthlyPayment.html", {"data": data})



def filter_by_category(request,id):
    data1 = Product_category_tbl.objects.all()
    data2=Products_tbl.objects.filter(product_category=id)
    return render(request,"memberviewproduct.html",{"data2":data2,"data1":data1})


def package_check(request):
    m=memberregistration_tbl.objects.get(id=request.session["userid"])
    from datetime import date
    p=m.expiry_date
    if p > date.today():
        return redirect("/package_not_expired/")
    else:
        return redirect("/package_booking/")

def package_not_expired(request):
    return render(request,"package_not_expired.html")

def package_booking(request):
    data=package_tbl.objects.all()
    m=memberregistration_tbl.objects.get(id=request.session["userid"])
    return render(request,"package_booking.html",{"data":data,"m":m})

def get_pack_details(request):
    pack=request.GET.get("p")
    d=package_tbl.objects.get(id=pack)
    price=d.package_price
    duration=d.package_duration
    return JsonResponse({"price":price,"duration":duration})


def save_package_booking(request):

    d=RegPayment_tbl.objects.get(memberid=request.session["userid"])
    d.memberid_id=request.session["userid"]
    d.membername=request.POST.get("name")
    d.totalamount=request.POST.get("totalamount")
    d.advanceamount=request.POST.get("advanceamount")

    d.monthlyPayment=request.POST.get("monthlyPayment")
    totalamount = request.POST.get("totalamount")
    advanceamount = request.POST.get("advanceamount")
    b = int(totalamount) - int(advanceamount)
    d.balanceamount = b
    d.save()
    duration=request.POST.get("duration")
    print(duration)
    m=memberregistration_tbl.objects.get(id=request.session["userid"])
    m.package_type_id=request.POST.get("package")
    from datetime import date, timedelta
    today = date.today()
    if duration == "3":
        print("hr")

        m.expiry_date = today + timedelta(days=90)
        m.save()
    elif duration == "6":
        print("hr")
        m.expiry_date = today + timedelta(days=180)
        m.save()
    m.save()
    return redirect("pack_payment",pay=advanceamount)

def pack_payment(request,pay):
    return render(request,"pack_payment.html",{"pay":pay})

def Payment_success_pack(request,pay):
    return render(request,"Payment_success_pack.html",{"pay":pay})