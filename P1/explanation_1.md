For the __LRU_Cache__ problem, after thinking of using different approaches (included previous failures), it has been
decided to use the __OrderedDict()__, specifically the use of the _method_ __.popitem(last=False)__. It allows to 
remove the _first added element_, which is basic for the __priority construction__ demanded. 

### Time and Space complexity
In respects to the limitation of the _cache_, any hashing approach has been discarded, as the __risk of collision__, 
hence the necessity of adding a __nested hash__ (reaching __O(n)__). Finally deciding for this approach that satisfies
the __O(1)__ requirement. As in therms of _space complexity_, the structure requires the usage of __c__, being __c__
the desired *LRU_Cache* capacity; being it in the end assimilable to __O(n)__.