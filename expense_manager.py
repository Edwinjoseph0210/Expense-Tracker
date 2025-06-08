import json
from collections import defaultdict

class ExpenseManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.expenses, f, indent=2)

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        self.save_expenses()

    def get_expenses(self):
        return self.expenses

    def get_summary(self):
        summary = defaultdict(float)
        for exp in self.expenses:
            summary[exp['category']] += exp['amount']
        return dict(summary)
