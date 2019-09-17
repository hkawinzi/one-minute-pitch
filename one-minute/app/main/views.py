from flask import render_template, request, redirect, url_for, abort
from sqlalchemy import func

from . import main
from ..models import User, Promotion, Pick, Production, Interview, CommentsPromotion, CommentsPick, CommentsProduction
from .forms import UpdateProfile, PromotionForm, PickForm, ProductionForm, InterviewForm, PromotionCommentForm, \
    PickCommentForm, ProductionCommentForm, InterviewCommentForm
from flask_login import login_required, current_user

from .. import db, photos
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home'

    return render_template('index.html', title=title)
@main.route('/user/<fname>')
def profile(fname):
    user = User.query.filter_by(firstname=fname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<fname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(fname):
    user = User.query.filter_by(firstname=fname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.pitch = form.pitch.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', fname=user.firstname))

    return render_template('profile/update.html', form=form)


@main.route('/user/<fname>/update/pic', methods=['POST'])
@login_required
def update_pic(fname):
    user = User.query.filter_by(firstname=fname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', fname=fname))


@main.route('/category/pickup-post', methods=['GET', 'POST'])
@login_required
def pick():
    form = PickForm()
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_pick = Pick(post=post, user=current_user, body=body)
        new_pick.save_pick()
        return redirect(url_for('.listpickup'))
    return render_template("pick_up_post.html", pick_form=form)


@main.route('/category/promotion-post', methods=['GET', 'POST'])
@login_required
def promotion():
    form = PromotionForm()
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_promotion = Promotion(post=post, user=current_user, body=body)
        new_promotion.save_promotion()
        return redirect(url_for('.listpromotion'))
    return render_template("promotion_post.html", promotion_form=form)


@main.route('/category/production-post', methods=['GET', 'POST'])
@login_required
def production():
    form = ProductionForm()
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_production = Production(post=post, user=current_user, body=body)
        new_production.save_production()
        return redirect(url_for('.listproduction'))
    return render_template("production_post.html", production_form=form)


@main.route('/category/interview-post', methods=['GET', 'POST'])
@login_required
def interview():
    form = InterviewForm()
    if form.validate_on_submit():
        post = form.post.data
        body = form.body.data
        new_interview = Interview(post=post, user=current_user, body=body)
        new_interview.save_production()
        return redirect(url_for('.listinterview'))
    return render_template("interview_post.html", interview_form=form)


@main.route('/category/promotion')
def listpromotion():
    posts = Promotion.query.all()
    return render_template("promotion.html", mypost=posts)


@main.route('/promotion/<int:id>', methods=['POST', 'GET'])
def displaypromotion(id):
    promotion = Promotion.query.get(id)
    form = PromotionCommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_promo_comment = CommentsPromotion(comment=comment, promotion_id=id, user=current_user)
        new_promo_comment.save_promo_coments()

    comments = CommentsPromotion.query.filter_by(promotion_id=id).all()
    return render_template('promopitch.html', promotion=promotion, comment_form=form, comments=comments)


@main.route('/category/pickup')
def listpickup():
    posts = Pick.query.all()
    return render_template("pick_up.html", mypost=posts)


@main.route('/pickup/<int:id>', methods=['GET', 'POST'])
def displaypickup(id):
    pick = Pick.query.get(id)
    form = PickCommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_pick_comment = CommentsPick(comment=comment, pick_id=id, user=current_user)
        new_pick_comment.save_pick_coments()

    comments = CommentsPick.query.filter_by(pick_id=id).all()
    return render_template('pickpitch.html', pick=pick, comment_form=form, comments=comments)


@main.route('/category/production')
def listproduction():
    posts = Production.query.all()
    return render_template("production.html", mypost=posts)


@main.route('/production/<int:id>', methods=['GET', 'POST'])
def displayproduction(id):
    production = Production.query.get(id)
    form = ProductionCommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_produ_comment = CommentsProduction(comment=comment, production_id=id, user=current_user)
        new_produ_comment.save_produ_coments()

    comments = CommentsProduction.query.filter_by(production_id=id).all()
    return render_template('produpitch.html', production=production, comment_form=form, comments=comments)


@main.route('/background_process')
def background_process():
    like = Like(user=current_user)
    like.save_like()
    total = db.session.query(func.sum(Like.like)).scalar()
    total = str(total)
    return total


@main.route('/background_processs')
def background_processs():
    unlike = Unlike(user=current_user)
    unlike.save_unlike()
    total = db.session.query(func.sum(Unlike.unlike)).scalar()
    total = str(total)
    return total


@main.route('/category/interview')
def listinterview():
    posts = Interview.query.all()
    return render_template("interview.html", mypost=posts)


@main.route('/interview/<int:id>', methods=['GET', 'POST'])
def displayinterview(id):
    interview = Interview.query.get(id)
    form = InterviewCommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_int_comment = CommentsInterview(comment=comment, interview_id=id, user=current_user)
        new_int_comment.save_int_coments()

    comments = CommentsInterview.query.filter_by(interview_id=id).all()
    return render_template('interpitch.html', interview=interview, comment_form=form, comments=comments)
