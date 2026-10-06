# Mini Banking System

A clean object-oriented Python architecture modeling ledger accounts, deposits, withdrawals, and balance transfers.

## Architecture
- `Transaction`: Records immutable audit log entries (type, timestamp, balance after).
- `Account`: Encapsulates customer balance state and transaction history.
- `Bank`: Coordinates atomic funds transfers and account lifecycle.

## Complexity
- Account Creation: $O(1)$
- Deposit / Withdrawal: $O(1)$
- Inter-account Transfer: $O(1)$
- Memory: $O(T)$ proportional to number of transactions.

## How to Run & Test
```bash
python banking.py
python -m unittest discover tests
```
