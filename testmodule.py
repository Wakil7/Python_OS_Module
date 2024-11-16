# import matplotlib.pyplot as plt

# def first_fit_with_multiple_processes(memory_blocks, process_sizes):
#     # Initialize the figure for visualization
#     fig, (ax1, ax2) = plt.subplots(1, 2)

#     # Set limits for both axes
#     ax1.set_ylim(0, sum(memory_blocks))  # Y-axis: total memory size
#     ax1.set_xlim(0, 2)  # X-axis: memory blocks

#     ax2.set_ylim(0, sum(memory_blocks))  # Y-axis: total memory size
#     ax2.set_xlim(0, 2)  # X-axis: memory blocks

#     # Set titles and labels
#     ax1.set_title("Initial Memory Status")
#     ax1.set_xlabel("Memory Blocks")
#     ax1.set_ylabel("Memory Size")

#     ax2.set_title("Final Memory Status (After First Fit)")
#     ax2.set_xlabel("Memory Blocks")
#     ax2.set_ylabel("Memory Size")

#     # Draw initial memory blocks (light gray) on ax1
#     start_y = 0
#     for i, block_size in enumerate(memory_blocks):
#         ax1.bar(1, block_size, bottom=start_y, width=0.8, color='lightgray', edgecolor='black')
#         ax1.text(1.5, start_y + block_size / 2, f"Block {i+1}", ha="center", va="center", fontsize=10)
#         start_y += block_size

#     # Draw memory blocks and allocate processes on ax2 (final state)
#     allocated_processes = []
#     start_y = 0
#     temp_process_sizes = process_sizes.copy()  # Copy of process sizes to modify them

#     for i, block_size in enumerate(memory_blocks):
#         # Draw the memory block as a bar on ax2 (same for initial and final)
#         ax2.bar(1, block_size, bottom=start_y, width=0.8, color='lightgray', edgecolor='black')
#         ax2.text(1.5, start_y + block_size / 2, f"Block {i+1}", ha="center", va="center", fontsize=10)

#         remaining_space = block_size  # Track remaining space in the current block
#         process_y = start_y  # Position for the first process in the block

#         # Try to allocate multiple processes to the current block in ax2
#         for j, process_size in enumerate(temp_process_sizes):
#             if process_size <= remaining_space and process_size != -1:
#                 allocated_processes.append(process_size)
#                 ax2.bar(1, process_size, bottom=process_y, width=0.8, color='green', edgecolor='black')
#                 ax2.text(1.5, process_y + process_size / 2, f"Process {j+1}", ha="center", va="center", fontsize=10, color="white")
#                 process_y += process_size  # Update position for next process in the block
#                 remaining_space -= process_size  # Decrease the remaining space
#                 temp_process_sizes[j] = -1  # Mark the process as allocated

#         start_y += block_size

#     # Show the plot
#     plt.tight_layout()
#     plt.show()

# # Example data
# memory_blocks = [10, 20, 30, 40, 50]  # Memory block sizes
# process_sizes = [12, 5, 8, 6, 7, 15, 20]  # Process sizes (some can fit together)

# first_fit_with_multiple_processes(memory_blocks, process_sizes)
