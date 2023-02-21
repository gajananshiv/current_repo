from django.contrib import admin
from .models import Csv
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
# Register your models h

class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()

class CsvAdmin(admin.ModelAdmin):
    list_display = ('BANKNIFTY','OPEN','HIGH','LOW','CLOSE','VOLUME')
    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csv/',self.upload_csv),]
        return new_urls+urls
    def upload_csv(self,request):
        if request.method=='POST':
            csv_file=request.FILES['csv_upload']
            if not csv_file.name.endswith('.csv'):
                messages.warning(request,'The wrong file uploading')
                return HttpResponseRedirect(request.path_info)
            file_data=csv_file.read().decode('utf-8')
            csv_data=file_data.split('\n')

            for x in csv_data:
                fields=x.split(',')
                Created = Csv.objects.update_or_create(BANKNIFTY=fields[0],


                    OPEN=fields[1],
                    HIGH=fields[2],
                    LOW=fields[3],
                    CLOSE=fields[4],
                    VOLUME=fields[5],
                   )

        form=CsvImportForm()
        data={'form':form}
        return render(request,'admin/csv_upload.html',data)



admin.site.register(Csv,CsvAdmin)