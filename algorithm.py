def recursion_tree(n):
    level = 0
    total_cost = 0
    original_n = n
    output_lines = []

    output_lines.append("Recursion Tree Analysis")
    output_lines.append("Recurrence: T(n) = 2T(n/2) + n^2\n")
    output_lines.append("-------------------------------------------------------------------------")
    output_lines.append("{:<10} {:<20} {:<20} {:<20}".format(
        "Level", "No. of Subproblems", "Subproblem Size", "Cost at Level"
    ))
    output_lines.append("-------------------------------------------------------------------------")

    while True:
        num_subproblems = 2 ** level
        subproblem_size = original_n // (2 ** level)

        if subproblem_size < 1:
            break

        cost_at_level = num_subproblems * (subproblem_size ** 2)
        total_cost += cost_at_level

        output_lines.append("{:<10} {:<20} {:<20} {:<20}".format(
            level,
            num_subproblems,
            subproblem_size,
            cost_at_level
        ))

        if subproblem_size == 1:
            break

        level += 1

    output_lines.append("-------------------------------------------------------------------------")
    output_lines.append(f"\nHeight of Recursion Tree = log₂(n) ≈ {level}")
    output_lines.append(f"Total Work T(n) = {total_cost}")
    output_lines.append("\nUsing Geometric Series:")
    output_lines.append("Total Cost = n^2 (1 + 1/2 + 1/4 + ...)")
    output_lines.append("Total Cost ≤ 2n^2")
    output_lines.append("\nFinal Asymptotic Complexity: Θ(n^2)")

    # Write to file
    with open("recursion_tree_output.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

    # Print output
    for line in output_lines:
        print(line)


# Main Program
n = int(input("Enter value of n (power of 2 recommended): "))
recursion_tree(n) 