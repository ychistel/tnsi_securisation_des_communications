class crypto:
    
    def __init__(self,msg):
        self.msg = msg
        self.chiffre = 0
        self.base = 2**8
        self.modulo = 2**1024

    def hacher(self):
        for c in self.msg:
            self.chiffre = self.chiffre * self.base + ord(c)
        self.chiffre = self.chiffre % self.modulo

    def afficher(self):
        print(self.chiffre)
        code = hex(self.chiffre)[2:]
        n = len(code)
        print("n=",n)
        if n % 2 == 0:
            msg = ''
            for i in range(n//2):
                msg = msg + code[2*i:2*i+2] 
        else:
            msg = code[0] + ' '
            for i in range(1,n//2):
                msg = msg + code[2*i:2*i+2]
        print(msg)
        
        
msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum euismod, \
mauris ut sodales hendrerit, ex nisi cursus leo, egestas rhoncus libero felis nec nulla. \
Cras pellentesque quam in pulvinar ornare. Praesent blandit ultrices lacus ut tincidunt. \
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos \
himenaeos. Praesent eget rutrum mauris. Nulla libero libero, laoreet sit amet nisl \
sed, auctor eleifend erat. Morbi condimentum faucibus risus non commodo. Etiam dapibus \
auctor ultrices. In aliquet lectus metus, a elementum leo placerat nec. Aenean \
condimentum aliquam mi in ultricies. In eleifend dui enim, ac ornare erat consectetur \
quis. Praesent molestie nulla quis nisi pulvinar feugiat. Nulla vel mauris \
sollicitudin, posuere risus quis, auctor purus. Morbi lacus quam, tristique at \
semper vitae, finibus in massa."
#msg = "bonjour"
message = crypto(msg)
message.hacher()
message.afficher()

