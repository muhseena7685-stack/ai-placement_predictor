def generate_recommendations(student):
    recs = []
    if student["cgpa"] < 7.0:
        recs.append("Improve CGPA by focusing on core subjects.")
    if student["technical_score"] < 70:
        recs.append("Take a coding or technical skill course (Python, DSA).")
    if student["communication_score"] < 70:
        recs.append("Join communication workshops or mock interviews.")
    if student["aptitude_score"] < 60:
        recs.append("Practice aptitude questions on Quant & Reasoning.")
    if student["internships_count"] == 0:
        recs.append("Apply for at least one internship for industry exposure.")
    if len(recs) == 0:
        recs.append("Great profile! Focus on placement drives and interviews.")
    return recs