from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Note

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    if not notes:
        flash('You have no notes first add!', category='error')
        return redirect(url_for('views.add'))
    return render_template('home.html', notes=notes, user=current_user)


@views.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        discription = request.form.get('discription')
        detail = request.form.get('detail')

        if len(title) < 1:
            flash('Title is too short', category='error')
        else:
            new_note = Note(title=title, discription=discription,
                            detail=detail, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('views.home'))

    return render_template('add_note.html', user=current_user)


@views.route('/delete/<int:id>', methods=['GET'])
@login_required
def delete_note(id):
    note = Note.query.filter_by(id=id).first()
    if not note:
        flash('Note does not exist', category='error')
    else:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted!', category='success')
    return redirect(url_for('views.home'))
