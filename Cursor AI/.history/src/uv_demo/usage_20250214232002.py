from uv_demo.calculator import Calculator

def main() -> None:
    # Create a calculator instance with 2 decimal places precision
    calc = Calculator(precision=2)
    
    # Basic operations
    print("Basic Operations:")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"Division: 15 / 2 = {calc.divide(15, 2)}")
    
    # Advanced operations
    print("\nAdvanced Operations:")
    print(f"Power: 2^3 = {calc.power(2, 3)}")
    print(f"Square root of 16 = {calc.square_root(16)}")
    print(f"25 as percentage = {calc.percentage(0.25)}%")
    
    # Memory operations
    print("\nMemory Operations:")
    calc.add(10, 5)
    print(f"Last result: {calc.get_last_result()}")
    calc.clear_memory()
    print(f"After clearing memory: {calc.get_last_result()}")

if __name__ == "__main__":
    main() 