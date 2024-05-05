from django.forms import ModelForm
from .models import *


class ArticleForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
