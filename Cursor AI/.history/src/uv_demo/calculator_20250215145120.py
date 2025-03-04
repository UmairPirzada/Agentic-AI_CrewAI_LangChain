from typing import Union, Optional
from decimal import Decimal

class Calculator:
    """A calculator class with basic and advanced mathematical operations."""
    
    def __init__(self, precision: int = 2):
        """Initialize calculator with specified decimal precision."""
        self.precision = precision
        self._last_result: Optional[float] = None
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers."""
        self._last_result = round(float(a + b), self.precision)
        return self._last_result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a."""
        self._last_result = round(float(a - b), self.precision)
        return self._last_result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers."""
        self._last_result = round(float(a * b), self.precision)
        return self._last_result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        self._last_result = round(float(a / b), self.precision)
        return self._last_result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Raise base to the power of exponent."""
        self._last_result = round(float(base ** exponent), self.precision)
        return self._last_result
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        self._last_result = round(float(number ** 0.5), self.precision)
        return self._last_result
    
    def percentage(self, number: Union[int, float]) -> float:
        """Convert number to percentage (multiply by 100)."""
        self._last_result = round(float(number * 100), self.precision)
        return self._last_result
    
    def get_last_result(self) -> Optional[float]:
        """Return the last calculated result."""
        return self._last_result
    
    def clear_memory(self) -> None:
        """Clear the last stored result."""
        self._last_result = None 