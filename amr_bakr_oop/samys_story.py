class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = max(0, min(health_rate, 100))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        else:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10  


class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance, velocity):
        self.car.run(distance, velocity)

    def refuel(self, amount):
        self.car.fuel_rate += amount


class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = max(0, min(fuel_rate, 100))
        self.velocity = max(0, min(velocity, 200))

    def run(self, distance, velocity):
        self.velocity = velocity
        self.fuel_rate -= (distance // 10) * 10 
        if self.fuel_rate <= 0:
            self.stop()

    def stop(self):
        self.velocity = 0
        print(f" {self.name} need fuel !")


class Office:
    employees_num = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        Office.employees_num += 1

    def fire(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        Office.employees_num -= 1

    def get_all_employees(self):
        return [e.name for e in self.employees]

    def check_lateness(self, emp_id, move_hour):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                arrival_time = move_hour + (employee.distance_to_work / employee.car.velocity)
                return "Late" if arrival_time > 9 else "On Time"



samy_car = Car("Fiat 128", 80, 100)  
samy = Employee("Samy", 5000, "Neutral", 90, 1, samy_car, "samy@iti.eg", 12000, 20)
iti_office = Office("ITI")
iti_office.hire(samy)


print("Samy details :")
print(f"Name: {samy.name}")
print(f"Money: {samy.money} EGP")
print(f"Mood: {samy.mood}")
print(f"Salary: {samy.salary} EGP")
print(f"Car: {samy.car.name}")
print(f"Fuel Level: {samy.car.fuel_rate}%")
print(f"Email: {samy.email}")
print("*" * 50)


samy_move_hour = 8  
samy.drive(20, 100)


status = iti_office.check_lateness(samy.emp_id, samy_move_hour)


print("\nSamy details during work:")
print(f"Speed: {samy.car.velocity} km/h")
print(f"Remaining Fuel: {samy.car.fuel_rate}%")
print(f"Arrival Status: {status}")
print("*" * 50)

samy.work(8)

print("\nSamy details after work:")
print(f"Mood: {samy.mood}")
print(f"Remaining Money: {samy.money} EGP")
print("*" * 50)


