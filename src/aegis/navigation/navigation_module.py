from ..core.base_module import BaseModule

class NavigationModule(BaseModule):
    def __init__(self):
        super().__init__("Navigation")
        self.current_coordinates = [0, 0, 0]
        self.target_coordinates = None

    def update(self):
        if self.target_coordinates:
            self.status = "NAVIGATING"
            # Simulate movement
            for i in range(3):
                if self.current_coordinates[i] < self.target_coordinates[i]:
                    self.current_coordinates[i] += 1
        else:
            self.status = "STATION_KEEPING"
        
        return self.current_coordinates
