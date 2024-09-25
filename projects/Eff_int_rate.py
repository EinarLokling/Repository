def eff_int_rate(r, n):
    
    r = 0.09
    n = 12
    
    eff_rate = (1+(r/n))**n - 1
    
    print(f"The effective interest rate is {100*eff_rate:.2f}%.")


