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
            print(graph)
            csep = int(request.POST.get("csep"))

            newdoc = Document.objects.get(id=cid)
            colheads = selColumns(newdoc,csep)
        elif 'colselect' in request.POST:
            cid = int(request.POST.get("newid"))
            graph = int(request.POST.get("newgraph"))
            print("HELLO" + str(graph))
            csep = int(request.POST.get("csep"))
            newdoc = Document.objects.get(id=cid)
            x = []
            y = selColumns(newdoc,csep)
            for i in range(len(y)):
                s = "cols"+str(i)
                x.append(int(request.POST.get(s)))
            print("HELLO")
            for i in x:
                print(i)
            # x.append(int(request.POST.get("cols1")))
            # x.append(int(request.POST.get("cols2")))
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
    colors = {
        0:'blue',
        1:'orange', 
        2:'green', 
        3:'red', 
        4:'purple', 
        5:'brown', 
        6:'pink', 
        7:'gray', 
        8:'olive', 
        9:'cyan'
    }
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
    # plt.figure(figsize=(20,7))
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
    # plt.subplot(2, 1, 1)
    
    plt.switch_backend('AGG')
    plt.xticks(rotation='vertical')
    if(graph == 1):
        lb = []
        for i in x:
            if(i==100):
                continue
            temp = list(map(lambda r: r[i], M))
            temp = list(map(lambda z: float(z), temp))
            col.append(temp)
            lb.append(labels[i])
        print("sdghshdfjkds")
        for i in col:
            print(i)
        if(x[0]==100):
            for i in range(len(col)):
                plt.plot(col[i], ls='solid', label=lb[i] ,color=colors[i])
            plt.xlabel('X')
        else:
            for i in range(1,len(col)):
                print("YOYO")
                plt.plot(col[0], col[i], label=lb[i],ls='solid', color=colors[i])
            plt.xlabel(labels[x[0]])
        plt.ylabel('Y')
        plt.legend(loc=0)
    elif(graph == 2):
        lb = []
        for i in range(1,len(x)):
            if(x[i]==100):
                continue
            temp = list(map(lambda r: r[x[i]], M))
            temp = list(map(lambda z: float(z), temp))
            col.append(temp)
            lb.append(labels[x[i]])
        x_axis = list(map(lambda r: r[x[0]], M))
        xaxisls = [z for z in range(len(x_axis))]
        plt.xticks(xaxisls,x_axis)
        if(len(col)%2!=0):
            diff = 0.30*(int(len(col)/2))
            xaxisls = list(map(lambda x: x-diff,xaxisls))
            for i in range(len(col)):
                plt.bar(xaxisls, col[i], label=lb[i], color=colors[i], width=0.30)
                xaxisls = list(map(lambda x: x+0.30,xaxisls))
        else:
            diff = 0.30*(int(len(col)/2)) -0.15
            xaxisls = list(map(lambda x: x-diff,xaxisls))
            for i in range(len(col)):
                plt.bar(xaxisls, col[i], label=lb[i], color=colors[i], width=0.30)
                xaxisls = list(map(lambda x: x+0.30,xaxisls))
        plt.xlabel(labels[x[0]])
        plt.ylabel('Y')
        plt.legend(loc=0)
    elif(graph == 3):
        for i in range(1,len(x)):
            if(x[i]==100):
                continue
            temp = list(map(lambda r: r[x[i]], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
            plt.ylabel(labels[x[i]]) 
            break
        plt.hist(col[0], facecolor='blue')
        plt.xlabel('X')
    else:
        lb = None
        for i in range(1,len(x)):
            if(x[i]==100):
                continue
            temp = list(map(lambda r: r[x[i]], M))
            temp = list(map(lambda x: float(x), temp))
            col.append(temp)
            lb = labels[x[i]]
            break
            # temp = list(map(lambda r: r[i], M))
            # temp = list(map(lambda x: float(x), temp))
            # col.append(temp)
        x_axis = list(map(lambda r: r[x[0]], M))
        plt.pie(col[0], labels=x_axis, rotatelabels=True)
        plt.title(lb)
        plt.axis("off")
        # plt.legend(patches,x_axis,loc='best')

    imgname = doc.docfile.path+".png"
    print(imgname)
    # ax = plt.axes()
    # ax.axis('scaled')
    plt.savefig(imgname, bbox_inches='tight', dpi=100)
    # plt.close()
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
    