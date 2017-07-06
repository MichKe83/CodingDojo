class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if price > 10000:
			self.tax = .15
		else: 
			self.tax = .12

		self.price = self.price + (price * self.tax)
		
		

	def displayAll(self):
		print 'Price is: $' + str(self.price)
		print 'Speed: ' + str(self.speed) + 'MPH'
		print 'Fuel: ' + str(self.fuel)
		print 'Mileage: ' + str(self.mileage) + 'MPG'
		print 'Tax: ' + str(self.tax)	


		

#price, speed, fuel, mileage
car1 = Car(11000, 105, 'premium', 32)
car2 = Car(30000, 85, 'nitrous', 13)
car3 = Car(27000, 90, 'unleaded', 31)
car4 = Car(300, 25, 'rubberband', 100)
car5 = Car(8000, 65, 'mid-grade', 26)
car6 = Car(14000, 95, 'unleaded', 22)



car1.displayAll()
car2.displayAll()
car3.displayAll()
car4.displayAll()
car5.displayAll()
car6.displayAll()



'''Assignment: Car
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.'''