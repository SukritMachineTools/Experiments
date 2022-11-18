from pressBrakeP import pressBrake

class home():
    def home(self):
        try:
            pb=pressBrake()
            pb.pressBrakeFrame()

        except Exception as e:
            print(e)

if __name__=='__main__':
    h=home()
    h.home()