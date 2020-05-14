from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.forms import CommentForm
from app.models import Comments

@app.route('/')
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/comfunction',methods=['GET','POST'])
def comfunction():
	comment = Comments.query.filter().all()
	form = CommentForm()
	if form.validate_on_submit():
		com = Comments(content=form.content.data)
		db.session.add(com)
		db.session.commit()
		flash('Congratulations, you have issued!')
		return redirect(url_for('index'))
	return render_template('commentArea.html', form=form,comment=comment)

@app.route('/cityCondition',methods=['GET','POST'])
def cityCondition():
    return render_template('cityCondition.html')



@app.route('/foods',methods=['GET','POST'])
def foods():
    return render_template('foods.html')

@app.route('/haoChengGaiXia',methods=['GET','POST'])
def haoChengGaiXia():
    return render_template('haoChengGaiXia.html')

@app.route('/huShangShengMingYue',methods=['GET','POST'])
def huShangShengMingYue():
    return render_template('huShangShengMingYue.html')

@app.route('/longZiHu',methods=['GET','POST'])
def longZiHu():
    return render_template('longZiHu.html')

@app.route('/path1',methods=['GET','POST'])
def path1():
    return render_template('path1.html')

@app.route('/path2',methods=['GET','POST'])
def path2():
    return render_template('path2.html')

@app.route('/path3',methods=['GET','POST'])
def path3():
    return render_template('path3.html')

@app.route('/path4',methods=['GET','POST'])
def path4():
    return render_template('path4.html')

@app.route('/paths',methods=['GET','POST'])
def paths():
    return render_template('paths.html')

@app.route('/scenicSpot',methods=['GET','POST'])
def scenicSpot():
    return render_template('scenicSpot.html')

@app.route('/yuWangGong',methods=['GET','POST'])
def yuWangGong():
    return render_template('yuWangGong.html')

@app.route('/zhangGongShan',methods=['GET','POST'])
def zhangGongShan():
    return render_template('zhangGongShan.html')


