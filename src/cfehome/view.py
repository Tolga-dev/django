from django.http import HttpResponse
from django.shortcuts import render 
import pathlib

curr_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(req, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title" : my_title
    } 
    html_template = "home.html"
    return render(req, html_template, my_context)

def home_old_page_view(req, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!doctype html>
<html lang="en">
<body>
    <h1> {my_title}</h1>
</body>
</html>
    """.format(**my_context)

    # html_file_path = curr_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)