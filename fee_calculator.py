def calculate_pix_fee(transaction_amount: float) -> float:
    """
    Calcula a taxa de transação PIX para contas PJ do Be Bank.

    Rules:
    - Taxa de 1% sobre o valor da transação.
    - Taxa máxima de R$10 por transação.

    Args:
        transaction_amount (float): O valor da transação PIX.
        
    Returns:
        float: A taxa a ser cobrada.
    """
    # Copilot will complete logic here
    fee = transaction_amount * 0.01
    maximum_fee = 10.0
    return min(fee, maximum_fee)
