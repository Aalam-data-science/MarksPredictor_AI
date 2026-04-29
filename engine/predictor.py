def predict_needed_marks(target_sgpa, mid_sem_data, subjects_config, defaults):
    # Total credits calculate karna
    total_credits = sum(s['credits'] for s in subjects_config.values() if s['credits'] > 0)
    
    # Total credits calculate karna
    total_credits = sum(s['credits'] for s in subjects_config.values() if s['credits'] > 0)
    
    predictions = {}
    
    # Parul University SGPA to Percentage approx formula: (SGPA - 0.5) * 10
    target_percentage = (target_sgpa - 0.5) * 10
    
    for sub, info in subjects_config.items():
        mid_sem = mid_sem_data.get(sub, 25.0) # Default 25 if not provided
        
        # --- AAPKA CUSTOM ML LOGIC ---
        # 35+ Mid-sem -> 45+ Internal/Practical
        if mid_sem >= 35:
            est_internal_prac = 46.0
        # 30+ Mid-sem -> 40+ Internal/Practical
        elif mid_sem >= 30:
            est_internal_prac = 41.0
        # Minimum 35 se niche nahi jayega (even for 16 mid-sem)
        else:
            est_internal_prac = 35.0
            
        # 1. 150 Marks wale subjects (End Sem = 60)
        if info['max_marks'] == 150:
            # Formula: Total Needed = (Target% * 150 / 100)
            total_needed = (target_percentage * 150) / 100
            current_have = mid_sem + est_internal_prac
            needed_in_endsem = total_needed - current_have
            
            # Capping: 60 se upar nahi jana chahiye
            final_target = min(60, max(24, round(needed_in_endsem, 2))) # 24 is passing (40%)
            predictions[sub] = f"{final_target} / 60"

        # 2. 100 Marks wale subjects (Maths/PSOSM - End Sem = 60 or 40)
        elif info['max_marks'] == 100:
            total_needed = (target_percentage * 100) / 100
            # 100 marks mein practical nahi hota, only Internal (40) + EndSem (60)
            # Mid-sem is part of internal
            current_internal = (mid_sem/40)*20 + 15 # Approx internal logic
            needed_in_endsem = total_needed - current_internal
            
            final_target = min(60, max(24, round(needed_in_endsem, 2)))
            predictions[sub] = f"{final_target} / 60"

        # 3. 50 Marks wale subjects (ICT)
        elif info['max_marks'] == 50:
            total_needed = (target_percentage * 50) / 100
            # Mostly Practical based
            predictions[sub] = f"{max(20, round(total_needed, 2))} / 50 (Total)"

    return predictions