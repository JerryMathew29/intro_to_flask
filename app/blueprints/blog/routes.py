from .import bp as blog
from flask import request,  url_for, redirect, flash, render_template
from app import db
from app.blueprints.blog.models import Post
from flask_login import current_user, login_required

@blog.route('/create-post', methods=['POST'])
def create_post():
    if request.method == 'POST':
        r = request.form
        data = {
            'post_body': r.get('post-body'),
            'author_id': current_user.id,
        }
        p = Post(body=data['post_body'], user_id=data['author_id'])
        db.session.add(p)
        db.session.commit()
        flash("The post was created successfully", 'success')
    return redirect(url_for('index'))
    
@blog.route('/blog')
@login_required
def get_post():
    _id = request.args.get('id')
    p = Post.query.get(_id)
    return render_template('post-single.html', post=p)