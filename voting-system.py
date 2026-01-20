MAX_CANDIDATES = 5
MAX_VOTERS = 100

candidates = []
voters = []

def add_candidates():
    n = int(input(f"Enter number of candidates (max {MAX_CANDIDATES}): "))
    if n > MAX_CANDIDATES:
        print("Limit exceeded!")
        n = MAX_CANDIDATES

    candidates.clear()
    for i in range(n):
        name = input(f"Candidate {i+1} name: ")
        candidates.append({"name": name, "votes": 0})
    print("Candidates added successfully.\n")


def view_candidates():
    print("\nCandidates List:")
    for i, c in enumerate(candidates, start=1):
        print(f"{i}. {c['name']} - {c['votes']} votes")


def register_voters():
    n = int(input(f"Enter number of voters (max {MAX_VOTERS}): "))
    if n > MAX_VOTERS:
        print("Limit exceeded!")
        n = MAX_VOTERS

    voters.clear()
    for i in range(n):
        print(f"\nVoter {i+1}")
        name = input("Name: ")
        voter_id = input("Voter ID: ")
        password = input("Password: ")
        voters.append({
            "name": name,
            "id": voter_id,
            "password": password,
            "has_voted": False
        })
    print("Voters registered successfully.\n")


def verify_voter(voter_id, password):
    for i, v in enumerate(voters):
        if v["id"] == voter_id and v["password"] == password:
            if v["has_voted"]:
                print("You have already voted!")
                return None
            return i
    print("Invalid Voter ID or Password!")
    return None


def cast_vote(voter_index):
    view_candidates()
    choice = int(input("Enter candidate number to vote: "))

    if choice < 1 or choice > len(candidates):
        print("Invalid choice!")
        return

    candidates[choice - 1]["votes"] += 1
    voters[voter_index]["has_voted"] = True
    print("Vote cast successfully!\n")


def display_results():
    if not candidates:
        print("No candidates available.")
        return

    print("\nElection Results:")
    max_votes = max(c["votes"] for c in candidates)

    winners = [c["name"] for c in candidates if c["votes"] == max_votes]

    for c in candidates:
        print(f"{c['name']} : {c['votes']} votes")

    if len(winners) > 1:
        print("\nResult is a TIE between:")
        for w in winners:
            print("-", w)
    else:
        print(f"\nWinner: {winners[0]}")


def main():
    while True:
        print("\n===== VOTING SYSTEM =====")
        print("1. Add Candidates")
        print("2. Register Voters")
        print("3. Vote")
        print("4. Display Results")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_candidates()
        elif choice == "2":
            register_voters()
        elif choice == "3":
            voter_id = input("Enter Voter ID: ")
            password = input("Enter Password: ")
            index = verify_voter(voter_id, password)
            if index is not None:
                cast_vote(index)
        elif choice == "4":
            display_results()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice!")


main()
