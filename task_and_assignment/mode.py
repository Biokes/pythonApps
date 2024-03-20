class Mode:

    @staticmethod
    def mode_value(numbers: list):
        count = 0
        new_count = 0
        mode = numbers[1]
        numbers.sort()
        for number in range(0, len(numbers)):
            for values in range(0, len(numbers)):
                if numbers[number] == numbers[values]:
                    count += 1
            if count >= new_count:
                mode = numbers[number]
                new_count = count
            count = 0
        return [new_count, mode]
