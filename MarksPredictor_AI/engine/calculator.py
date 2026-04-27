def get_grade_point(score, max_marks):
    percentage = (score / max_marks) * 100
    
    if percentage >= 90: return 10  # O Grade
    if percentage >= 80: return 9   # A+ Grade
    if percentage >= 70: return 8   # A Grade
    if percentage >= 60: return 7   # B+ Grade
    if percentage >= 50: return 6   # B Grade
    if percentage >= 40: return 5   # P Grade (Pass)
    return 0                         # F Grade (Fail)

def calculate_sgpa(results, subjects_config):
    total_credit_points = 0
    total_credits = 0
    
    for sub_name, marks in results.items():
        if sub_name in subjects_config:
            credit = subjects_config[sub_name]['credits']
            max_m = subjects_config[sub_name]['max_marks']
            
            gp = get_grade_point(marks, max_m)
            total_credit_points += (gp * credit)
            total_credits += credit
            
    if total_credits == 0: return 0
    return round(total_credit_points / total_credits, 2)