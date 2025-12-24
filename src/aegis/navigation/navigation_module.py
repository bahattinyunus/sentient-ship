from ..core.base_module import BaseModule

class NavigationModule(BaseModule):
    """
    SEYR (NAVIGATION) MODÜLÜ
    
    Tasavvufi Karşılık: Seyr-i Süluk (Journey)
    İşlev: Doğru rota (Sırat-ı Müstakim) tayini.
    """
    def __init__(self):
        super().__init__("Seyr")
        self.current_coordinates = [0, 0, 0] # [Zahir, Batın, Hakikat]
        self.niyet_menzili = None # Target

    def niyet_et(self, hedef):
        self.niyet_menzili = hedef
        self.logger.info(f"Niyet edildi: Menzil {hedef}")

    def update(self):
        if self.niyet_menzili:
            self.status = "SEYR HALİNDE"
            # Hareketi simüle et (Yolculuk)
            diff = [t - c for t, c in zip(self.niyet_menzili, self.current_coordinates)]
            
            # Adım adım yaklaş
            for i in range(3):
                if abs(diff[i]) > 0.1:
                    step = 1 if diff[i] > 0 else -1
                    self.current_coordinates[i] += step
            
            self.logger.info(f"Manevi Konum: {self.current_coordinates}")
            
            if self.current_coordinates == self.niyet_menzili:
                self.logger.info("VUSLAT! Menzile erişildi.")
                self.niyet_menzili = None
        else:
            self.status = "RABITA (Stationary)"
            # Boş durma, zikir çek (Idle animation equiv)
        
        return self.current_coordinates
