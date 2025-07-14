import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from .models import db, Applicant

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/apply', methods=['POST'])
def apply():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
        message = request.form['message']
        resume = request.files['resume']

        if not all([name, email, phone, position, message, resume]):
            return jsonify({'error': 'Missing fields'}), 400

        filename = secure_filename(resume.filename)
        resume_path = os.path.join(os.getcwd(), 'uploads', filename)
        resume.save(resume_path)

        applicant = Applicant(
            name=name,
            email=email,
            phone=phone,
            position=position,
            message=message,
            resume_filename=filename
        )

        db.session.add(applicant)
        db.session.commit()

        return jsonify({'message': 'Application submitted successfully'}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong'}), 500
