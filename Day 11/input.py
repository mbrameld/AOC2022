monkies = """Monkey 0:
  Starting items: 83, 88, 96, 79, 86, 88, 70
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 59, 63, 98, 85, 68, 72
  Operation: new = old * 11
  Test: divisible by 5
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 2:
  Starting items: 90, 79, 97, 52, 90, 94, 71, 70
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 3:
  Starting items: 97, 55, 62
  Operation: new = old + 5
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 4:
  Starting items: 74, 54, 94, 76
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 58
  Operation: new = old + 4
  Test: divisible by 17
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 6:
  Starting items: 66, 63
  Operation: new = old + 6
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 7:
  Starting items: 56, 56, 90, 96, 68
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 1"""
