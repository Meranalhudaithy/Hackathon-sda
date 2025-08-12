#another flexxxx




def expr_original(A, B, C):
  
    return (
        (A and (not B))
        or ((not A) and C and (not B))
        or (A and C and (not B))
        or ((not B) and (not C))
        or (((A or C)) and (not B))
        or ((not A) and (not B))
    )

def expr_simplified(A, B, C):
   
    return not B

def verify_equivalence(verbose: bool = False) -> bool:

    ok = True
    if verbose:
        print("A  B  C        Original      Simplified")
       
    for A in (False, True):
        for B in (False, True):
            for C in (False, True):
                left = expr_original(A, B, C)
                right = expr_simplified(A, B, C)
                if verbose:
                    print(f"{int(A)}  {int(B)}  {int(C)}            {int(left)}             {int(right)}")
                if left != right:
                    ok = False
    return ok

if __name__ == "__main__":
    print("logic")
    print("simplifies to: not B")

    same = verify_equivalence(verbose=True)
    print("all inputs:", "we did it its so much faster now as fast as meeee " if same else "failed")
