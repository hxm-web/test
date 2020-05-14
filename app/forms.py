from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length



class CommentForm(FlaskForm):
    content = StringField('内容：', validators=[DataRequired(), Length(min=0, max=200)])
    submit = SubmitField('提交')


