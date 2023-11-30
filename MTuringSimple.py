def SimpleTuringMachine1(word):
    
    """Simple turing machine that accepts L , an infinite language such
    as it starts with n number of a followed by the same number of b and c

    Args:
        word (_string_): _the word to test_

    Returns:
        _type_: _bool and strings to say why the word was rejected by the TM_
    """
    
    if not(word.startswith("a")):
        return "FAIL : START NOT a"
    if not(word.endswith("c")):
        return "FAIL : END NOT c"
    
    suma = sumb = sumc = 0
    current_char = "a"
    
    for char in word:
        if char == "a":
            if current_char != "a":
    
                print(f"Found {current_char} after the initial a block")
                return False
            
            suma +=1
        
        if char == "b":
            current_char = "b"
            if current_char == "c":
                print(f"Found {current_char} after the initial b block")
                return False
            
            sumb += 1
        
        if char == "c":
            current_char = "c"
            if current_char != "c":
                print(f"Found {current_char} after the initialcb block")
                return False
            
            sumc += 1
            
        
    if suma == sumb == sumc :
        return "OK"
        
    elif suma != sumb:
        return "FAIL: a and b not equal"
    
    elif suma != sumc:
        return "FAIL: a and c not equal "
    
    elif sumb != sumc:
        return "FAIL: c and b not equal"
    
    
    print("RUN FINISHED")
   
   
def SimpleTuringMachine2(word): 
    """_A function that accepts languages such as aa$bb or ab$ab where the $ spilts twin squences_

    Args:
        word (_string_): _word to check_

    Returns:
        _string _: _OK or FAIL if the word is accepted or rejected_
    """
    
    middle_char = int(len(word) / 2)
    if word[middle_char: middle_char + 1] != "$":
        print("FAIL: $ IS NOT THE MIDDLE OF THE WORD")
        
    part_one =  word[0:middle_char]
    part_two = word[middle_char+1:]
    
    if len(part_one) != len(part_two) :
        print("FAIL: $ does not split in equal parts")
    
    if part_one == part_two:
        print("OK")
        
    else:
        print("FAIL : NOT SAME SEQUENCE")
    return " "

# Now what i will do is , after discovering the logic of accepting/rejecting words , i will try to emulate a pushdown automaton that does the same
#thing as SimpleTuringMachine2 with a stack


def SimplePushDownAutomaton(word):
    """_A function that emulates a pushdown Automaton with a stak that accepts L an infinite language that
        is defines as a^nb^n on {a,b} alphabet, empty word rejected_

    Args:
        word (_string_): _word to check_

    Returns:
        _string _: _OK or FAIL if the word is accepted or rejected_
    """
   
    stack = ["#"]
    current_char = "a"
    
    if word[0] != "a":
        
        print("FAIL: WORD MUST START WITH a")
        return False
    
    for char in word:
        if char != "a" and char != "b":
            print(f"Illegal to use {char}")
            return False

    for char in word:
        
        
        if char == "a":
            stack.append("a")
 
        if char =="b":
            
            print(f"STACK AFTER READING  a  IS {stack}")
            current_char = "b"
            if current_char == "a":
                print("FAIL: FOUND a AFTER b")
                return False
            stack.pop()
            
            print(f"STACK AFTER READING  b  IS {stack}")
            
    if stack == ["#"]:
        stack.pop()
        print(stack)
        print("OK")
        return True
                
    else:
        print("FAIL: NOT EQUAL NUMBER OF A AND B")
        return False
            

                
            
     
    
    
    
  

    
    

