def validate_marks(marks, max_limit):
    """Check karta hai ki marks range mein hain ya nahi"""
    try:
        val = float(marks)
        if 0 <= val <= max_limit:
            return val
        return None
    except ValueError:
        return None

def print_report_card(predictions):
    """Result ko sundar aur accurate tarike se dikhane ke liye"""
    print("\n" + "="*45)
    print(f"{'SUBJECT':<25} | {'REQUIRED MARKS'}")
    print("="*45)
    
    for sub, result_string in predictions.items():
        # result_string mein pehle se hi '/ 60' ya '/ 30' juda hua hai
        print(f"{sub:<25} | {result_string}")
        
    print("="*45)
    print("TIP: Ye marks minimum hain target CGPA pane ke liye.")