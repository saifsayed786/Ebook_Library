from django.dispatch import receiver
from .models import Document
from django.db.models.signals import pre_save,post_save,post_delete
import os
import nltk
import slate3k as slate
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from celery.task import task
import fitz
from pathlib import Path
# @receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.eBookFile:
        if os.path.isfile(instance.eBookFile.path):
            os.remove(instance.eBookFile.path)
post_delete.connect(auto_delete_file_on_delete,sender=Document)


# @receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).eBookFile
    except Document.DoesNotExist:
        return False

    new_file = instance.eBookFile 
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)  
pre_save.connect(auto_delete_file_on_change,sender=Document)
# @receiver(models.signals.post_save, sender=Document)
from django.dispatch.dispatcher import Signal
def reducer(self):
    return (Signal, (self.providing_args,))
Signal.__reduce__ = reducer

@task(ignore_result=True)
def eBookData_after_save(sender,instance,created,**kwargs):   
    new_file = instance.eBookFile.path
    doc = fitz.open(new_file)
    page = doc.loadPage(0) #number of page
    pix = page.getPixmap(matrix=fitz.Matrix(150/72,150/72))
    output = new_file+".png"
    image = pix.writePNG(output)
    Document.objects.filter(id=instance.pk).update(thumbnail=output)
    cleaned_data = []
    with open(new_file,mode='rb') as pdfFile:
        extracted_pdf_text = slate.PDF(pdfFile)
        data=[]
        for  s in extracted_pdf_text:
            tokens = word_tokenize(s)
            tokens = [w.lower() for w in tokens]
            table = s.maketrans('', '', """!"#$%&'()*+,./:;<=>?@[\]^_`{|}~“”’‘""")
            #print(table)
            stripped = [w.translate(table) for w in tokens]
            stop_words = stopwords.words('english')
            words = [w for w in stripped if not w in stop_words]
            cleaned_data.extend(set(words))
            data = ' '.join(list(set(cleaned_data)))
            Document.objects.filter(id=instance.pk).update(eBookData=data)
post_save.connect(eBookData_after_save.delay,sender=Document)
