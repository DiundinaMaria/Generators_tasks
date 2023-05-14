from datetime import datetime, timedelta


class ThueMorseGenerator:
    def __init__(self, seed: str) -> None:
        if seed != '0' and seed != '1':
            raise AttributeError

        self.seed = seed
        self.sequence = seed

    def next(self):
        inverted = bin(~int(self.sequence, 2))[3:]
        self.sequence = ''.join([self.sequence, inverted])

    def get_seq(self):
        return self.sequence


if __name__ == "__main__":
    gen = ThueMorseGenerator('0')
    start = datetime.now()
    end = start + timedelta(hours=1)
    try:
        while datetime.now() < end:
            gen.next()
    except MemoryError:
        print("Not enough memory")
        with open("thue_morse_result.txt", "w") as file:
            file.write(gen.get_seq())
    else:
        print("1 hour has passed")
        with open("thue_morse_result.txt", "w") as file:
            file.write(gen.get_seq())
