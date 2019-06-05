from django import forms
    
class AddArticleForm(forms.Form):
    download_url = forms.URLField(help_text="Enter a valid HTTP(s) URL, to grab this HTML page")
    # TODO: Validators
