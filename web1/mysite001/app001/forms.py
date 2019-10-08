from django import forms

class nameForm(forms.Form):
    name1=forms.CharField() #检查提交的name1值是否为字符串