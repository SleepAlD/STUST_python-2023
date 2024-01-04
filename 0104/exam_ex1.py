class Fried_Chicken :

    #空建構
    def __init__(self) -> None:
        pass     
    
    #訂單寫入
    def Book_fried_chicken(self, buyers_name, meal_part, meal_spicy, meal_portion, meal_sum) : 
        self.name = buyers_name
        self.part = meal_part
        self.sum = meal_sum
        self.portion = meal_portion
        self.spicy = meal_spicy

    #確認並顯示顧客訂單
    def Cheak_book(self) :
        print(f"{self.name}'s Order :\n")
        print(f"{self.part} , {self.portion} , {self.spicy} x{self.sum}\n")

    #告知金額
    def Order_charges(self):

        #將雞翅各部位的價格寫入字典
        price = {
            'chicken wing' : 39,
            'chicken breast' : 49,
            'chicken ass' : 69
        }

        #將雞翅各份量的價格倍率寫入字典
        portion = {
            'Small' : 1,
            'Medium' : 1.5,
            'Large' : 2,
            'Very Large' : 3
        }

        #從字典中確認是否有要購買的部位以及分量的大小 計算並告知價格
        if self.part in price :
            order_price = self.sum * price[self.part]
        if self.portion in portion :
            order_price *= portion[self.portion]
        print(f"Mr.{self.name} your need to pay {order_price} dollar to take your order.")

John = Fried_Chicken()
Davis = Fried_Chicken()
Carter = Fried_Chicken()
James = Fried_Chicken()

#輸入顧客訂單
John.Book_fried_chicken("John", "chicken ass", "No Spicy", "Large", 3)
Davis.Book_fried_chicken("Davis", "chicken wing", "Very Spicy", "Small", 5)
Carter.Book_fried_chicken("Carter", "chicken ass", "Small Spicy" ,"Medium" ,6)
James.Book_fried_chicken("James", "chicken wing", "Medium Spicy", "Very Large", 10)

#讓顧客確認訂單並告知付款金額
John.Cheak_book()
John.Order_charges()
print("-------------------------------------------------------------\n")

Davis.Cheak_book()
Davis.Order_charges()
print("-------------------------------------------------------------\n")

Carter.Cheak_book()
Carter.Order_charges()
print("-------------------------------------------------------------\n")

James.Cheak_book()
James.Order_charges()
print("-------------------------------------------------------------\n")




