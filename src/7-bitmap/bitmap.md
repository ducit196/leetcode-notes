# Bit manipulation

### Basic operation
**Basic**  
AND: X & Y: = 1 if both 1, otherwise 0  
OR : X | Y: = 0 if both 0, otherwise 1  
XOR: X ^ Y: = 0 if same bit, 1 if different bit. 1 ^ 1 = 0, 1 ^ 0 = 1(Best for flip bit)  
NOT: ~X: flip all bit of X  
**Shift**  
Left shift:  a << k: a = a * 2^k  
Right shift: a >> k: a = a / 2^k

**2 complement**  
```plaintext
a = 12:  0(x28)1100
~a = -13: 1(x28)0011
Then -12 = ~a + 1 = 1(x28) + 1
General: change a to -a: -a = ~a + 1
In python code: 
```
### Common function
Get Kth bit of x:
```plaintext
    def getBit(int x, int k):
        return (x >> k) & 1 #Shift kth to right most, and with 1
```
Set Kth bit of x to 1:
```plaintext
    def setBitOne(int x, int k):
        return x | (1 << k) #Shift bit 1 to k index, and with 1
```

Set Kth bit of x to 0:
```plaintext
    def setBitZero(int x, int k):
        return x & ~(1 << k) #Shift kth to right most, and with 1
```
Flit Kth bit of x
```plaintext
    def flip(int x, int k):
        return x ^ (1 << k) # x ^ 1 --> ~x, x ^ 0 = x
```
### Trick
Clear right most bit 1 of x:  
    x = x & x - 1


XOR Properties:  
Commutativity: aXORb=bXORa
The order in which you XOR two numbers doesn’t matter.

Associativity: (aXORb)XORc=aXOR(bXORc)
Grouping of XOR operations doesn’t affect the result.

Identity: aXOR0=a
XOR with 0 leaves the number unchanged.

Self-inverse: aXORa=0
XORing a number with itself results in 0.

Inversion:
If aXORb=c, then:

a=bXORc
b=aXORc