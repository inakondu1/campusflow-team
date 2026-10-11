from campusflow.tickets import create_ticket, assign_ticket
from campusflow.workflow import update_status
from campusflow.reports import get_queue, generate_report
from campusflow.storage import save_tickets, load_tickets

tickets = load_tickets("tickets.json")

while True:
    print("\nCampusFlow")
    print("1. Create ticket")
    print("2. List tickets")
    print("3. Assign ticket")
    print("4. Update status")
    print("5. Queue")
    print("6. Reports")
    print("0. Exit")

    choice = input("Choose an option: ")
    if choice == "0":
        save_tickets(tickets, "tickets.json")
        break
    if choice == "1":
        title = input("Enter ticket title: ")
        category = input("Enter category: ")
        urgency = input("Enter urgency: ")
        affected_users = input("Enter number of affected users: ")

        try:
            affected_users = int(affected_users)
        except ValueError:
            print("Invalid number of affected users")
            continue

        result = create_ticket(title, category, urgency, affected_users, tickets)
        print(result)

    if choice == "2":
        if not tickets:
            print("No tickets found")
        else:
            for ticket in tickets:
                print(ticket)