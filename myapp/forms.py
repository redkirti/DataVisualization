from django import forms
from .models import Document

# documents = Document.objects.all()
# for document in documents:
#     doc = document
# colheads = {}
# with open(doc.docfile.path, newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
#     for row in csvreader:
#         for i in range(len(row)):
#             colheads.append((i, row[i]))
#         break

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')

# class ColumnForm(forms.Form):
#     column1 = forms.ChoiceField(choices=colheads, label='Select a column')
#     column2 = forms.ChoiceField(choices=colheads, label='Select a column')