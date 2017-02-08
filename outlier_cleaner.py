#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import heapq
    cleaned_data = []
    residual = abs(net_worths - predictions)
    residual_large = heapq.nlargest(9, residual)
    for i, res in enumerate(residual):
        if res not in residual_large:
            cleaned_data.append((ages[i], net_worths[i], residual[i]))


    ### your code goes here

    
    return cleaned_data

