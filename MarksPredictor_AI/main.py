import json
from engine.predictor import predict_needed_marks
from utils.helpers import print_report_card

# 1. Load Data
with open('data/subjects_config.json', 'r') as f:
    config = json.load(f)

def start_app():
    print("--- Welcome to World's Best Data Science Grade Predictor ---")
    
    target = float(input("Apna Target SGPA dalo (e.g. 8.5): "))
    
    mid_sem_input = {}
    for sub in config['subjects']:
        if config['subjects'][sub]['type'] != 'minor': # ICT/Env skip for midsem
            m = input(f"Enter Mid-Sem marks for {sub} (Out of 40): ")
            mid_sem_input[sub] = float(m)
            
    # 2. Predict
    result = predict_needed_marks(target, mid_sem_input, config['subjects'], config['defaults'])
    
    # 3. Output
    print_report_card(result)

if __name__ == "__main__":
    start_app()