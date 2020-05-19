class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        pass

    def length_is_greater_than_one(self):
        return len(self.card_num) > 1

    def is_numeric(self):
        for i in range(len(self.card_num)):
            if not self.card_num[i].isnumeric():
                return False
        return True

    def validate_luhn(self):
        normalized = [int(x) for x in self.card_num]
        for i in range(len(normalized)):
            reverse_index = -(i + 1)
            is_even = reverse_index % 2 == 0
            if is_even:
                double = normalized[reverse_index] * 2
                greater_than_nine = double > 9
                if greater_than_nine:
                    normalized[reverse_index] = double - 9
                else:
                    normalized[reverse_index] = double
        if sum(normalized) % 10 == 0:
            return True
        return False
    
    def valid(self):
        if self.is_numeric() and self.length_is_greater_than_one():
            return self.validate_luhn()
        return False
