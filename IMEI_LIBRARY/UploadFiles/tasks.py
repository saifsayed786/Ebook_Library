# from .models import Document
# import os
# import nltk
# import slate3k as slate
# from nltk.tokenize import word_tokenize
# import string
# from nltk.corpus import stopwords
# from celery import shared_task

# @shared_task()
# def after_save_task():
#     new_file = instance.eBookFile.path

#     cleaned_data = []
#     with open(new_file,mode='rb') as pdfFile:
#         extracted_pdf_text = slate.PDF(pdfFile)
#         data=[]
#         for  s in extracted_pdf_text:
#             tokens = word_tokenize(s)
#             tokens = [w.lower() for w in tokens]
#             table = s.maketrans('', '', """!"#$%&'()*+,./:;<=>?@[\]^_`{|}~“”’‘""")
#             #print(table)
#             stripped = [w.translate(table) for w in tokens]
#             stop_words = stopwords.words('english')
#             words = [w for w in stripped if not w in stop_words]
#             cleaned_data.extend(set(words))
#             data = ' '.join(list(set(cleaned_data)))
#             Document.objects.filter(id=instance.pk).update(eBookData=data)