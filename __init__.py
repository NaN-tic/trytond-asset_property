# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import asset

def register():
    Pool.register(
        asset.Asset,
        module='asset_property', type_='model')
