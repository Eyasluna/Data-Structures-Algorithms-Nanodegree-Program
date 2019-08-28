The implementation of the Huffmann Algorithm has consisted _as
pseudo code tasks were resolved_, in the construction of several __classes__, being:
1. Node
2. Queue
3. Tree
4. HuffmanEncoder 

This has allowed to have a more encapsulated development, as well as, providing the project with a more consistent
structure. The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size. 

In respects to the study of the _time complexity_, would be __O(Ln)__, being _**L**_ the maximum length of a codeword; 
If I had not used a _built it_ function for sorting the input that takes __O(n*log(n))__; ending up the time complexity being __O(n*log(n))__. In 
respects to the _space complexity_, it is directly related to the __size of the employed alphabet__, in this case
**_k_**, resulting in __O(k)__.
