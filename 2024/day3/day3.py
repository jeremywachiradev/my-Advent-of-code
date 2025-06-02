
input ="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
inputlen=len(input)

def solution(input):
    l,r=0,0
    output=1
    while l<inputlen:
        if input[l]!="m":
            l+=1
        else:
            r=l+3
            # r is pointing to "("
            # ideally l:r(inclusive of r) points to "mul("
            if r>=inputlen:
                break
            elif input[l:r+1]=="mul(":
                bool_val,closing_bracket=isvalidmul(r)
                if bool_val:
                    multiplied_value=parse_and_multiplymul(r,closing_bracket)
                    output+=(multiplied_value)
                else:
                    #jump out of the if and continue with moving through the string
                    l+=1
                    continue

            else:
                l+=1
    return output
def parse_and_multiplymul(opening_bracket,closing_bracket):
    temp_arr=[input[opening_bracket:closing_bracket].split(",")]
    return int(temp_arr[0])*int(temp_arr[1])

def isvalidmul(r):
    pointer=r+1
    while pointer<=inputlen:
        if input[pointer].isdigit()==False:
            if input[pointer]==",":
                pointer+=1
                while pointer<=inputlen:
                    if input[pointer].isdigit()==False:
                        if input[pointer]==")":
                            # return both the Truth and POINTER WHICH CURRENTLY POINTS AT ")"
                            return True,pointer
                        else:
                            return False,pointer
            else:
                return False,pointer

        pointer+=1
         
print(solution(input))