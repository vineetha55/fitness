from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('adminlogin/',views.adminlogin),
    path('admincheck/',views.admincheck),

    path('AdminLog/',views.AdminLog),
    path('adminLogcheck/',views.adminLogcheck),
    path('adminhome/',views.adminhome),


    #trainer

    path('AddTrainer/',views.AddTrainer),
    path('saveTrainer/',views.saveTrainer),
    path('ViewTrainer/',views.ViewTrainer),
    path('EditTrainer/<id>',views.EditTrainer),
    path('updateTrainer/<id>',views.updateTrainer),
    path('DeleteTrainer/<id>',views.DeleteTrainer),

    #doctor

    path('AddDoctor/',views.AddDoctor),
    path('saveDoctor/',views.saveDoctor),
    path('ViewDoctor/',views.ViewDoctor),
    path('EditDoctor/<id>',views.EditDoctor),
    path('updateDoctor/<id>',views.updateDoctor),
    path('DeleteDoctor/<id>',views.DeleteDoctor),

    #package

    path('AddPackage/',views.AddPackage),
    path('savepackage/',views.savepackage),
    path('ViewPackage/',views.ViewPackage),
    path('Editpackage/<id>',views.Editpackage),
    path('updatepackage/<id>',views.updatepackage),
    path('Deletepackage/<id>',views.Deletepackage),

    #adding events

    path('AddEvent/',views.AddEvent),
    path('SaveEvent/',views.SaveEvent),
    path('ViewEvent/',views.ViewEvent),
    path('EditEvent/<id>',views.EditEvent),
    path('UpdateEvent/<id>',views.UpdateEvent),
    path('DeleteEvent/<id>',views.DeleteEvent),

    path('AddCategory/',views.AddCategory),
    path('SaveCategory/',views.SaveCategory),
    path('ViewCategory/',views.ViewCategory),
    path('EditCategory/<id>',views.EditCategory),
    path('UpdateCategory/<id>',views.UpdateCategory),
    path('DeleteCategory/<id>',views.DeleteCategory),

    #products

    path('AddProduct/',views.AddProduct),
    path('SaveProduct/',views.SaveProduct),
    path('ViewProduct/',views.ViewProduct),
    path('EditProduct/<id>',views.EditProduct),
    path('UpdateProduct/<id>',views.UpdateProduct),
    path('DeleteProduct/<id>',views.DeleteProduct),

    #member registration

    path('memberregistration/',views.memberregistration),
    path('savememberregistration/',views.savememberregistration),
    path('memberdashboard/',views.memberdashboard),
    path('MemberPayment/<id>',views.MemberPayment,name="MemberPayment"),
    path("find_duration/",views.find_duration),
    path('SavePayment/<id>',views.SavePayment),

    #admin view member

    path('viewmemberregistration/',views.viewmemberregistration),
    path('DeleteMember/<id>',views.DeleteMember),

    #trainer

    path('Trainerhome/',views.Trainerhome),

    # admin assigning trainer

    path('AssignTrainer/<id>',views.AssignTrainer),
    path('saveAssignTrainer/<id>',views.saveAssignTrainer),

    #trainer view assigned member

    path('TrainerViewAssignedMember/',views.TrainerViewAssignedMember),

    #shedule time

    path('AddSchedule/',views.AddSchedule),
    path('SaveSchedule/',views.SaveSchedule),
    path('ViewSchedule/',views.ViewSchedule),
    path('EditSchedule/<id>',views.EditSchedule),
    path('UpdateSchedule/<id>',views.UpdateSchedule),
    path('DeleteSchedule/<id>',views.DeleteSchedule),

#membercart

    path('memberviewproduct/',views.memberviewproduct),
    path('SaveCart/<id>',views.SaveCart),
    path('ViewCart/',views.ViewCart),
    path('DeleteCart/<id>',views.DeleteCart),


    path('AddFeedback/',views.AddFeedback),
    path('saveFeedback/', views.saveFeedback),
    path('ViewFeedback/', views.ViewFeedback),
    path('AdminViewFeedback/',views.AdminViewFeedback),

    path('MemberBooking/<a>/<gst>/<subtotal>',views.MemberBooking),
    path("SaveBooking/<subtotal>/<gst>",views.SaveBooking),

    #doctor home
    path("Doctorhome/",views.Doctorhome),
    path("DoctorViewMembers/",views.DoctorViewMembers),
    path("add_doctor_member_report/<id>",views.add_doctor_member_report,name="add_doctor_member_report"),

    #memberhealth
    path("member_health_details/",views.member_health_details),
    path("save_health_details/",views.save_health_details),
    path("view_health_details/",views.view_health_details),
    path("view_doctor_health_details/<id>",views.view_doctor_health_details),
    path("savemember_doctor_report/<id>",views.savemember_doctor_report),
    path("view_doctor_member_report/<id>",views.view_doctor_member_report),


    #trainerviewreport
    path("view_trainer_member_report/",views.view_trainer_member_report),
    path("view_trainer_member_report1/",views.view_trainer_member_report1),
    path("add_trainer_workout_report/",views.add_trainer_workout_report),
    path("generate_workout_report/<id>",views.generate_workout_report),
    path("autofill_report/",views.autofill_report),
    path("save_monthly_report/<id>",views.save_monthly_report),

    #daily report

    path("add_daily_report/",views.add_daily_report),
    path("save_daily_report/",views.save_daily_report),
    path("view_daily_report/",views.view_daily_report),


    path("view_member_daily_report_trainer/",views.view_member_daily_report_trainer),
    path("member_view_overall_report/",views.member_view_overall_report),
    path("member_overall_report_monthwise/",views.member_overall_report_monthwise),

    #feedback for trainer
    path("Trainer_For_Feedback/",views.Trainer_For_Feedback),
    path("Save_trainer_feedback/<id>",views.Save_trainer_feedback),
    path("view_admin_trainer_feedback/",views.view_admin_trainer_feedback),
    path("view_admin_trainer_feedback1/<id>",views.view_admin_trainer_feedback1),
    path("generate_feedback_report/<id>",views.generate_feedback_report),
    path("Save_trainer_feedback_report/<id>",views.Save_trainer_feedback_report),
    path("my_feedback_report/",views.my_feedback_report),



    path("my_bookings/",views.my_bookings),
    path("admin_view_bookings/",views.admin_view_bookings),
    path("Payment_success/<price>/<id>",views.Payment_success),

    path('TrainerAddLeave/<id>',views.TrainerAddLeave),
    path('TrainerSaveLeave/<id>',views.TrainerSaveLeave),
    path('LeaveMngt/',views.LeaveMngt),
    path('DoctorAddLeave/<id>',views.DoctorAddLeave),
    path('DoctorSaveLeave/<id>',views.DoctorSaveLeave),

    #Salary Trainer

    path('TrainerAddSalary/<id>',views.TrainerAddSalary,name="TrainerAddSalary"),
    path('Trainersavesalary/<id>',views.Trainersavesalary),
    path('ViewTrainerSalary/',views.ViewTrainerSalary),
    path("month_wise_leave/",views.month_wise_leave),
    path("month_wise_leave_doctor/",views.month_wise_leave_doctor),


    # Salary Doctor

    path('AddDoctorSalary/<id>',views.AddDoctorSalary),
    path('Doctorsavesalary/<id>',views.Doctorsavesalary),
    path('ViewDoctorSalary/',views.ViewDoctorSalary),

    #workoutlist added by trainer

    path('AddWorkOut/',views.AddWorkOut),
    path('SaveAddWorkOut/',views.SaveAddWorkOut),
    path('ViewAddWorkOut/', views.ViewAddWorkOut),
    path('EditAddWorkOut/<id>', views.EditAddWorkOut),
    path('updateAddWorkOut/<id>', views.updateAddWorkOut),
    path('DeleteAddWorkOut/<id>', views.DeleteAddWorkOut),

    #Diet plan

    path('AddDietPlan/',views.AddDietPlan),
    path('SaveDietPlan/',views.SaveDietPlan),
    #path('ViewDietPlan/', views.ViewDietPlan),
    #path('EditDietPlan/<id>', views.EditDietPlan),
    #path('updateDietPlan/<id>', views.updateDietPlan),
    #path('DeleteDietPlan/<id>', views.DeleteDietPlan),


    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('gallery/',views.gallery),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('blogsingle/',views. blogsingle),
    path('SalaryDetails/',views.SalaryDetails),
    path('searchSalary/',views.searchSalary),
    path('view_trainer_salary/',views.view_trainer_salary),
    path('doctor_view_salary/',views.doctor_view_salary),

    path('Take_appointment/',views.Take_appointment),
    path('SaveTake_appointment/',views.SaveTake_appointment),
    path("ordered_products/<id>",views.ordered_products),
    path('DoctorViewAppointment/',views.DoctorViewAppointment),
    path("appointment_confirmation/<id>",views.appointment_confirmation),
    path("appointment_reject/<id>",views.appointment_reject),
    path('ViewAppointment/',views.ViewAppointment),
    path('DeleteAppointment/<id>', views.DeleteAppointment),
    path('MemberViewTrainer/',views.MemberViewTrainer),
    path('Deleteproduct/<id>', views.Deleteproduct),
    path("ViewWorkOut/",views.ViewWorkOut),
    path("view_trainer_workout/<id>",views.view_trainer_workout),
    path("ViewDietPlan/",views.ViewDietPlan),
    path("my_diet_plan/",views.my_diet_plan),
    path("my_work_out_plan/",views.my_work_out_plan),
    path("view_member_workout/<id>",views.view_member_workout),
    path("MemberViewSchedule/",views.MemberViewSchedule),
    path("MemberViewEvent/",views.MemberViewEvent),


]