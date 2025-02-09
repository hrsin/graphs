import math

def resistor_calc():
    print("Starting resistor calculator...\n")
    resistor_values = [10, 27, 49.9]
    result = None
    v_adj = 1.21
    i_adj = 0.000001
    v_out = 3.3
    min_diff = float('inf')
    res_calc = {}
    for i, r1 in enumerate(resistor_values):
        # calculating the desired R2 value
        r1*=1000
        desired_r2 = (v_out-v_adj)/(i_adj+(v_adj/(r1)))
        # Binary Search variables
        left, right = 0, len(resistor_values)-1
        while left<=right:
            mid = (left+right)//2
            r2 = resistor_values[mid]*1000
            calc_v_out = v_adj*(1+(r2/r1))+i_adj*r2
            diff = abs(calc_v_out-v_out)
            if diff<min_diff:
                min_diff = diff
                res_calc[calc_v_out] = (r1, r2)
            if calc_v_out<v_out:
                left = mid+1
            else:
                right = mid-1    
    i = 30
    for k in sorted(res_calc.keys()):
        print(f"Vout = {k:.2f},  R1 = {res_calc[k][0]}, R2 = {res_calc[k][1]}")
        
resistor_calc()