For the __union and intersection__ problem, the approach has been to transform the _linked lists_, a format which is
harder to work with, on something much __simpler__ as is a list. Once the transformation has been done, the combination
with the handy _object_ __sets__, has done all the work.


In the study of the __time complexity__, we find that the transformation from _linked list_ to list, takes __O(n)__
 time complexity, the the set function is in the __same or less__ order of magnitude, as for the variations:
- _Union_: we find the creation of the final array, again __O(n)__, making __n*O(n)__ be resulting to __O(n)__
- _Intersection_: we find the creation of the final array, which is a _double for-loop_ (operation _x in s_, acts with 
 __O(n)__), resulting finally in __O(n^n)__