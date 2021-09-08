# Documentation of package lin_algebra

> This is the documentation of a package named lin-algebra. This package includes a function which can help with many linear algebra problems. \
> Copyright (c) 2021 Wojciech Fiołka 

# lin-algebra.Matrix

### Constructor
> *Take a two-dimensional list as a parameter and make a Matrix object.*

### Operators overloaded

>- (+) *add two matrices and return a Matrix object with added elements.*
>- (-) *subtract two matrices and return a Matrix object with subtracted elements.*
>- (* num) (type float or int) *multiply all elements of Matrix by the number.*
>- (* Matrix) *make matrix multiplication and return the Matrix object of it.*
>- (+=) *add each element of the called Matrix to the corresponding element.*
>- (-=) *subtract each element of the called Matrix by corresponding element.*
>- (*= num) (type float or int) *multiply all elements of the called Matrix by the number.*
>- (*= Matrix) *make matrix multiplication and change called Matrix to the result of it.*
>- (==) *return true if all elements are the same.*
>- (!=) *return true if it is the difference between two matrices.*

### Operations on matrices

>- **det()**  *return determinant of the squared matrix.*
>- **is_squared()**  *return true if the matrix is squared and false if it is not.*
>- **T()**  *return a Matrix objets which is the transpose of the called matrix.*
>- **inv()**  *return a Matrix object which is inverse of the called matrix.*

### Operations on the diagonal and antidiagonal

>- **is_diagonal()**  *return if the called matrix is diagonal.*
>- **get_main_diagonal()**  *return list includes elements of main diagonal.*
>- **is_identity()**  *return if the called matrix is identity.*
>- **is_antidiagonal()**  *return if the called matrix is anti-diagonal.*
>- **get_antidiagonal()**  *return list includes elements of antidiagonal.*
>- **is_exchange()**  *return if the called matrix is exchanged.*
>- **trace()**  *return trace of diagonal matrix.*

### Other functions

>- **size()** *return tuple with number of rows and columns.*
>- **print()**  *print matrix.*
>- **gen_zero(rows, columns)** *return Matrix objects with size specified by rows 
and columns.*
>- **gen_random(rows, columns)**  *return Matrix objects with size specified by rows 
and columns.*




# lin-algebra.Vector

### Constructor
>*Take as parameter one-dimensional list and create Vector object*

### Overloaded operators

>- (+) *add two vectors and return a Vector object with added elements.*
>- (-) *subtract two vectors and return a Vector object with subtracted elements.*
>- (* num) (type float or int) *multiply all elements of Vector by the number.*
>- (* Vector) *make a dot product and return the result of it.*
>- (+=) *add to each element of the called Vector the corresponding element.*
>- (-=) *subtract each element of the called Vector by corresponding element.*
>- (*= num) (type float or int) *multiply all elements of the called Vector by the number.*
>- (*= Vector) *make a dot product and change the called Vector to the result of it.*
>- (==) *return true if all elements are the same.*
>- (!=) *return true if it is the difference between two vectors.*

### Operations on vectors

>- **vector_scalar_product(scalar)**  *multiply each element by scalar and return the new vector*
>- **dot(V1)**  *return dot product of vectors*
>- **cross(V1)**  *return tuple includes Vector object with elements created by cross product and length of the result vector*

### Other functions

>- **size()**  *return the size of the Vector.*
>- **length()**  *return the length of the Vector.*
>- **print()**  *prints vector.*
>- **gen_zero(dimensions)**  *return Vector object of zero vector*
>- **gen_random(dimensions)**  *return Vector object with random values from 0 to 30*

