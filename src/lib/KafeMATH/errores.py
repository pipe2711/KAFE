def raiseDomainError(func_name):
    raise Exception(f"{func_name}: Domain error")

def raiseNonEqualLength(func_name):
    raise ValueError(f"{func_name}: Non equal-length sequences")
