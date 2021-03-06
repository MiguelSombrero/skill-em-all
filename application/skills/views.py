from application import app, db, login_manager
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

@app.route("/skills", methods=["GET"])
@login_required
def skills_my():
    skills = Skill.query.filter_by(owner_id=current_user.id)

    return render_template("skills/skills.html",
        form = SkillForm(),
        skills = skills
    )

@app.route("/skills", methods=["POST"])
@login_required
def skills_create():
    form = SkillForm(request.form)

    if not form.validate():
        return render_template("skills/skills_form.html", form = form)

    if not __validate_experience(form):
        return render_template("skills/skills_form.html", form = form,
            error = "You must give an experience to skill")

    skill = Skill.query.filter_by(name=form.name.data, owner_id=current_user.id).first()
        
    if skill:
        return render_template("skills/skills_form.html", form = form,
            error = "You already have skill " + form.name.data)
         
    skill = Skill(form.name.data)
    skill.owner_id = current_user.id
    db.session.add(skill)
    db.session.commit()
    
    work_experience = Experience("Work experience",
        form.work_experience_years.data * 12 + form.work_experience_months.data
    )

    work_experience.skill_id = skill.id
    db.session.add(work_experience)
    
    other_experience = Experience("Other experience",
        form.other_experience_years.data * 12 + form.other_experience_months.data
    )

    other_experience.skill_id = skill.id
    db.session.add(other_experience)
    
    db.session.commit()   

    return redirect(url_for("skills_form"))

@app.route("/skills/<skill_id>/update", methods=["POST"])
@login_required
def skills_update(skill_id):
    skill = Skill.query.get(skill_id)

    if not skill.is_owned_by(current_user.id):
        return login_manager.unauthorized()
    
    form = SkillForm(request.form)

    if not form.validate():
        return render_template("skills/skills.html",
            form = form,
            skills = Skill.query.filter_by(owner_id=current_user.id)
        )

    if not __validate_experience(form):
        return render_template("skills/skills.html",
            form = form,
            skills = Skill.query.filter_by(owner_id=current_user.id),
            error = "You must give an experience to skill"
        )

    work_experience = Experience.query\
        .filter_by(skill_id=skill_id, experience_type="Work experience")\
        .first()
    
    other_experience = Experience.query\
        .filter_by(skill_id=skill_id, experience_type="Other experience")\
        .first()
        
    work_experience.experience = form.work_experience_years.data * 12 + form.work_experience_months.data
    other_experience.experience = form.other_experience_years.data * 12 + form.other_experience_months.data
    
    db.session.commit()     

    return redirect(url_for("skills_my"))

@app.route("/skills/<skill_id>/delete", methods=["POST"])
@login_required
def skills_delete(skill_id):
    skill = Skill.query.get(skill_id)

    if not skill.is_owned_by(current_user.id):
        return login_manager.unauthorized()
    
    db.session.delete(skill)
    db.session.commit()

    return redirect(url_for("skills_my"))

def __validate_experience(form):
    if form.work_experience_years.data == 0 and \
        form.work_experience_months.data == 0 and \
        form.other_experience_years.data == 0 and \
        form.other_experience_months.data == 0:
        return False
    
    return True
