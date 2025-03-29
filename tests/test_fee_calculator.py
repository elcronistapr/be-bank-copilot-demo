import logging
from fee_calculator import calculate_pix_fee
import pytest

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def test_fee_up_to_1000():
    result = calculate_pix_fee(500)
    logging.info(f"Transação: R$500, Taxa cobrada: R${result}. Para valores até R$1000, a taxa é de 1%.")
    assert result == 5.0  # 1% of 500 is 5.0

def test_fee_1001_to_5000():
    result = calculate_pix_fee(3000)
    logging.info(f"Transação: R$3000, Taxa cobrada: R${result}. Para valores entre R$1001 e R$5000, a taxa é de 0.5%.")
    assert result == 15.0  # 0.5% of 3000 is 15.0

def test_fee_above_5000():
    result = calculate_pix_fee(6000)
    logging.info(f"Transação: R$6000, Taxa cobrada: R${result}. Para valores acima de R$5000, a taxa é fixa em R$10.")
    assert result == 10.0  # Flat fee of R$10 for amounts above R$5000

if __name__ == '__main__':
    pytest.main()
