from ..core.base_module import BaseModule
import random

class PerceptionModule(BaseModule):
    """
    BASİRET (PERCEPTION) MODÜLÜ
    
    Tasavvufi Karşılık: Basiret (Insight)
    İşlev: Sadece maddeyi değil, manayı da okuma.
    """
    def __init__(self):
        super().__init__("Basiret")
        self.detected_entities = []

    def update(self):
        # Simüle edilmiş sensör taraması (Müşahede)
        if random.random() > 0.6:
            # Hakikat ve Zahir ayrımı
            is_hakikat = random.random() > 0.8
            
            if is_hakikat:
                entity = f"Tecelli_{random.randint(100, 999)} (Mana: Yüksek)"
                self.logger.info(f"✨ BASİRET ÇAKTI: Hakikat nuru tespit edildi -> {entity}")
            else:
                entity = f"Cisim_{random.randint(100, 999)} (Kesif Madde)"
                self.logger.info(f"Madde algılandı: {entity}")
                
            self.detected_entities.append(entity)
        
        # Eski verileri temizle (Masiva'yı terk)
        if len(self.detected_entities) > 5:
            self.detected_entities.pop(0)

        self.status = "MÜŞAHEDE (Scanning)"
        return self.detected_entities
