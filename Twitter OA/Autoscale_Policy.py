import math

# https://stackoverflow.com/questions/65593064/setup-a-autoscale-policy-assessment
#  easy

def inalInstances(instances, avg):
    i = 0
    while i < len(avg):
        if avg[i] < 25 and instances > 1:
            instances = math.ceil(instances / 2)
            i += 10
            if i > len(avg):
                break

        if avg[i] > 60 and instances <= 10 ** 8:
            instances *= 2
            i += 10
            if i > len(avg):
                break
        i += 1

        return(instances)