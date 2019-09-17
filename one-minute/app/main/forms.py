class UpdateProfile(FlaskForm):
    pitch = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
class PromotionForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class PickForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class ProductionForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class InterviewForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')