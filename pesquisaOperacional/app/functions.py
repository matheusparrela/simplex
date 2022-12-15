def sendInformation(requestSession):
    constraints =  list()
    funcObj = list()
    for k, v in requestSession.items():
        if k == 'numVariable' or k == 'numConstraints' or k == 'IMethod' or k == 'objective' or k == "IMethodModule":
            continue

        if 'a' in str(k):
            constraints.append(v)
        else:
            funcObj.append(float(v))

    restrictions = treat_restrictions(constraints, int(requestSession["numVariable"]))

    requestJson = {
        "problem_type"      : requestSession["IMethod"],
        "method"            : requestSession["exibition_type"],
        "objective"         : requestSession["objective"],
        "objective_function": funcObj,
        "restrictions"      : restrictions,
    }

    if "integer_solution" in requestSession.keys():
        requestJson["integer_solution"] = True
    else:
        requestJson["integer_solution"] = False

    var_names = []
    for i in range(1, int(requestSession["numVariable"]) + 1):
        var_names.append(f"x{i}")

    requestJson["variable_names"] = var_names

    return requestJson




def treat_restrictions(constraints, numVariables):
    constraints_list = []

    current_restriction = []
    for i in range(0, len(constraints)):
        current_restriction.append(constraints[i])
        if len(current_restriction) == numVariables + 2:
            constraints_list.append({
                "coeficients": [float(val) for val in current_restriction[:-2]],
                "type": current_restriction[-2],
                "value": float(current_restriction[-1])
            })

            current_restriction = []

    for i in range(int(numVariables)):
        current_restriction = list(range(int(numVariables)))
        current_restriction = [x * 0 for x in current_restriction]
        current_restriction[i] = 1
        constraints_list.append({
            "coeficients": current_restriction,
            "type": ">=",
            "value": 0
        })

    return constraints_list