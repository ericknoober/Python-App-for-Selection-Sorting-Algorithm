# Python-App-for-Selection-Sorting-Algorithm
Title: SelectionSortApp

Screenshots of testing:
This screenshot shows how entering nothing into the array will automatically finish the sorting algorithm without error.
<img width="1048" height="384" alt="image" src="https://github.com/user-attachments/assets/986d77b1-ddf0-4b0e-9019-8fe1ee49f9a1" />
Entering more than 10 elements will only take the first 10 since selection sort is slow for better visualization.
<img width="1464" height="673" alt="image" src="https://github.com/user-attachments/assets/93102aba-912a-4df5-8c6c-62e3241efbe8" />
Animation speed slider works and best used at 75 for best visualization.
<img width="687" height="89" alt="image" src="https://github.com/user-attachments/assets/54f6a0ff-c6aa-4d19-a511-5ffab0b84f94" />

Predetermined example buttons work and change the next inputted array to be sorted
<img width="439" height="77" alt="image" src="https://github.com/user-attachments/assets/6b6b68cd-d0cf-4541-a5d3-af389d8a11b5" />

Why I chose it: I chose selection sort because of the complexity of its sorting alogorithm. I didn't want to choose something simple like linear search or bubble sort and wanted to challenge my understanding on the topic of sorting alogorithms and use a visual application in order to understand my learning.

Problem Breakdown & Computational Thinking:
Decomposition: To run the selection sort algorithm, the key components are the iterations to determine the minimum value in each pass, keeping track of all the relevant values, and swapping elements.
Pattern Recognition: Selection sort repeatedly searches through the array for the smallest value and constantly makes swapps with the left indexes. 
Abstraction: The user does not see the code of the alogorithm, but only the visualization needed to understand the topic.
Algorithm Design: The user would input an array and would be processed through my selection sort algorithms along with gradio. The output would be the gradio visualization of the sorting algorithm. 

Steps to run:
1. Enter numbers seperated by commas and less than 10 in the textbox
2. Change the animation speed to 75 for best animation
3. Click start sorting to see visualization
4. Wait for animation to finish before seleting another array

Hugging face link: https://huggingface.co/spaces/ericknoober/SelectionSortApp
