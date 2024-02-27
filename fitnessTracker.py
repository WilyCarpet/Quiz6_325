"""
This program implements a fitness tracker system that collects, stores, and displays user activity data.
The design adheres to the SOLID principles as follows:

S - Single Responsibility Principle (SRP):
    - Each class has a single responsibility:
        - User: Represents user data.
        - Activity: Represents different types of activities and calculates metrics.
        - DataStorage: Abstract class for storing activity data.
        - MemoryStorage: Concrete class for storing activity data in memory.
        - Display: Abstract class for displaying activity data.
        - WebPageDisplay: Concrete class for displaying activity data on a web page.
        - ActivityMonitor: Monitors user activity and coordinates data storage and display.

O - Open-Closed Principle (OCP):
    - The system is open for extension but closed for modification.
    - New activity types can be added without modifying existing classes by implementing the Activity interface.
    - Data storage and display functionality can be extended without modifying ActivityMonitor by subclassing DataStorage and Display.

L - Liskov Substitution Principle (LSP):
    - Subclasses of Activity adhere to the contracts defined by the Activity class.
    - Subclasses of Display adhere to the contracts defined by the Display class.
    - Made Land Subclass to distinguish between activities that could track steps

I - Interface Segregation Principle (ISP):
    - Separate interfaces are defined for data storage (DataStorage) and display (Display) concerns.
    - This allows clients to depend only on the interfaces they use, promoting loose coupling.

D - Dependency Inversion Principle (DIP):
    - Dependencies such as DataStorage and Display are injected into the ActivityMonitor constructor.
    - This promotes loose coupling and facilitates testing by allowing dependencies to be easily swapped.
"""
from abc import ABC, abstractmethod

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

class Activity(ABC):
    def __init__(self):
        self.calories = 0
        self.distance_traveled = 0

    
    @abstractmethod
    def calculate_distance(self,beginPoint,endPoint):
        pass
    
    #I am just saying that calories burned is equal to your 
    # (distance traveled * 0.1) * ActivityRate e.g. walking = 1, running = 2
    @abstractmethod
    def calories_burned(self):
        pass

#Since activities like swimming don't need steps
class Land(ABC):
    def __init__(self):
        self.steps = 0
    
    #Im saying it takes about 150 steps to walk 100 meters so 1 meter = 1.5 steps
    @abstractmethod
    def total_steps(self,distance):
        pass

class Walking(Activity,Land):
    def calculate_distance(self,beginPoint,endPoint):
        distance = beginPoint - endPoint
        self.calories = (distance * 0.1) * 1

        self.distance_traveled = distance
    
    def total_steps(self,distance):
        self.steps = distance * 1.5


class Running(Activity,Land):
    def calculate_distance(self,beginPoint,endPoint):
        distance = beginPoint - endPoint
        self.calories = (distance * 0.1) * 2

        self.distance_traveled = distance
    
    def total_steps(self):
        self.steps = self.distance_traveled * 1.5


class Swimming(Activity):
    def calculate_distance(self,beginPoint,endPoint):
        distance = beginPoint - endPoint
        self.calories = (distance * 0.1) * 3

        self.distance_traveled = distance

#Making DataStorage an abstract so you can easaily change how you store the data
class DataStorage(ABC):
    @abstractmethod
    def store_data(self, data):
        pass

class MemoryStorage(DataStorage):
    def __init__(self):
        self.dataBase = []

    def store_data(self, data):
        self.dataBase.append(data)

#Making Display an abstract class so you can esaily switch the type of display you want
class Display(ABC):
    @abstractmethod
    def display_data(self, data):
        pass

class WebPageDisplay(Display):
    def __init__(self,dataBase):
        self.database = dataBase
    def display_data(self,data):
        for data in self.database:
            if isinstance(data,Land):
                print(f'Distance: {data.distance_traveled}, Steps: {data.steps}Calories Burend: {data.calories}')
            else:
                print(f'Distance: {data.distance_traveled}, Calories Burend: {data.calories}')

class ActivityMonitor:
    def __init__(self, data_storage: DataStorage, display: Display):
        self.data_storage = data_storage
        self.display = display

    def monitor_activity(self, activity: Activity, beginPoint, endPoint):
        # Collect activity data
        activity.calculate_distance(beginPoint,endPoint)
        if isinstance(activity,Land):
            activity.total_steps()
        data = activity
        
        # Store data
        self.data_storage.store_data(data)
        
        # Notify display
        self.display.display_data(data)
