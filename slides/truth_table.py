import pandas as pd

combinations = [
    (P, L, F, X)
    for P in [False, True]
    for L in [False, True]
    for F in [False, True]
    for X in [False, True]
]

and_results = [
    {
        "isDev": not P and (F or L or X),
        'apiEnv.includes("prod")': P,
        "localhostMatch": L,
        "featureMatch": F,
        "xyzMatch": X,
    }
    for P, L, F, X in combinations
]

and_truth_table = pd.DataFrame(and_results)

or_results = [
    {
        "isDev": not P or (F or L or X),
        'apiEnv.includes("prod")': P,
        "localhostMatch": L,
        "featureMatch": F,
        "xyzMatch": X,
    }
    for P, L, F, X in combinations
]

or_truth_table = pd.DataFrame(or_results)
