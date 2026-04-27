def predict_needed_marks(target_sgpa, mid_sem_data, subjects_config, defaults):
    # Total credits calculate karna
    total_credits = sum(s['credits'] for s in subjects_config.values() if s['credits'] > 0)
    
    predictions = {}
    
    for sub, info in subjects_config.items():
        # Current internal marks (Avg 16.5)
        current_marks = defaults['internal_avg']
        
        # 1. 150 Marks wale subjects (AIML, OOPS, Physics, Adv. Comm)
        if info['max_marks'] == 150:
            mid_sem = mid_sem_data.get(sub, 0)
            prac = defaults['practical_avg'] # 24 average
            current_total = current_marks + mid_sem + prac
            # End sem 60 mein se kitne chahiye (Targeting 80% for safe side)
            needed = (info['max_marks'] * 0.8) - current_total
            predictions[sub] = f"{max(0, round(needed, 2))} / 60"

        # 2. 100 Marks wale subjects (Linear Algebra, PSOSM)
        elif info['max_marks'] == 100:
            mid_sem = mid_sem_data.get(sub, 0)
            current_total = current_marks + mid_sem # No practical here
            needed = (info['max_marks'] * 0.8) - current_total
            predictions[sub] = f"{max(0, round(needed, 2))} / 40" # End sem is often 40 or 60 check booklet

        # 3. 50 Marks wale subjects (ICT, EVS) - Fix is here!
        elif info['max_marks'] == 50:
            # ICT/EVS mein mid-sem nahi hota, mostly practical/viva hota hai (30 marks)
            # Internal (20) + Practical/Viva (30) = 50
            needed_in_viva = (50 * 0.8) - current_marks # 40 marks target - 16.5 internal
            predictions[sub] = f"{max(0, round(needed_in_viva, 2))} / 30 (Viva/Prac)"

    return predictions