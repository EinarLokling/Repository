def tempConversion(temp, scale):
    """
    Converts temperatures between Fahrenheit and Celsius and 
    return the converted temperature.

    Parameters
    ----------
    temp : float
        A temperature to be converted.
    scale : str
        Indicates the scale of the temperature ("F" or "C").

    Returns
    -------
    converted_temp : float
        The converted temperature.

    """
    if scale == "F":
        converted_temp = (5/9)*(temp - 32)
    else:
        converted_temp = (9/5) * temp + 32
        
    return converted_temp

converted_temp = tempConversion(temp, scale)

