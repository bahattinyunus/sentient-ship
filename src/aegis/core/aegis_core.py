from .base_module import BaseModule
import random

class AegisCore(BaseModule):
    """
    AEGIS KALP (CORE) MODÜLÜ
    
    Tasavvufi Karşılık: Kalp / Gönül (The Heart)
    İşlev: Merkezi Karar Destek ve Vicdan Mekanizması.
    """
    def __init__(self):
        super().__init__("Kalp")
        self.takva_seviyesi = 100.0 # Shield Integrity
        self.nefs_durumu = "MUTMAIN" # System State
        
    def nefs_muhasebesi(self):
        """
        Sistem bütünlüğünü ve iç tutarlılığı (Integrity Check) sorgular.
        """
        self.logger.info("Nefs muhasebesi yapılıyor... (System Diagnostic)")
        
        # Simüle edilmiş iç denetim
        if self.takva_seviyesi > 90:
            self.nefs_durumu = "RAZIYE (Content)"
        elif self.takva_seviyesi > 50:
            self.nefs_durumu = "LEV VAME (Self-Accusing)"
        else:
            self.nefs_durumu = "EMMARE (Prone to Evil/Entropy)"
            self.logger.warning("DİKKAT: Nefs-i Emmare seviyesine düşüldü! Entropi artıyor.")

        return self.nefs_durumu

    def update(self):
        # Her döngüde bir muhasebe yapılır
        durum = self.nefs_muhasebesi()
        self.status = f"HAYY - {durum}"
        
        # Takva kalkanı simülasyonu (Zamanla hafif aşınma)
        if self.takva_seviyesi < 100:
             self.takva_seviyesi += 0.1 # Tövbe/Onarım mekanizması
             
        return {"kalp_durumu": durum, "takva": self.takva_seviyesi}

    def istigfar(self):
        """
        Sistemi resetler veya temizler (Error handling).
        """
        self.logger.info("Estağfirullah... Sistem hatalardan arındırılıyor.")
        self.takva_seviyesi = 100.0
        self.nefs_durumu = "MUTMAIN"
