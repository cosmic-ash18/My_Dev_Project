from django import forms

LANG_CHOICES = [
    # Second name is what is seen in the dropdown
    ('cpp', 'C++'),
    ('py', 'Python'),
    ('java', 'Java'),
    ('c', 'C')
]


class CodeSubmissionForm(forms.Form):
    language = forms.ChoiceField(choices=LANG_CHOICES,
        widget =forms.Select(attrs={'class':'form-select'}))
    code = forms.CharField(
        widget = forms.Textarea(attrs={'rows':15,'class':'form-control','placeholder':'Write your code here...'}),
        label = 'Source Code'
    )
    stdin = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows':5, 'class':'form-control','placeholder':'Custom input (stdin)'}),
        label = 'Custom Input'
    )