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
    # Define the fee structure
    if transaction_amount <= 1000:
        fee = 0.01 * transaction_amount   # 1% for amounts up to R$1000
    elif transaction_amount <= 5000:
        fee = 0.005 * transaction_amount  # 0.5% for amounts between R$1001 and R$5000
    else:
        fee = 10.0                        # R$10 for amounts above R$5000
    
    return fee
