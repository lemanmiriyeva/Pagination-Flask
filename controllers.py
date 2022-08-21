from flask import render_template,request, url_for
from app import app
from model import *

rows_per_page=5

@app.route('/')
def blogs():
    page=request.args.get('page',1,type=int)
    blogs = Blogs.query.paginate(page=page,per_page=rows_per_page)
    total=db.session.query(Blogs).count()
    return render_template('home.html', blogs = blogs,total=total, show=False)