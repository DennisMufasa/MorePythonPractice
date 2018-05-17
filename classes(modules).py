class Employees:        # create a class called employees
    def __init__(self, name, position, salary ):        # initializing class variables
        """Assigning class variables their values"""
        self.name = name
        self.position = position
        self.salary = salary

    """Creating a few functions contained in the class"""
    def delegation(self):
        self.position = self.position.lower()  # this is to make the if statement below consistent with the parsed value
        if self.position == 'developer':
            print(self.name + ' is a dev at our company')


# using the class and its fn
"""creating an instance of the class"""
mimi = Employees('mufasa', 'Developer', 100000)
"""using one of the functions in the class employees"""
mimi.delegation()

