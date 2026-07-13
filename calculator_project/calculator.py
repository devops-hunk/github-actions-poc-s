#!/usr/bin/env python3
"""
Calculator module.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def divide(a, b):
    """Divide one number by another."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
