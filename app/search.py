from flask import Blueprint, request, jsonify
from models import db, Patient

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET'])
def search_patients():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = Patient.query.filter(
        (Patient.first_name.ilike(f"%{query}%")) |
        (Patient.last_name.ilike(f"%{query}%")) |
        (Patient.medical_record_number.ilike(f"%{query}%")) |
        (Patient.diagnosis.ilike(f"%{query}%"))
    ).all()

    response = [
        {
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "dob": patient.dob,
            "medical_record_number": patient.medical_record_number,
            "diagnosis": patient.diagnosis,
            "last_visit": patient.last_visit
        }
        for patient in results
    ]

    return jsonify(response)