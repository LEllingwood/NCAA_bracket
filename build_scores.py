
# This function calculates the total score for each team--given score * weight 


def calc_overal_score():
    location_score = ''
    mascot_score = ''
    color_score = ''

    mascot_weight = 3
    location_weight = 1
    color_weight = 2.25
    
    school_score = float(location_score * location_weight) + float(color_score * color_weight) + float(mascot_score * mascot_weight)
    return school_score
