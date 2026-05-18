"""Validate every streamtex-design design system."""

from __future__ import annotations

import importlib
import pkgutil

import pytest
from streamtex.core import validation

import streamtex_design.design_systems as ds_pkg


def _iter_design_systems():
    for module_info in pkgutil.iter_modules(ds_pkg.__path__):
        if module_info.ispkg:
            yield importlib.import_module(f"streamtex_design.design_systems.{module_info.name}")


DS_MODULES = list(_iter_design_systems())


@pytest.mark.parametrize("mod", DS_MODULES, ids=lambda m: m.__name__)
def test_design_system_validates(mod):
    issues = validation.validate_design_system(mod)
    errors = [i for i in issues if i.is_error()]
    assert errors == [], f"{mod.__name__} errors: {errors}"


def test_three_design_systems():
    names = {m.DesignSystem.name for m in DS_MODULES}
    assert names == {"default", "modern_dark", "modern_light"}, f"Got {names}"
