from application import app, db
from flask import render_template, request, redirect, url_for
from application.skills.models import Skill
from application.accounts.models import Account
from application.models import account_skill
from application.skills.forms import SkillForm
from flask_login import login_required, current_user

@app.route("/skills")
def skills_form():
    return render_template("skills/skills_form.html",
        form = SkillForm()
    )

@app.route("/skills", methods=["POST"])
@login_required
def skills_create():
    form = SkillForm(request.form)

    if not form.validate():
        return render_template("skills/skills_form.html", form = form)

    skill = Skill.query.filter_by(name=form.name.data).first()

    if not skill:
        account = Account.query.get(current_user.id)
        skill = Skill(form.name.data, account)

        db.session.add(skill)
        db.session.commit()

    return redirect(url_for("skills_form"))
