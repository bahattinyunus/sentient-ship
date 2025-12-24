from ..core.base_module import BaseModule

class PropulsionModule(BaseModule):
    """
    HİMMET (PROPULSION) MODÜLÜ
    
    Tasavvufi Karşılık: Himmet / Aşk (Spiritual Zeal)
    İşlev: Harekete geçiren ilahi aşk enerjisi.
    """
    def __init__(self):
        super().__init__("Himmet")
        self.cezbe_katsayisi = 0 # Warp Factor
        self.feyz_cikisi = 100 # Power Output

    def update(self):
        if self.cezbe_katsayisi > 0:
            self.status = "CEZBE HALİ (Warp Active)"
            # Aşk arttıkça güç artar
            self.feyz_cikisi = 100 + (self.cezbe_katsayisi * 33)
            self.logger.info(f"🔥 Motorlar AŞK ile çalışıyor! Güç: {self.feyz_cikisi}%")
        else:
            self.status = "SAKİNLİK (Impulse)"
            self.feyz_cikisi = 20
        
        return self.feyz_cikisi
