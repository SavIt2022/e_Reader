
from django import forms
from.models import *
class CourseAdditionForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"
class GradeOneCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeOne
        fields="__all__"
class GradeTwoCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeTwo
        fields="__all__"
class GradeThreeCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeThree
        fields="__all__"

class GradeFourCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeFour
        fields="__all__"
class GradeFiveCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeFive
        fields="__all__"
class GradeSixCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeSix
        fields="__all__"
class GradeSevenCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeSeven
        fields="__all__"
class GradeEightCourseAdditionForm(forms.ModelForm):
    class Meta:
        model=GradeEight
        fields="__all__"