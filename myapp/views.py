from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import csv
import matplotlib.pyplot as plt


def my_form(request):
    # for doc in documents:
    #     doc.delete()
    message = 'Upload a CSV File'
    imgname = ""
    colheads = {}
    id = 0
    form = DocumentForm()
    # Handle file upload
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'])
                newdoc.save()
                id = newdoc.id
                colheads = selColumns(newdoc)
                # imgname = plotgraph(newdoc)
                # Redirect to the document list after POST
                # return redirect('my-form')
            else:
                message = 'The form is not valid. Fix the following error:'
        elif 'colselect' in request.POST:
            id = int(request.POST.get("newid"))
            newdoc = Document.objects.get(id=id)
            x = []
            x.append(int(request.POST.get("cols1")))
            x.append(int(request.POST.get("cols2")))
            imgname = plotgraph(newdoc, x)

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message, 'imgname': imgname, 'colheads': colheads, 'id': id}
    return render(request, 'list.html', context)


def plotgraph(doc, x):
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
    for i in x:
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


def selColumns(doc):
    colheads = {}
    with open(doc.docfile.path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            for i in range(len(row)):
                colheads[row[i]] = i
            break
    return colheads
    