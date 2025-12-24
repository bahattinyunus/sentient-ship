from ..core.base_module import BaseModule

class PropulsionModule(BaseModule):
    def __init__(self):
        super().__init__("Propulsion")
        self.warp_factor = 0
        self.power_output = 100

    def update(self):
        if self.warp_factor > 0:
            self.status = "WARP_ENGAGED"
            self.power_output = 100 + (self.warp_factor * 10)
        else:
            self.status = "THRUSTERS_READY"
            self.power_output = 20
        
        return self.power_output
