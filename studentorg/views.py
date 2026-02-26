from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import (
    OrganizationForm,
    OrgMemberForm,
    StudentForm,
    CollegeForm,
    ProgramForm,
)


# =========================
# HOME
# =========================
class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in our custom summary counts
        context['college_count'] = College.objects.count()
        context['program_count'] = Program.objects.count()
        context['organization_count'] = Organization.objects.count()
        context['student_count'] = Student.objects.count()
        context['org_member_count'] = OrgMember.objects.count()
        return context


# =========================
# ORGANIZATION
# =========================
class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")


# =========================
# ORG MEMBER
# =========================
class OrgMemberList(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"
    paginate_by = 5


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmember_del.html"
    success_url = reverse_lazy("orgmember-list")


# =========================
# STUDENT
# =========================
class StudentList(ListView):
    model = Student
    template_name = "student_list.html"
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_del.html"
    success_url = reverse_lazy("student-list")


# =========================
# COLLEGE
# =========================
class CollegeList(ListView):
    model = College
    template_name = "college_list.html"
    paginate_by = 5


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")


# =========================
# PROGRAM
# =========================
class ProgramList(ListView):
    model = Program
    template_name = "program_list.html"
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy("program-list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "program_del.html"
    success_url = reverse_lazy("program-list")