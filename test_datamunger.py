import unittest
from datamunger import *

class Test_program(unittest.TestCase):

    def test_calc_total(self):

     self.assertEqual(sum([3,6,7,8,9,17]), 50, "Should be equal to 50")

     self.assertEqual(sum([-2,5,0,-10,12]), 5,"Should be equal to 5")

     arr = [1,2,3,4,5,6,7,8]
     computed =0

     for i in arr[2:8]:
         computed=computed+i
    
     self.assertEqual(computed,33, "Should be equal to 33")

    
    def test_check_monotonic(self):
        

        arr1 = [10,12,12,14,16,16,20]

        is_montonic = False

        for i in arr1[0:7]:
            if (i+1)>=i :
                is_montonic = True
            else:
                is_montonic = False
        
        self.assertTrue(is_montonic, True)

        arr2 = [12,10,11,13,12]     
        
        is_montonic2= False


        for i in arr2[0:5]:
            if  i> i+1:
                is_montonic2 = True
                print(is_montonic2)
            else:
                is_montonic2 = False

        self.assertFalse(is_montonic2, False)


if __name__ == "__main__":
        unittest.main()
      



  
     



  

        
                

         
         



