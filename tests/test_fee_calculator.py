from transacoes.fee_calculator import calculate_pix_fee

def test_fee_below_limit():
    assert calculate_pix_fee(500.00) == 5.0

def test_fee_above_limit():
    assert calculate_pix_fee(2000.00) == 10.0
