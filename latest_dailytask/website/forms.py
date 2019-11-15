from django  import forms


class FormProject(forms.Form):
    Pname = forms.CharField(max_length=400)
    Pdescription = forms.CharField(max_length=3000)
    Cname = forms.CharField(max_length=300)
    Cdetails = forms.CharField(max_length=4000)
    Pdeadline = forms.CharField(max_length=100)
    Pstartdate = forms.CharField(max_length=100)
    Pmanagedby = forms.CharField(max_length=400)
    Pcontract = forms.CharField(max_length=2000)
    Ptextresource = forms.CharField(max_length=6000)
    Pimage1=forms.ImageField()
    Pimage2  = forms.ImageField()
    Pimage3 =forms.ImageField()



    



class FormTask(forms.Form):
    Ttitle=forms.CharField(max_length=3000)
    Ttechnology = forms.CharField(max_length=3000)
    Tassignedto=forms.CharField(max_length=600)
    Tassignedby=forms.CharField(max_length=600)
    Tassigneddate=forms.CharField(max_length=600)
    Tdeadline = forms.CharField(max_length=400)



class FormTaskUpdate(forms.Form):

    Utitle = forms.CharField(max_length=3000)
    Udescription = forms.CharField(max_length=4000)
    Uempname = forms.CharField(max_length=4000)
    Uimg1 = forms.ImageField()
    Uimg2 = forms.ImageField()
    Uimg3 = forms.ImageField()


class FormLogin(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput)












