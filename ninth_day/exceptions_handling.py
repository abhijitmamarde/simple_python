def div_2_nos_v1(n1, n2):
    res = n1/n2
    print(res)
    return res

# with possible exception handled
def div_2_nos(n1, n2):
    try:
        res = n1/n2
    # except:
    except ZeroDivisionError:
        print("Divider cannot be 0, result not calculated!")
        return 0.0
    except NameError:
            print("NameError occured!")
            return 0.0
    except Exception as err:
        print(f"Some unknown error occured! {err}")
        return 0.0
    else:
        print("This means no exception occured!")
    finally:
         print("This will be always executed!!!")
    
    
    print(res)
    return res

# this would Stop the program, 
# div_2_nos_v1(10, 0)

# this wont stop the program
div_2_nos(10, 0)

print("DONE the execution completely!")

