import pytest
from fee_calculator import calculate_pix_fee
import time  # Importing the time module to add a delay

# Existing test for calculating fee for transactions up to R$1000
def test_fee_up_to_1000():
    result = calculate_pix_fee(500)
    print(f"Transação: R$500, Taxa cobrada: R${result}. Para valores até R$1000, a taxa é de 1%.")
    assert result == 5.0  # 1% of 500 is 5.0
    time.sleep(15)  # Adds a 15-second delay before the terminal clears

# Existing test for calculating fee for transactions between R$1001 and R$5000
def test_fee_1001_to_5000():
    result = calculate_pix_fee(3000)
    print(f"Transação: R$3000, Taxa cobrada: R${result}. Para valores entre R$1001 e R$5000, a taxa é de 0.5%.")
    assert result == 15.0  # 0.5% of 3000 is 15.0
    time.sleep(15)  # Adds a 15-second delay before the terminal clears

# Existing test for calculating fee for transactions above R$5000
def test_fee_above_5000():
    result = calculate_pix_fee(6000)
    print(f"Transação: R$6000, Taxa cobrada: R${result}. Para valores acima de R$5000, a taxa é fixa em R$10.")
    assert result == 10.0  # Flat fee of R$10 for amounts above R$5000
    time.sleep(15)  # Adds a 15-second delay before the terminal clears

# Add more tests if needed...

if __name__ == '__main__':
    pytest.main()
