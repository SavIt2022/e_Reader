from django.urls import path


from.views import * 
from django.conf import settings
from django.conf.urls.static import static

from homepage import views

appname="homepage"
urlpatterns=[
   
    path('course-profile/<int:id>/',course,name='course-profile'),
    path('xhome',xhome, name='xhome'),
    path('grades',grades, name='grades'),
    path('payments',payments, name='payments'),
    path('subjects',subjects, name='subjects'),
    path('courses',courses_list, name='courses_list'),
    path('admin_dashboard',admin_dashboard, name='admin_dashboard'),
    path('school_admin_dashboard',school_admin_dashboard, name='school_admin_dashboard'),
    path('add',add_course,name='add_course'),
    path('edit/<int:id>/',edit_course, name='edit_course'),


    path('grade1',grade1_course_list, name="grade1_course_list"),
    path('addgrade1',add_grade1_course,name='add_grade1_course'),
    path('editgrade1/<int:id>/',edit_grade1_course, name='edit_grade1_course'),

    path('grade2',grade2_course_list, name="grade2_course_list"),
    path('addgrade2',add_grade2_course,name='add_grade2_course'),
    path('editgrade2/<int:id>/',edit_grade2_course, name='edit_grade2_course'),

    path('grade3',grade3_course_list, name="grade3_course_list"),
    path('addgrade3',add_grade3_course,name='add_grade3_course'),
    path('editgrade3/<int:id>/',edit_grade3_course, name='edit_grade3_course'),

    path('grade4',grade4_course_list, name="grade4_course_list"),
    path('addgrade4',add_grade4_course,name='add_grade4_course'),
    path('editgrade4/<int:id>/',edit_grade4_course, name='edit_grade4_course'),

    path('grade5',grade5_course_list, name="grade5_course_list"),
    path('addgrade5',add_grade5_course,name='add_grade5_course'),
    path('editgrade5/<int:id>/',edit_grade5_course, name='edit_grade5_course'),

    path('grade6',grade6_course_list, name="grade6_course_list"),
    path('addgrade6',add_grade6_course,name='add_grade6_course'),
    path('editgrade6/<int:id>/',edit_grade6_course, name='edit_grade6_course'),

    path('grade7',grade7_course_list, name="grade7_course_list"),
    path('addgrade7',add_grade7_course,name='add_grade7_course'),
    path('editgrade7/<int:id>/',edit_grade7_course, name='edit_grade7_course'),

    path('grade8',grade8_course_list, name="grade8_course_list"),
    path('addgrade8',add_grade8_course,name='add_grade8_course'),
    path('editgrade8/<int:id>/',edit_grade8_course, name='edit_grade8_course'),



    ]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
