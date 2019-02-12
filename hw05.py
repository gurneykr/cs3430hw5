#!/usr/bin/python

#!/usr/bin/python

###########################################
# module: hw05.py
# YOUR NAME
# YOUR A#
###########################################

# place the imports necessary for your solution here



###################### Problem 1 ########################

def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)
    # your code here
    pass

def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)
    # your code here
    pass

############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)
    # your code here
    pass

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)
    # your code here
    pass

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    # your code here
    pass

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    # your code here
    pass

def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)
    # your code here
    pass

def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or \
           price_direction.get_val() == -1
    # your code here
    pass



    
