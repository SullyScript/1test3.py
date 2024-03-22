# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check
import load_data
#import load_data module here
#from load_data import character_occupation_list, character_strength_list, 
#character_luck_list, character_weapon_list, load_data, calculate_health
 
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "55"

#==========================================#
#Do not modify the code already provided.

###
#In a file named test3.py, write a test function named test_return_correct_dict_inside_list to test that all six functions in the load data module, the dictionaries inside the list have the correct data. A general character’s data is stored in the following format (although some keys may or may not be present depending on which function is being tested)
#{'Occupation': 'WA', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}.
#We recommend testing the first and the last element in the list.
#For each function except load_data you need to provide at least 3 test cases: 5 functions * 3 test/function = 15 test cases
#For function load_data, you need to provide 6 test cases.
#That’s 21 test cases in total.
###

def test_return_correct_dict_inside_list():
    
    filename = "characters-test.csv"
    result = load_data.character_occupation_list(filename)
    
    
    
    expected_first = {'Occupation': 'Warrior', 'Agility': 11, 'Stamina': 9, 'Personality': 10, 
                      'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}
    
    expected_last = {'Occupation': 'Mage', 'Agility': 7, 'Stamina': 2, 'Personality': 11, 
                     'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}
      
    
    
    check.equal(result[0], expected_first, "First character data incorrect.")
    check.equal(result[-1], expected_last, "Last character data incorrect.") 
    
    check.summary()
    
if __name__ == "__main__":
    test_return_correct_dict_inside_list()
    
    
    
    """
    expected_last = {'Occupation': 'Warrior', 'Agility': 11, 'Stamina': 9, 'Personality':10,
             'Intelligence': 8, 'Luck': 0.61, 'Armor': 11, 'Weapon': 'Spear'}   
    
    """
    
    
    #print("Testing with simplified function call...")
    result = load_data.character_occupation_list("characters-test.csv")
    #print("Result:", result)
    #print(dir(load_data))
        # Here, manually check if the result looks correct before adding checks
    
    #test_simplified()
    
    #Complete the function with your test cases
    """
    #filename = "characters-test.csv"
    result = load_data.character_occupation_list(filename)
    
    expected_first = {'Occupation': 'Warrior', 'Agility': 10, 'Stamina': 15}
    # Expected structure and values for the last character (assuming known data for the test case)
    expected_last = {'Occupation': 'Mage', 'Agility': 12, 'Stamina': 14}
    
    # Check that the first and last items in the list match the expected dictionaries
    check.equal(result[0], expected_first, "First character data incorrect.")
    check.equal(result[-1], expected_last, "Last character data incorrect.")    
    
    check.summary()
    """
    #test that character_occupation_list returns a correct dictionary inside the list (3 different test cases required)
    
    
    #test that character_strength_list returns a correct dictionary inside the list  (3 different test cases required)
    
    
    #test that character_luck_list returns a correct dictionary inside the list  (3 different test cases required)
    
    
    #test that character_weapon_list returns a correct dictionary inside the list (3 different test cases required)
    
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    
    #test that calculate_health returns a correct dictionary inside the list  (3 different test cases required)
    
    
   


# Do NOT include a main script in your submission
