#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Check morello2014 test
"""

import numpy as np

from cotede.utils import download_testdata
from cotede.qc import fProfileQC

def test():
    """
    """
    datafile = download_testdata("dPIRX010.cnv")
    pqc = fProfileQC(datafile, cfg='morello2014')
    assert sorted(np.unique(pqc.flags['TEMP']['morello2014'])) == [1, 2, 3, 4]
    assert sorted(np.unique(pqc.flags['TEMP2']['morello2014'])) == [1]
    assert sorted(np.unique(pqc.flags['PSAL']['morello2014'])) == [1, 2, 4]
    assert sorted(np.unique(pqc.flags['PSAL2']['morello2014'])) == [1]
