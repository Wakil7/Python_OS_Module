# import matplotlib.pyplot as plt

# def fcfs_gantt_chart(processes, burst_times):
#     n = len(processes)

#     # Calculate waiting time and start time
#     start_times = [0] * n
#     for i in range(1, n):
#         start_times[i] = start_times[i-1] + burst_times[i-1]

#     # Calculate completion times
#     completion_times = [start_times[i] + burst_times[i] for i in range(n)]

#     # Normalize bar lengths to make them equal
#     normalized_burst = [1] * n  # Equal length bars

#     # Plotting the Gantt Chart
#     fig, gnt = plt.subplots(figsize=(12, 6))
#     # plt.subplots_adjust(bottom=0.3)  # Adjust space at the bottom for labels

#     gnt.set_ylim(0, 30)
#     gnt.set_xlim(0, n + 1)
#     gnt.set_xlabel('Processes')
#     gnt.set_yticks([])
#     gnt.set_xticks([])  # Removed xticks to hide process labels at the bottom
#     gnt.set_title('FCFS Scheduling Gantt Chart (Equal Length Divisions)')

#     # Adding the bars for each process with equal length
#     for i in range(n):
#         gnt.barh(10, normalized_burst[i], left=i, height=5, align='center', color='skyblue', edgecolor='black')
#         plt.text(i + 0.5, 10, f"P{processes[i]}", ha='center', va='center', color='black', fontweight='bold')

#     # Adding completion times directly aligned to the right end of each bar
#     for i in range(n):
#         plt.text(i + 1, 6, f"{completion_times[i]}", ha='center', va='center', color='blue', fontweight='bold')

#     plt.show()


# # Example data
# processes = [1, 2, 3, 4]               # Process IDs
# burst_times = [5, 9, 6, 4]             # Burst times for each process

# # Generating Gantt Chart
# fcfs_gantt_chart(processes, burst_times)

# import matplotlib.pyplot as plt

# def cpuscheduling(self, data):
#     n = len(data)

#     # Initialize figure
#     plt.figure(figsize=(12, 4))

#     # Set axis limits dynamically based on the number of processes
#     plt.xlim(0, n + 1)  # Adjust the xlim based on the number of processes
#     plt.ylim(0, 30)     # You can adjust this if needed to fit the y-axis

#     # Add title and hide ticks
#     plt.title("Gantt Chart")
#     plt.xticks([])  # Hide x-ticks
#     plt.yticks([])  # Hide y-ticks

#     # Create Gantt bars
#     for i, pid in enumerate(data.keys()):
#         ct = data[pid][0]  # Completion time
#         plt.barh(15, 1, left=i, height=5, color="skyblue", edgecolor="black")  # Plot bars
#         # Process ID text centered above the bars
#         plt.text(i + 0.5, 15, str(pid), color="black", fontweight="bold", ha="center", va="center")
#         # Completion time text below the bars
#         plt.text(i + 1, 9, str(ct), color="black", fontweight="bold", ha="center", va="center")

#     # Show the plot
#     plt.show()

# # Example usage:
# data = {
#     1: [5],
#     2: [10],
#     3: [15],
#     4: [20]
# }

# cpuscheduling(None, data)


# def fcfs_gantt_chart(processes, burst_times):
#     n = len(processes)

#     # Calculate waiting time and start time
#     start_times = [0] * n
#     for i in range(1, n):
#         start_times[i] = start_times[i-1] + burst_times[i-1]

#     # Calculate completion times
#     completion_times = [start_times[i] + burst_times[i] for i in range(n)]

#     # Normalize bar lengths to make them equal
#     normalized_burst = [1] * n  # Equal length bars

#     # Calculate the max x limit to add extra space on the right
#     extra_space = 0.5  # Adjust this value for more/less space
#     max_x_limit = n + extra_space

#     # Plotting the Gantt Chart using plt.barh()
#     plt.figure(figsize=(12, 4))
#     plt.ylim(0, 30)
#     plt.xlim(0, max_x_limit)  # Added extra space on the right
#     plt.xlabel('Processes')
#     plt.title('FCFS Scheduling Gantt Chart (Equal Length Divisions)')
    
#     # Hiding y-axis ticks
#     plt.xticks([])
#     plt.yticks([])

#     # Adding the bars for each process with equal length
#     for i in range(n):
#         plt.barh(15, normalized_burst[i], left=i, height=8, color='skyblue', edgecolor='black')
#         plt.text(i + 0.5, 15, f"{processes[i]}", color='black', fontweight='bold')

#     # Adding completion times directly aligned to the right end of each bar
#     for i in range(n):
#         plt.text(i + 1, 2, f"CT: {completion_times[i]}", ha='center', va='center', color='blue', fontweight='bold')

#     # Display the plot
#     plt.show()

# # Example data
# processes = [1, 2, 3, 4]               # Process IDs
# burst_times = [5, 9, 6, 4]             # Burst times for each process

# # Generating Gantt Chart
# fcfs_gantt_chart(processes, burst_times)

import matplotlib.pyplot as plt

def first_fit_with_multiple_processes(memory_blocks, process_sizes):
    # Initialize the figure for visualization
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Set limits for both axes
    ax1.set_ylim(0, sum(memory_blocks))  # Y-axis: total memory size
    ax1.set_xlim(0, 2)  # X-axis: memory blocks

    ax2.set_ylim(0, sum(memory_blocks))  # Y-axis: total memory size
    ax2.set_xlim(0, 2)  # X-axis: memory blocks

    # Set titles and labels
    ax1.set_title("Initial Memory Status")
    ax1.set_xlabel("Memory Blocks")
    ax1.set_ylabel("Memory Size")

    ax2.set_title("Final Memory Status (After First Fit)")
    ax2.set_xlabel("Memory Blocks")
    ax2.set_ylabel("Memory Size")

    # Draw initial memory blocks (light gray) on ax1
    start_y = 0
    for i, block_size in enumerate(memory_blocks):
        ax1.bar(1, block_size, bottom=start_y, width=0.8, color='lightgray', edgecolor='black')
        ax1.text(1.5, start_y + block_size / 2, f"Block {i+1}", ha="center", va="center", fontsize=10)
        start_y += block_size

    # Draw memory blocks and allocate processes on ax2 (final state)
    allocated_processes = []
    start_y = 0
    temp_process_sizes = process_sizes.copy()  # Copy of process sizes to modify them

    for i, block_size in enumerate(memory_blocks):
        # Draw the memory block as a bar on ax2 (same for initial and final)
        ax2.bar(1, block_size, bottom=start_y, width=0.8, color='lightgray', edgecolor='black')
        ax2.text(1.5, start_y + block_size / 2, f"Block {i+1}", ha="center", va="center", fontsize=10)

        remaining_space = block_size  # Track remaining space in the current block
        process_y = start_y  # Position for the first process in the block

        # Try to allocate multiple processes to the current block in ax2
        for j, process_size in enumerate(temp_process_sizes):
            if process_size <= remaining_space and process_size != -1:
                allocated_processes.append(process_size)
                ax2.bar(1, process_size, bottom=process_y, width=0.8, color='green', edgecolor='black')
                ax2.text(1.5, process_y + process_size / 2, f"Process {j+1}", ha="center", va="center", fontsize=10, color="white")
                process_y += process_size  # Update position for next process in the block
                remaining_space -= process_size  # Decrease the remaining space
                temp_process_sizes[j] = -1  # Mark the process as allocated

        start_y += block_size

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example data
memory_blocks = [10, 20, 30, 40, 50]  # Memory block sizes
process_sizes = [12, 5, 8, 6, 7, 15, 20]  # Process sizes (some can fit together)

first_fit_with_multiple_processes(memory_blocks, process_sizes)
