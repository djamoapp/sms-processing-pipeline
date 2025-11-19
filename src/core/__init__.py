"""
Package core - Composants fondamentaux du système
"""

from .parsers import normalize_date, parse_currency_amount, extract_numeric_value
from .currency_converter import CurrencyConverter, currency_converter, convert_currency, normalize_currency, get_currency_symbol
from .text_normalizer import normalize_sms
from .validators import is_valid_phone_number, is_valid_counterparty_name, is_plausible_reference
from .extractors_base import BaseExtractor, RegexExtractor

__all__ = [
    # Parsers
    'normalize_date',
    'parse_currency_amount', 
    'extract_numeric_value',
    
    # Currency
    'CurrencyConverter',
    'currency_converter',
    'convert_currency', 
    'normalize_currency',
    'get_currency_symbol',
    
    # Text processing
    'normalize_sms',
    
    # Validators
    'is_valid_phone_number',
    'is_valid_counterparty_name', 
    'is_plausible_reference',
    
    # Base classes
    'BaseExtractor',
    'RegexExtractor'
]