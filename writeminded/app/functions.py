def handleUploadedFile(f):
    with open('app/static/uploads/' + f.name, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk) 