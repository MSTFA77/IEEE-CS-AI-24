def bayes_theorem(prior_a, prior_b, conditional_b_given_a):
    posterior_a_given_b = (conditional_b_given_a * prior_a) / prior_b
    return posterior_a_given_b
def take_input():
    prior_a = float(input("Enter the prior probability of event A: "))
    prior_b = float(input("Enter the prior probability of event B: "))
    conditional_b_given_a = float(input("Enter the conditional probability of B given A: "))
    
    return prior_a, prior_b, conditional_b_given_a
prior_a, prior_b, conditional_b_given_a = take_input()
result = bayes_theorem(prior_a, prior_b, conditional_b_given_a)
print(f"The posterior probability of A given B is: {result}")
