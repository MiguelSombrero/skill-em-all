from application import app, db
from flask import render_template, request, redirect, url_for
from application.skills.models import Skill
from application.skills.models import Experience
from application.accounts.models import Account
from application.skills.forms import SkillForm
from flask_login import login_required, current_user

@app.route("/skills/new")
@login_required
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

    skill = Skill.query.filter_by(name=form.name.data, owner_id=current_user.id).first()
        
    if not skill:
        skill = Skill(form.name.data)
        skill.owner_id = current_user.id
        db.session.add(skill)
        db.session.commit()

        if form.work_experience_years.data > 0 or form.work_experience_months.data:
            work_experience = Experience("Work experience",
                form.work_experience_years.data * 12 + form.work_experience_months.data
            )

            work_experience.skill_id = skill.id
            db.session.add(work_experience)
            db.session.commit()

        if form.other_experience_years.data > 0 or form.other_experience_months.data:
            other_experience = Experience("Other experience",
                form.other_experience_years.data * 12 + form.other_experience_months.data
            )

            other_experience.skill_id = skill.id
            db.session.add(other_experience)
            db.session.commit()

    return redirect(url_for("skills_form"))
