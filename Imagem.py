import qrcode, configparser

class Imagem:
    def __init__(self, site):
        config = configparser.ConfigParser()
        config.read('Common.ini')
        self.config = config
        self.site = site
    
    def getSite(self):
        return self.site
    
    def setSite(self, site):
        self,site = site
    
    def geraQr(self, cor, cor_fundo):
        qr = qrcode.QRCode(
            version = 1,
            box_size = 10,
            border = 4,
        )
        qr.add_data(self.site)
        qr.make(fit=True)
        img = qr.make_image(fill_color = str(cor), back_color = str(cor_fundo))
        img.save('qrvic.png')

        
        
    
       