USD_to_INR = 89.96
USD_to_EUR = 0.86
EUR_to_INR = 105.08


def usd_to_inr(amount):
    return amount * USD_to_INR

def inr_to_usd(amount):
    return amount / USD_to_INR

def usd_to_eur(amount):
    return amount * USD_to_EUR

def eur_to_usd(amount):
    return amount / USD_to_EUR

def eur_to_inr(amount):
    return amount * EUR_to_INR

def inr_to_eur(amount):
    return amount / EUR_to_INR