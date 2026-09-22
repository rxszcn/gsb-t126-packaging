"""同一个对象在被读过之后，成员数量与顺序会不会自己变

跑法：PYTHONPATH=src .venv/bin/python repro/specset-view.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pickle

from packaging.specifiers import Specifier, SpecifierSet

ss = SpecifierSet([Specifier(">=1.0"), Specifier(">=1.0"), Specifier("!=2.0")])
print("fresh      : len =", len(ss), " list =", [str(s) for s in ss])
print("str(ss)    =", str(ss))
print("after str(): len =", len(ss), " list =", [str(s) for s in ss])
clean = SpecifierSet("!=2.0,>=1.0")
same = SpecifierSet([Specifier(">=1.0"), Specifier("!=2.0")])
print("pickle 与规范构造一致吗:", pickle.dumps(same) == pickle.dumps(clean))
comb = SpecifierSet(">=1.0") & SpecifierSet("<2.0,!=2.0")
print("__and__ 结果: len", len(comb), " str", str(comb), " list", [str(s) for s in comb])
