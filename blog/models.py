
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def mail_validator(value):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@snu.ac.kr$', value):
        raise ValidationError('snu.ac.kr로 끝나는 "스누메일"을 적어주세요')

class Tag(models.Model):
    name_tag = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name_tag

class Core(models.Model):
    name_core = models.CharField(max_length=20, help_text='Root (English)')
    kr_name_core = models.CharField(max_length=20, help_text='대분류 (한국어)')
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name_core


class Category(models.Model):
    name_category = models.CharField(max_length=20, help_text='Club Category (English)')
    kr_name_category = models.CharField(max_length=20, help_text='분과명 (한국어)')
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    #count = models.IntegerField()
    root = models.ForeignKey(Core, on_delete=models.CASCADE, null=True)


    #카테고리 이름이 object 이름으로 반영됨.
    def __str__(self):
        return self.name_category



class Dongari(models.Model):
    name_dongari = models.CharField(default="name", max_length=100, blank=False, help_text='Club Name(English)')
    kr_name_dongari = models.CharField(default="name", max_length=100, blank=False, help_text='동아리명 (한국어)')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    description = models.TextField(help_text='동아리에 대한 소개')
    # email = models.CharField(max_length=50, blank=False,
    #     validators=[mail_validator], help_text='스누메일')
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag') #이게 문자열로도 지정 가능하다. ('Tag') vs. (Tag).
                                            #For latter case, the "Tag" class MUST be defined before this (Dongari) class

    def __str__(self):
        return self.name_dongari
