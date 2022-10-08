#  1 which generation are you
 def generation(x, y):
	g = {
		-3: {
			"m": "great grandfather",
			"f": "great grandmother",
		},
		-2: {
			"m": "grandfather",
			"f": "grandmother",
		},
		-1: {
			"m": "father",
			"f": "mother",
		},
		0: {
			"m": "me!",
			"f": "me!",
		},
		1: {
			"m": "son",
			"f": "daughter",
		},
		2: {
			"m": "grandson",
			"f": "granddaughter",
		},
		3: {
			"m": "great grandson",
			"f": "great granddaughter",
		}
	}
    return g[x][y]
# 2 correct the mistakes
  def squared(b):
	return a * a

# 3 less than 100
  def less_than_100(a, b):
	if a + b < 100 :
	 return True
	else :
	 return False
# 4 Convert Minutes into Seconds
  def convert(minutes):
	return minutes * 60
# 5 Return the First Element in a List
  def get_first_value(number_list):
	return number_list[0]
# 6 Extract City Facts
  def city_facts(city):
	return "{} has a population of 1 {} and is situated in {}".format(city.name,city.population,city.continent)
# 7 recursion length of a string 
   def length(txt):
	return len(txt)
# 8 area of a triangle
   def tri_area(base, height):
	return base * height / 2
# 9 Return the Remainder from Two Numbers
  def remainder(x, y):
	return x % y
# 10 Compare Strings by Count of Characters
   def comp(txt1, txt2):
	if len(txt1) = len(txt2):
	 return True
	else : 
	 return False
# 11 To the Power of _____
 def calculate_exponent(num, exp):
	 return pow(num,exp)
# 12 Return the Next Number from the Integer Passed
def addition(num):
	return num + 1
# 13 Return the Sum of Two Numbers
 def addition(a, b):
	 return a + b
# 14 how edabit works
 def hello():
     return "hello edabit.com"
# 15 Find the Largest Number in a List
  def findLargestNum(nums):
	return max(nums)