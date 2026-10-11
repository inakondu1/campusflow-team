AI Learning Log — Engineer B (Ina)
1. Sorting Tickets

    What I needed to learn: How to sort tickets by priority first, and then by ID number if priorities are the same.

    What AI told me: Use a tuple like (-priority, id_number) inside Python's sorted function.

    How I tested it: I ran tests with sample tickets to make sure T001 came before T002 when priorities matched.

    Result: It worked perfectly. Now I know how tuple sorting works in Python.

2. Saving and Loading JSON Files

    What I needed to learn: How to save data safely without crashing if the file is missing or broken.

    What AI told me: Check if the file exists first, and catch json.JSONDecodeError if the file has bad data.

    How I tested it: I made a test file with broken text and checked that it raised a clear error instead of wiping our data.

    Result: Accepted and used in storage.py.

3. Fixing AI Ticket Status Rules

    What I needed to learn: How to control ticket status changes (open to in_progress to resolved).

    What AI suggested: The AI allowed a resolved ticket to go straight back to in_progress.

    Why I changed it: Our project rules say a resolved ticket must first be reopened to open.

    Result: I rejected the AI's original rule and wrote a strict check so resolved tickets can only go back to open.