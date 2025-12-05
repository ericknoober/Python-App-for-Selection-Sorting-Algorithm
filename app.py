import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import time

#selection sort steps
def selection_sort_steps(numbers):
    
    arr = numbers.copy()
    n = len(arr)
    steps = []

    # inital state
    steps.append((arr.copy(), -1, -1, -1, "Starting"))

    for i in range(n):
        min_idx = i
        steps.append((arr.copy(), i, -1, min_idx, f"Finding min from position {i}"))

        for j in range(i + 1, n):
            # compare values
            steps.append((arr.copy(), i, j, min_idx, f"Comparing {arr[j]} with {arr[min_idx]}"))
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                steps.append((arr.copy(), i, j, min_idx, f"New minimum: {arr[min_idx]}"))
        
        if min_idx != i:
            # before swap
            steps.append((arr.copy(), i, min_idx, min_idx, f"Swapping {arr[i]} and {arr[min_idx]}"))
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            # after swap
            steps.append((arr.copy(), i, -1, -1, f"Swapped! {arr[i]} in position"))
        else:
            steps.append((arr.copy(), i, -1, -1, f"Element {arr[i]} already in correct position"))
    
    # sorted state
    steps.append((arr.copy(), -1, -1, -1, "Sorting Completed!"))
    return steps

#creating the graph
def create_visualization(arr, current_idx, comparing_idx, min_idx, status):
    
    # size of graph
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # color coding
    colors = []
    for i in range(len(arr)):
        if status == "Sorting Completed!":
            colors.append('lightgreen')
        elif i == current_idx:
            colors.append('orange')
        elif i == comparing_idx:
            colors.append('yellow')
        elif i == min_idx:
            colors.append('red')
        else:
            colors.append('lightblue')
    
    # bars
    bars = ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', linewidth=1)
    
    # value labels on bars
    for bar, value in zip(bars, arr):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{value}', ha='center', va='bottom', fontweight='bold')
    
    # plot characteristics
    ax.set_title(f"Selection Sort Visualization\nStatus: {status}", fontsize=14, fontweight='bold')
    ax.set_xlabel("Array Index")
    ax.set_ylabel("Value")
    ax.set_xticks(range(len(arr)))
    
    # grid
    ax.grid(True, axis='y', alpha=0.3)
    plt.tight_layout()
    
    return fig

#switching between each graph to show each step and pass
def run_visualization(input_numbers, speed):
    
    # parse numbers
    try:
        numbers = [int(x.strip()) for x in input_numbers.split(",") if x.strip()]
    except Exception as e:
        numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # limit array size to less than 10
    if len(numbers) > 10:
        numbers = numbers[:10]
    
    # get selection sort steps
    steps = selection_sort_steps(numbers)
    
    # calculate sorting speed
    delay = max(0.1, 2.0 - (speed / 100 * 1.9))
    
    # sort speed
    for step_num, step_data in enumerate(steps):
        print(f"Debug: Yielding step {step_num + 1}")  # Debug print
        arr, curr_idx, comp_idx, min_idx, status = step_data
        fig = create_visualization(arr, curr_idx, comp_idx, min_idx, status)
        yield fig
        time.sleep(delay)

# create ui and text
with gr.Blocks() as demo:
    gr.Markdown("""
    # Selection Sort Visualization
    Selection sort is a basic comparsion-based sorting algorithm 
    that iterates through an array to find the minimum element and put it at the start.
    It always have a time complexity of O(n²) and a space complexity of O(1) since it sorts in-place.
    Selection sort is a simple alogirthm which can be used to learn the key concepts of computer science, 
    but has its disadvantages when sorting big data sets.
    """)
    
    with gr.Row():
        with gr.Column():

            #number inputs
            input_numbers = gr.Textbox(
                label="Numbers to sort",
                value="64, 34, 25, 12, 22, 11, 90",
                placeholder="Enter less than 10 numbers separated by commas",
                max_lines=1
            )

            #speed slider
            speed_slider = gr.Slider(
                minimum=1,
                maximum=100,
                value=75,
                label="Animation Speed",
                info="1 = Slowest, 100 = Fastest"
            )
            
            visualize_btn = gr.Button("Start Sorting", variant="primary")

            #colour legend
            gr.Markdown("""
            ### Color Legend:
            - **Blue**: Unsorted elements
            - **Orange**: Current position
            - **Yellow**: Comparing
            - **Red**: Current minimum
            - **Green**: Sorted
            """)
        
        with gr.Column():
            plot_output = gr.Plot(label="Sorting Process")
    
    # example options
    gr.Examples(
        examples=[
            ["17,23,14,2,30,29,9,43"],
            ["3,20,5,7,1,14"],
            ["1,2,3,4,5"],
            ["5,4,3,2,1"]
        ],
        inputs=[input_numbers],
        label="Examples:"
    )
    
    # add action to button
    visualize_btn.click(
        fn=run_visualization,
        inputs=[input_numbers, speed_slider],
        outputs=plot_output
    )
    
# launch app
demo.launch()
