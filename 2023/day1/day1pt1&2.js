let input=`two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
`.trim().split("\n")

function solution(input){
    output=0
    my_starts_with_dict={
        "o":1,"t":2,"f":3,"s":4,"e":5,"n":6
    }
    my_dict={
        "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"
    }
    return input.reduce((sumation,word)=>{
        my_arr=[]
        for (i=0;i<word.length;i+=1){
            char=word[i]
            if (!isNaN(Number(char))){
                my_arr.push(char)
                my_chars=""
            }
            else if (char in my_starts_with_dict){
                    for (num in my_dict){
                        if (word.slice(i,i+num.length)===num){
                            my_arr.push(my_dict[num])
                            break
                        }
                    }
    
}
                    }
    
                
            

        
        const firstDigit = my_arr[0];
        const lastDigit = my_arr[my_arr.length - 1];
        const twoDigitNumber = Number(firstDigit + lastDigit);
        console.log(my_arr)
        return sumation + twoDigitNumber;
       
    },0)
    
    
}
      
     console.log(solution(input))
