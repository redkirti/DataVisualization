from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import csv
import matplotlib.pyplot as plt


def my_form(request):
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            imgname = plotgraph(newdoc)
            # Redirect to the document list after POST
            # return redirect('my-form')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        imgname = ""
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    for doc in documents:
        doc.delete()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message, 'imgname': imgname}
    return render(request, 'list.html', context)


def plotgraph(doc):
    I = {}
    M = []
    plt.figure(figsize=(10,8))
    rowNum = 0
    with open(doc.docfile.path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='"')
        for row in csvreader:
            rowNum += 1
            if (rowNum == 1):
                count = len(row)
                for i in range(len(row)):
                    I[row[i]] = i
                continue
            else:
                M.append(row)

    col = []
    for i in range (1,count):
        temp = list(map(lambda r: r[i], M))
        temp = list(map(lambda x: float(x), temp))
        col.append(temp)

    plt.subplot(2, 1, 1);
    plt.plot(col[0], col[1], ls='solid', color='blue', marker='o', markersize=9, mew=2, linewidth=2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    imgname = doc.docfile.path+".png"
    print(imgname)
    plt.savefig(imgname)
    imgname = doc.docfile.url+".png"
    return imgname