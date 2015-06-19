# -*- coding: utf-8 -*-

"""

    Based on ARGO's density inversion test. Test 14 @ ARGO QC 2.9.1
"""

import numpy as np
from numpy import ma


def densitystep(S, T, P):
    """
    """
    assert S.shape == T.shape
    assert S.shape == P.shape
    try:
        import gsw
        rho0 = gsw.pot_rho_t_exact(S, T, P, 0)
        ds = ma.append(ma.masked_all(1),
                np.sign(np.diff(P))*np.diff(rho0))
        return ds

    except ImportError:
        print("Package gsw is required and is not available.")


def density_inversion(data, cfg, aux=False):
    """

        Must decide where to set the flags.
    """
    assert ('temperature' in data.keys()), \
            "Missing temperature"
    assert ('salinity' in data.keys()), \
            "Missing salinity"
    assert ('pressure' in data.keys()), \
            "Missing pressure"

    ds = densitystep(data['temperature'], data['salinity'],
            data['pressure'])

    return ds
    #flag = np.zeros(ds.shape, dtype='i1')
    #flag[ds >= cfg] = 1
    #flag[ds < cfg] = 4

    if aux:
        return flag, ds
    else:
        return flag
