
class Set:
    def __init__(self):
        self.elements = {}

    def contains(self, value):
        return value in self.elements

    def insert(self, value):
        if not self.contains(value):
            self.elements[value] = 1
            return True
        
        return False

    def remove(self, value):
        if self.contains(value):
            del self.elements[value]
            return True
        
        return False
    
    def list_elements(self):
        return self.elements.keys()

    def union(self, other_set):
        union_set = Set()

        # insert values from current set
        values = self.list_elements()
        for value in values:
            union_set.insert(value)

        # insert values from another set
        values = other_set.list_elements()
        for value in values:
            union_set.insert(value)

        return union_set
    
    def intersection(self, other_set):
        intersection_set = Set()

        values = self.list_elements()
        for value in values:
            if other_set.contains(value):
                intersection_set.insert(value)

        return intersection_set

    def difference(self, other_set):
        difference_set = Set()

        values = self.list_elements()
        for value in values:
            if not other_set.contains(value):
                difference_set.insert(value)

        return difference_set
    
    def print(self):
        values = self.list_elements()
        for value in values:
            print(value, end=" ")

