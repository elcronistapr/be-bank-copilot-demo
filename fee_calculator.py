def calculate_pix_fee(transaction_amount: float) -> float:
    """
    Calculates the PIX transaction fee for Be Bank business accounts.

    Rules:
    - 1% fee over the transaction amount.
    - Maximum fee of R$10 per transaction.

    Args:
        transaction_amount (float): The PIX transaction amount.

    Returns:
        float: The fee to be charged.
    """
    # Copilot will complete logic here
    fee = transaction_amount * 0.01
    maximum_fee = 10.0
    return min(fee, maximum_fee)
