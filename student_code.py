def ask(var, value, evidence, bn):
	
#var is the name of the hyptothesis variable.
#value indicates whether the hypothesis being asked about is True or False.
#evidence is the set of variables known to be True or False.
#bn is the BayesNet (in the provided module) pertaining to the problem.

#To calculate P(H|E), ask should calculate and return, where:

     #P(H,E) is the joint probability of the hypothesis (var = value) 
     # and the evidence (evidence), and

     #alpha is the Normalization Constant (the joint probability of 
     # the hypothesis and the evidence plus the joint probability 
     # of $\neg$hypothesis and the evidence).


	#We need to map each hypothesis variable with it respective value
	# using a dictionary 
	
	variable_value_dict = dict(evidence)
	variable_value_dict[var] = value

	opposite_variable_value_dict = dict(evidence)
	opposite_variable_value_dict[var] = not value

	#We can then create a helper function that helps us calculate joint_probability
	x = helper(list(bn.variables),variable_value_dict, bn)

	y = helper(list(bn.variables),opposite_variable_value_dict, bn)

	prob = x/(x+y)

	return prob


def helper(variables, values, bn):
	# To implement this recursion you may want to 
	# introduce a new function. That function takes the 
	# list of variables in the joint probability and 
	# the collection of all known variable values.

	#base case
	if len(variables) == 0:
		return 1

	
	variable = variables.pop(0)

	if variable.name in list(values):

		# Probability calculates the associated joint probability
		# Parameters:
		# hypothesis (Boolean): is the hypothesis True or False?
		# evidence (Array): facts about the world state
		# Returns: Float

		Joint_Probability = variable.probability(values[variable.name], values)
		recursion = Joint_Probability * helper(variables, values, bn)
		return recursion 

	else:
		True_values = dict(values)
		True_values[variable.name] = True

		False_values = dict(values)
		False_values[variable.name] = False
		
		True_variable = list(variables)
		False_variable = list(variables)
		# If the value of the next variable is not known, we need to 
		# compute the sum of the joint probabilities when the unknown 
		# is True or False.
		sum_joint_probabilities = (variable.probability(True, values)*helper(True_variable, True_values, bn)) + \
								(variable.probability(False, values)*helper(False_variable, False_values, bn))

		return sum_joint_probabilities
