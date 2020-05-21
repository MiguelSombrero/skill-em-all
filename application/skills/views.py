from application import app, db
from flask import render_template, request, redirect, url_for
from application.skills.models import Skill
from application.skills.models import Experience
from application.accounts.models import Account
from application.models import account_skill
from application.skills.forms import SkillForm
from flask_login import login_required, current_user

@app.route("/skills/new")
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
    account = Account.query.get(current_user.id)
        
    if not skill:
        skill = Skill(form.name.data)
        db.session.add(skill)
        db.session.commit()

    Account.save_skill_for_user(current_user.id, skill.id)

    if form.work_experience.data > 0:
        work_experience = Experience("work_experience", form.work_experience.data)
        work_experience.account_id = current_user.id
        work_experience.skill_id = skill.id

        db.session.add(work_experience)
        db.session.commit()

    if form.other_experience.data > 0:
        other_experience = Experience("other_experience", form.other_experience.data)
        other_experience.account_id = current_user.id
        other_experience.skill_id = skill.id

        db.session.add(other_experience)
        db.session.commit()

    return redirect(url_for("skills_form"))
