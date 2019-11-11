#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test load qc configurations (utils.load_cfg)
"""

import os.path
import pkg_resources

from cotede.utils import load_cfg, cotede_dir


CFG = [f[:-5] for f in pkg_resources.resource_listdir('cotede', 'qc_cfg')
        if f[-5:] == '.json']


def test_no_local_duplicate_cfg():
    """ Avoid local cfg of default procedures

        Guarantee that there is no local copy of a default cfg json file,
          otherwise the default cfg could be breaking, and the tests safely
          escaping into a local, non-distributed, cfg.
    """

    for cfg in CFG:
        local_cfg = os.path.join(cotede_dir(), "cfg", "%s.json" % cfg)
        assert not os.path.exists(local_cfg), \
                "Redundant local cfg file: %s" % cfg


def test_inout():
    """ load_cfg shouldn't modify input variable cfg
    """
    cfg = 'cotede'
    out = load_cfg(cfg)
    assert out != cfg


def test_dict():
    """Test a user dict config

       It is possible to define a full config instead of choosing one of the
         builtins. This is done by giving a dictionary with the correct
         structure.
    """
    cfg = {'main': {'valid_datetime': None}}
    cfg_out = load_cfg(cfg)
    assert cfg_out == cfg


def test_default():
    cfg_out = load_cfg()
    assert isinstance(cfg_out, dict)
    assert len(cfg_out) > 0


def test_factory_cfgs():
    """Load all available configs, one at a time

       CoTeDe comes with builtin config. This test checks if can
         load all those available configs.
    """
    for cfg in CFG:
        print("Loading %s" % cfg)
        try:
            cfg_out = load_cfg(cfg)
        except:
            assert False, "Couldn't load: %s" % cfg
        assert isinstance(cfg_out, dict)
        assert len(cfg_out) > 0


# Missing a test to load cfg at ~/.cotede

def test_dict_input():
    """Test a dictionary input, i.e. manually defined config

       It should return the same dictionary
    """
    cfg = {'temperature': {'global_range': 'test'}}
    assert cfg == load_cfg(cfg)


def test_inheritance():
    """Test inheritance
    """
    cfg = load_cfg('cotede')
    cfg2 = load_cfg({'inherit': 'cotede'})
    for c in cfg:
        assert c in cfg
        assert cfg[c] == cfg2[c]

    # If is a list, the last is the lowest priority
    cfg2 = load_cfg({'inherit': ['cotede', 'gtspp']})
    for c in cfg:
        assert c in cfg
        if not isinstance(cfg[c], dict):
            assert cfg[c] == cfg2[c]
        else:
            for cc in cfg[c]:
                assert cfg[c][cc] == cfg2[c][cc]
