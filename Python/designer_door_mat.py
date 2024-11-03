def door_mat_design(n,m):
    try:
        if n%2 != 0 and m == n*3: # Make sure n is odd number and m is equal to 3*n
            # Print all lines above WELCOME
            for i in range(n//2):
                for j in range((m-3*(2*i+1))//2):
                    print("-",end="")
                    
                print(".|."*(2*i+1),end="")
                
                for j in range((m-3*(2*i+1))//2):
                    print("-",end="")
                
                print()
            # Print WELCOME line
            for i in range((m-7)//2):
                print("-",end="")
                
            print("WELCOME",end="")
            
            for i in range((m-7)//2):
                print("-",end="")
                
            print()
            # Print lines below WELCOME
            for i in range(n//2-1,-1,-1):
                for j in range((m-3*(2*i+1))//2):
                    print("-",end="")
                    
                print(".|."*(2*i+1),end="")
                
                for j in range((m-3*(2*i+1))//2):
                    print("-",end="")
                    
                print()    
        else:
          raise Exception
            
                    
    except Exception:
        print("Input value is not as per requirement")           

n,m = input().split()
n,m = int(n), int(m)
door_mat_design(n,m)
