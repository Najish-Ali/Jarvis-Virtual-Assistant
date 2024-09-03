import unittest  # Import the unittest library to create and run tests
from src.voice_assistant import VoiceAssistant  # Import the VoiceAssistant class to be tested

class TestVoiceAssistant(unittest.TestCase):
    """
    Test case class for the VoiceAssistant class.
    
    Inherits from unittest.TestCase to provide the testing framework.
    """
    
    def setUp(self):
        """
        Set up the test environment.
        
        This method is called before each test is executed. It initializes
        a new instance of the VoiceAssistant class to be used in the tests.
        """
        self.assistant = VoiceAssistant()
    
    def test_command_processing(self):
        """
        Test the process_command method of the VoiceAssistant class.
        
        This test checks if the process_command method returns the expected
        response for a given command. It verifies that the method correctly
        processes the command and returns the proper output.
        """
        response = self.assistant.process_command("Hello")  # Call the method with a sample command
        self.assertEqual(response, "Hi there!")  # Assert that the response matches the expected output

if __name__ == "__main__":
    unittest.main()  # Run the tests when the script is executed directly
