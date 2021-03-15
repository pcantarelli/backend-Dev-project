def list_info(exercise_list):
    group_set = set()
    total_time_estimation = 0
    exercise_time_estimation = 0
    rep_time_estimation = 3
    reps = 0 
    series = 0
    time_interval = 0
    numExcercises = len(exercise_list)

    for exercise in exercise_list:
        for k, v in exercise.items():
            if k == 'group_name':
                group_set.add(v)
            elif k == 'reps':
                reps = int(v)
            elif k == 'series':
                series = int(v)
            elif k == 'time_interval':
                time_interval = int(v)
        exercise_time_estimation = (((reps * rep_time_estimation) + time_interval) * series)
        total_time_estimation += exercise_time_estimation
        exercise_time_estimation = 0

    num_excercises = len(exercise_list)
    num_group = len(group_set)

    total_program_string = ""
    if (total_time_estimation % 60) > 30:
        total_program_string = f" {(total_time_estimation // 60)+1} minutes"
    else:
        total_program_string = f" {(total_time_estimation // 60)} minutes"

    return {
        'num_excercises': num_excercises, 
        'num_group': num_group, 
        'total_program_string': total_program_string, 
    }


def get_groups_list(exercise_list):
    group_set = set()

    for exercise in exercise_list:
        for k, v in exercise.items():
            if k == 'group_name':
                group_set.add(v)

    group_set = list(group_set)

    return group_set