# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

        
        
'''
Borrowed from OsamaAdel's post in 2016
This is a hard exercise indeed. But things will be much easier when you know the following.
Let's assume we have 8 digits, each digit can hold either 1 or 0, how many combinations can be made ? .. let's draw a table :

d8    d7    d6    d5    d4    d3    d2    d1
0     0     0     0     0      0      0     0
0     0     0     0     0      0      0     1
0     0     0     0     0      0      1     0
0     0     0     0     0      0      1     1
0     0     0     0     0      1      0     0
0     0     0     0     0      1      0     1
..
..
..
1     1     1     1     1      1      1     1

The number or rows (which is the same as the number of different combinations) is equal to 2**8 (8 is the number of digits).
So, basically .. until now we are just talking about the number of combinations. However, this is well related to binary numbering system.
In binary system, a number is represented in 1's and 0's. The digits have weights which mean, the number under d8 in the previous example will be multiplied by 128 (so if under d8 there is 1, it will worth 128, otherwise it will worth 0) .. and the number under d7 will be multiplied by 64 .. the multiplicands are powers of 2 and are decreasing from left to right .. until d1 which is multiplied by 1 (2**0). So what we get if all the 8 digits are 1's ? 1*128 + 1*64 + 1*32 + 1*16 + 1*8 + 1*4 + 1*2 + 1*1 = 255. So, how many numbers can be represented in those 8 digits ? actually it's the same questions as "how many combinations can be made using 8 digits" and the answer is 2**8.
If you understand what I have said so far, then the rest will be easy.
The code in powerSet make use of this similarity between binary numbers and the idea of the number of combinations. So, if we have N items, we could have 2**N different combinations, we can also represent each combination using a different binary number represented in N digits.
So if the items are pizza, cheese, apple, water, juice, meat, egg, rice we can write the table again but a little bit different

pizza   cheese   apple   water   juice   meat   egg   rice
0       0        0       0       0       0      0     0
0       0        0       0       0       0      0     1
0       0        0       0       0       0      1     0
0       0        0       0       0       0      1     1
0       0        0       0       0       1      0     0
...
...
1       1        1       1       1       1      1     1

1 means that we will take that item, 0 means that we won't take it. At the same time, we can represent each different combination by it's corresponding binary value. So taking "rice" only is equal to 1, taking rice and egg is equal to 3 .. and etc.
So what does the code says ? First, it iterates through all 2**N possible combinations (possible binary numbers) Second, for each combination of them (represented in its binary form) check for the 1's inside the number and add the corresponding items to the combo list. But how does it do it ? In a very smart way.
The shift operator >> shifts all digits to the right X times, where X is the number on the right of the >> operator. For example, 8 (which is equal to 1000) >> 1, will shift the 4 digits 1 step to the right to be (0100) which is equal to 4. Even numbers in binary always have 0 as the first digit on the right whereas odd numbers have 1 as the first number on the right. So, 8 (1000) has 0 on the right .. when we shift it right by 1 .. 4(0100) has 0 on the right, 2(0010) has 0 on the right .. 1(0001) has 1 on the right. So, if we check if the number is odd or not, we can know if there is 1 on the right or not.
Using this idea, the code tries to shift each different combination by numbers from 0 to N, each time it checks if it's odd or not by checking if there's a remainder of 1 (if (i >> j) % 2 == 1) .. if so, then the number of times we shifted the current combination (j in this case) is the original position of the 1 in the combination .. which we can use as an index for the corresponding item we want to take.
So if the current combination is 1000 (8) and by shifting it 3 times to the right we have 0001 which is odd, we know that 1 in 1000 is the 3rd bit (starting from 0 from the right to the left). if the list of items are [rice, meat, egg, juice] then items[3] is juice.
So, for each different combination, we use the binary representation of that combination and use the previous method to search for the 1's in the number and add the corresponding items to the list of the items to be taken.
It's quite long and complex especially for those who never got exposed to binary numbers before .. but this is the trick.
The solution to the exercise is quite tricky .. I'm not going to post anything about it here but the idea is so similar but is still tricky.
Good luck.
'''
