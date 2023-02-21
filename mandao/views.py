from django.shortcuts import render

# show_html
def test(request):
    return render(request,"cms/picture_create.html")