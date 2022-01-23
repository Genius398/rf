class parent():
    def __init__(self):
        print("This is a parent class boi")
        
        
        
    def menu(dish):
        if dish=="burger":
            print("YOu can add more stuff")
            print("More Cheese | Add Jalapeno")
            
        elif dish=="iced_americano":
            print("You can add more stuff")
            print("Chocolate | Caramel")
            
        else:
            print("choose a valid option")
            
            
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            print("250 USD")
            
        if dish=="burger" and add_ons=="jalepeeno":
            print("350 USD")
            
        if dish=="iced_americano" and add_ons=="chocolate":
            print("250 USD")
            
        if dish=="iced_americano" and add_ons=="caramel":
            print("250 USD")
            
#=======================================================================#      
            
class child1(parent):
    def __init__(self, dish):
        self.new_dish = dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        


class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)
        

child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger", "jalepeeno")
child2_object.get_final_amount()





