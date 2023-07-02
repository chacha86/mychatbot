from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.forms import ChatForm
from pybo.models import Chat
from pybo import db
from datetime import datetime

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route("list")
def _list():
    form = ChatForm()
    chat_list = Chat.query.order_by(Chat.create_date.asc()).all()
    print(chat_list)
    print(chat_list[0].body)
    return render_template("chat.html", chat_list=chat_list, form=form)

@bp.route("create", methods=('POST',))
def create():
    form = ChatForm()
    if form.validate_on_submit():
        body = form.body.data
        c1 = Chat(user_id=1, body=body, create_date=datetime.now())
        db.session.add(c1)
        db.session.commit()
    return redirect(url_for('chat._list'))
