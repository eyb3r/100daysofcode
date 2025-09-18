from datetime import date


class Operation:
    def __init__(self, title: str, amount: int, category: str, date_: date = date.today()):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date_

    def to_dict(self):
        str_date = "-".join((str(self.date.month), str(self.date.year - 2000)))
        return {"title": self.title,
                "category": self.category,
                "date": str_date,
                "amount": self.amount,
                }


class Income(Operation):
    def __init__(self, title: str, amount: int, category: str, date_: date):
        super().__init__(title, amount, category, date_)


class Expense(Operation):
    def __init__(self, title: str, amount: int, category: str, date_: date, subscription: bool = False):
        super().__init__(title, amount, category, date_)
        self.subscription = subscription

    def to_dict(self):
        result = super().to_dict()
        result["subscription"] = self.subscription
        return result
