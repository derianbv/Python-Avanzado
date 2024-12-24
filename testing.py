############################### Pruebas ############################################
"""
Tenemos que crear una clase de prueba que va a tener varios test (ya pre establecidos por la clase unit test) que pueden ser los siguientes:

assertEqual	Verifica si dos valores son iguales.
assertNotEqual	Verifica si dos valores son diferentes.
assertTrue	Verifica si una condición es verdadera.
assertFalse	Verifica si una condición es falsa.
assertIs	Verifica si dos objetos son el mismo.
assertIsNot	Verifica si dos objetos son diferentes.
assertIn	Verifica si un elemento está en una colección.
assertRaises	Verifica si se lanza una excepción esperada.


Ejemplo:     self.assertEqual(2 + 2, 4) -> ture

"""

# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from mymodule import square, double

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.

        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.

# Define a test case class for testing the 'double' function.
class TestDouble(unittest.TestCase): 

    # Define the first test method for the 'double' function.
    def test1(self): 
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.

        # Check that calling 'double(-3.1)' returns -6.2.
        # This tests if the function correctly computes double of -3.1, verifying that it handles negative float inputs.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.

        # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()


#################### OTRO EJEMPLO EXPLICADO ############################################




from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

import unittest



class TestSentimentAnalyzer(unittest.TestCase): 

    def test_sentiment_analyzer(self): 
        
        
        self.assertEqual(
            sentiment_analyzer('I love working with Python')['label'],'SENT_POSITIVE'
         )
        
        self.assertEqual(
            sentiment_analyzer('I hate working with Pyhton')['label'],'SENT_NEGATIVE'
         )

         self.assertEqual(
            sentiment_analyzer('I am neutral on Python')['label'],'SENT_NEUTRAL'
         )


unittest.main()


# Luego solo debemos correr el archivo y si detecta algun error, sacará algo así: 

'''

======================================================================
ERROR: test_sentiment_analyzer (__main__.TestSentimentAnalyzer.test_sentiment_analyzer)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/project/practice_project/test_sentiment_analysis.py", line 13, in test_sentiment_analyzer
    sentiment_analyzer('I love working with Python')['label'],'SENT_POSITIVE'
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
KeyError: 'label'

----------------------------------------------------------------------
Ran 1 test in 0.255s

FAILED (errors=1)
'''

# si pasa debería ser así: 

'''
.py 
.
----------------------------------------------------------------------
Ran 1 test in 1.100s

OK
'''
