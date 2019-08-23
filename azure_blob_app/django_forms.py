from django import forms


class UserDetails_Form(forms.Form):
    """
        we are using empty django forms just to convert existing HTML code to django forms
    """
    pass
    # We can you this approach too
    # prefix = 'userdetails_form'
    # customernameHelp = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Customer Name', 'id': "customername", 'aria - describedby': "customernameHelp",
    #            'class ': 'form-control'}))
    # generateuniqueid = forms.CharField(widget=forms.TextInput(
    #     attrs={'placeholder': 'Generate Unique ID', 'id': "generateuniqueid", 'aria - describedby': "generateuniqueid",
    #            'class ': 'form-control'}))
