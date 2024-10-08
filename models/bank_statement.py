# models/bank_statement.py
from pydantic import Field, BaseModel
from enum import Enum
from typing import List

class CreditOrDebit(str, Enum):
    credit = "credit"
    debit = "debit"

class DescriptionType(str, Enum):
    asset = "asset"
    liability = "liability"
    equity = "equity"
    revenue = "revenue"
    expense = "expense"

class BankStatement(BaseModel):
    date: str
    amount: float
    description: str = Field(..., description="The exact description as given in the bank statement.")
    vendor_name: str = Field(..., description="The name of the vendor or company present in the description.")
    transaction_description: str = Field(..., description="Summary of the description.")
    credit_or_debit: CreditOrDebit
    description_label: DescriptionType

class BankStatements(BaseModel):
    checking_account_beginning_balance: float
    bankstatement: List[BankStatement]
