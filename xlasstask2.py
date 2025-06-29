print("zahra syed")
perceptions = ['dirt', 'clean', 'obstacle']
actions = ['sweep', 'move_forward', 'avoid']
results = []
def reflex_agent(cperception):
    if cperception == 'dirt':
        action = actions[0] 
    elif cperception == 'clean':
        action = actions[1]  
    elif cperception == 'obstacle':
        action = actions[2]  
    else:
        action = 'do_nothing'  
    return action
def run_agent(perceptions):
    for percept in perceptions:
        action = reflex_agent(percept)
        results.append(f"Perception: {percept}, Action: {action}")
    return results
input_perceptions = ['dirt', 'obstacle', 'clean', 'clean', 'dirt']
final_results = run_agent(input_perceptions)
for result in final_results:
    print(result)