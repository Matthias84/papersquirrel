from django import forms


class AddArticleForm(forms.Form):
    CHOICES_UA = (
        ('papersquirrel/0.1 (Linux; ) requests/2.22', 'Default'),
        ('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0', 'Firefox Desktop Browser'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Google Search Bot'), #https://support.google.com/webmasters/answer/1061943
    )
    download_url = forms.URLField(help_text="Enter a valid HTTP(s) URL, to grab this HTML page")
    useragent = forms.ChoiceField(choices = CHOICES_UA)
    # TODO: Validators
