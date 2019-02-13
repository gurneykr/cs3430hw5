#!/usr/bin/python

#!/usr/bin/python

###########################################
# module: hw05.py
# Krista Gurney
# A01671888
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import logdiff
from deriv import deriv
from deriv import ln_deriv

import unittest
import math



###################### Problem 1 ########################

def solve_pdeq(k1, k2):
    #k1*y' = k2*y
    assert isinstance(k1, const)
    assert isinstance(k2, const)
    return make_prod(make_const(1.0), make_e_expr(make_prod(make_quot(k2, k1),make_pwr('t', 1.0))))


def solve_pdeq_with_init_cond(y0, k):
    # solve y'=3y y(0) =1
    assert isinstance(y0, const)
    assert isinstance(k, const)
    return make_prod(y0, make_e_expr(make_prod(k, make_pwr('t', 1.0))))

############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)
    k = math.log(n.get_val()/p0.get_val()) / t.get_val()
    return make_prod(p0, make_e_expr(make_prod(const(k), make_pwr('t', 1.0))))

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)
    return make_prod(p0 , make_e_expr(make_prod(make_prod(const(-1.0), lmbda), t )))

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    return math.ceil(math.log(c14_percent.get_val())/ -0.00012)

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    return tof(demand_eq)(price.get_val())

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



    
