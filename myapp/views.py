from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import csv
import matplotlib.pyplot as plt


def my_form(request):
    imgname = ""
    colheads = {}
    graph = None
    csep = None
    cid = 0
    form = DocumentForm()
    # Handle file upload
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'], tag=request.POST['tag']) 
                newdoc.save()
                cid = newdoc.id
                graph = 1234
                # imgname = plotgraph(newdoc)
                # Redirect to the document list after POST
                # return redirect('my-form')
            else:
                message = 'The form is not valid. Fix error:'
        elif 'graphselect' in request.POST:
            cid = int(request.POST.get("newid"))
            graph = int(request.POST.get("graph"))
            csep = int(request.POST.get("csep"))

            newdoc = Document.objects.get(id=cid)
            colheads = selColumns(newdoc,csep)
        elif 'colselect' in request.POST:
            cid = int(request.POST.get("newid"))
            graph = int(request.POST.get("newgraph"))
            csep = int(request.POST.get("csep"))
            newdoc = Document.objects.get(id=cid)
            x = []
            x.append(int(request.POST.get("cols1")))
            x.append(int(request.POST.get("cols2")))
            imgname = plotgraph(newdoc, x, graph, csep)
        elif 'exampleset' in request.POST:
            cid = int(request.POST.get("exampleset"))
            graph = 1234

    # Load documents for the list page
    documents = Document.objects.all()
    # for doc in documents:
    #     doc.delete()
    # Render list page with the documents and the form
    context = {
        'documents': documents, 
        'form': form,
        'imgname': imgname, 
        'colheads': colheads, 
        'id': cid, 
        'graph': graph,
        'csep' : csep
        }
    return render(request, 'list.html', context)


def plotgraph(doc, x, graph, sep):
    I = {}
    M = []
    if(sep==1):
        d = ' '
    elif(sep==2):
        d = ','
    elif(sep==3):
        d = '   '
    elif(sep==4):
        d = ';'
    elif(sep==5):
        d = ':'
    elif(sep==6):
        d = '-'
    else:
        d = ' '
    plt.figure(figsize=(10,8))
    rowNum = 0
    with open(doc.docfile.path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=d, quotechar='"')
        for row in csvreader:
            rowNum += 1
            if (rowNum == 1):
                count = len(row)
                for i in range(len(row)):
                    I[row[i]] = i
                continue
            else:
                M.append(row)
    labels = list(I.keys())
    col = []
    plt.subplot(2, 1, 1)
    if(graph == 1):
        for i in x:
            temp = list(map(lambda r: r[i], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
        plt.plot(col[0], col[1], ls='solid', color='blue', marker='o', markersize=9, mew=2, linewidth=2)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
    elif(graph == 2):
        for i in x:
            if(i==0):
                temp = list(map(lambda r: r[i], M))
                col.append(temp)
                continue
            temp = list(map(lambda r: r[i], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
        plt.bar(col[0], col[1], color='maroon', width=0.4)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
    elif(graph == 3):
        for i in x:
            temp = list(map(lambda r: r[i], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
        plt.hist(col[1], col[0], facecolor='blue', alpha=0.5)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1]) 
    else:
        for i in x:
            if(i==0):
                temp = list(map(lambda r: r[i], M))
                col.append(temp)
                continue
            temp = list(map(lambda r: r[i], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
        plt.pie(col[1], labels = col[0])
    imgname = doc.docfile.path+".png"
    print(imgname)
    plt.savefig(imgname, bbox_inches='tight')
    imgname = doc.docfile.url+".png"
    return imgname


def selColumns(doc, sep):
    colheads = {}
    if(sep==1):
        d = ' '
    elif(sep==2):
        d = ','
    elif(sep==3):
        d = '   '
    elif(sep==4):
        d = ';'
    elif(sep==5):
        d = ':'
    elif(sep==6):
        d = '-'
    else:
        d = ' '
    with open(doc.docfile.path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=d, quotechar='"')
        for row in csvreader:
            for i in range(len(row)):
                colheads[row[i]] = i
            break
    return colheads
    