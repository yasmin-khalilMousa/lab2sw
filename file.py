class SimpleMath:
	@staticmethod
	def add(a, b):
		return a + b

	@staticmethod
	def subtract(a, b):
		return a - b

	@staticmethod
	def multiply(a, b):
		return a * b

	@staticmethod
	def divide(a, b):
		if b == 0:
			raise ValueError("Cannot divide by zero")
		return a / b


def _demo():
	sm = SimpleMath()
	a, b = 10, 2
	print(f"{a} + {b} = {sm.add(a, b)}")
	print(f"{a} - {b} = {sm.subtract(a, b)}")
	print(f"{a} * {b} = {sm.multiply(a, b)}")
	print(f"{a} / {b} = {sm.divide(a, b)}")


if __name__ == "__main__":
	_demo()