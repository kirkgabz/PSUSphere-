from django.contrib import admin
from django.urls import path

from studentorg.views import (
    HomePageView,
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,

    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"),

    # Organization
    path("organization_list/", OrganizationList.as_view(), name="organization-list"),
    path("organization_list/add/", OrganizationCreateView.as_view(), name="organization-add"),
    path("organization_list/<pk>/", OrganizationUpdateView.as_view(), name="organization-update"),
    path("organization_list/<pk>/delete/", OrganizationDeleteView.as_view(), name="organization-delete"),

    # OrgMember
    path("orgmember_list/", OrgMemberList.as_view(), name="orgmember-list"),
    path("orgmember_list/add/", OrgMemberCreateView.as_view(), name="orgmember-add"),
    path("orgmember_list/<pk>/", OrgMemberUpdateView.as_view(), name="orgmember-update"),
    path("orgmember_list/<pk>/delete/", OrgMemberDeleteView.as_view(), name="orgmember-delete"),

    # Student
    path("student_list/", StudentList.as_view(), name="student-list"),
    path("student_list/add/", StudentCreateView.as_view(), name="student-add"),
    path("student_list/<pk>/", StudentUpdateView.as_view(), name="student-update"),
    path("student_list/<pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

    # College
    path("college_list/", CollegeList.as_view(), name="college-list"),
    path("college_list/add/", CollegeCreateView.as_view(), name="college-add"),
    path("college_list/<pk>/", CollegeUpdateView.as_view(), name="college-update"),
    path("college_list/<pk>/delete/", CollegeDeleteView.as_view(), name="college-delete"),

    # Program
    path("program_list/", ProgramList.as_view(), name="program-list"),
    path("program_list/add/", ProgramCreateView.as_view(), name="program-add"),
    path("program_list/<pk>/", ProgramUpdateView.as_view(), name="program-update"),
    path("program_list/<pk>/delete/", ProgramDeleteView.as_view(), name="program-delete"),
]