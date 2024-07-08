def conditional_probability(event_a, event_b):
    if len(event_a) != len(event_b):
        raise ValueError("The lengths of event_a and event_b must be the same.")
    
    count_a = sum(event_a)
    count_a_and_b = sum(a and b for a, b in zip(event_a, event_b))
    
    if count_a == 0:
        return 0 
    
    return count_a_and_b / count_a
def take_input():
    event_a = list(map(int, input("Enter the list for event A (space-separated): ").split()))
    event_b = list(map(int, input("Enter the list for event B (space-separated): ").split()))
    
    return event_a, event_b
event_a, event_b = take_input()
print(conditional_probability(event_a, event_b))
